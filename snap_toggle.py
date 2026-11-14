# SPDX-License-Identifier: GPL-3.0-or-later
"""Snap Toggle — enable and disable selected snap types in IngeTrazo.

Adds a panel (Extensions ▸ Snaps…) with checkboxes for each snap/inference type.
Unchecked types are blocked: the snap result is replaced with a raw (unsnapped)
point so the cursor no longer locks to that snap.

Install: copy this file to %APPDATA%\\ingetrazo\\plugins\\ and restart IngeTrazo.
"""

from __future__ import annotations

import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from core.snap import COLOR_NONE, SnapResult

log = logging.getLogger("ingetrazo.plugins.snap_toggle")

# (kind, label, description)
SNAP_KINDS = [
    ("endpoint", "Endpoint", "Vertices / edge endpoints"),
    ("midpoint", "Midpoint", "Edge midpoints"),
    ("arc_midpoint", "Arc midpoint", "Midpoint along arc/circle sweep"),
    ("center", "Center", "Circle/arc centers"),
    ("origin", "Origin", "World origin"),
    ("component_origin", "Component origin", "Group/component origins"),
    ("intersection", "Intersection", "Edge/guide intersections"),
    ("intersection_edge", "Intersection (edge lock)", "Lock-line crossing with an edge"),
    ("intersection_face", "Intersection (face lock)", "Lock-line crossing with a face"),
    ("on_edge", "On edge", "Arbitrary point on an edge"),
    ("on_face", "On face", "Free point on a face"),
    ("close", "Close", "Polygon/polyline close snap"),
    ("extension", "Extension", "Edge extension/continuation guide"),
    ("from_point", "From point", "Alignment from acquired points"),
    ("aligned", "Aligned", "Aligned/level with encouraged points on a face"),
    ("axis", "Axis lock", "Explicit axis lock (arrow keys / Shift)"),
    ("axis_inference", "Axis inference", "Automatic axis inference"),
    ("reference", "Reference (parallel/perpendicular)", "Parallel/perpendicular to reference edge"),
    ("perp_face", "Perpendicular to face", "Perpendicular-to-face inference"),
    ("on_line", "On guide line", "Point on a guide line"),
    ("on_axis", "On model axis", "On model X/Y/Z axes"),
    ("through_point", "Through point", "Through-point inference"),
]

KIND_ALIASES = {
    "centre": "center",
    "parallel": "reference",
    "perpendicular": "reference",
}


def _normalize_kind(kind):
    if not kind:
        return kind
    return KIND_ALIASES.get(str(kind), str(kind))


def _known_kinds():
    return {k for k, _, _ in SNAP_KINDS}


def _disabled_set(app):
    try:
        data = app.document_data({})
    except Exception:
        data = {}
    if not isinstance(data, dict):
        data = {}
    disabled = data.get("disabled", [])
    if not isinstance(disabled, list):
        disabled = []
    known = _known_kinds()
    out = set()
    for k in disabled:
        nk = _normalize_kind(k)
        if nk in known:
            out.add(nk)
    return out


def _set_disabled(app, disabled):
    known = _known_kinds()
    cleaned = sorted(k for k in disabled if k in known)
    app.set_document_data({"disabled": cleaned, "version": 3})


def _raw_world_point(viewport, px, py):
    try:
        fn = getattr(viewport, "_world_from_pixel", None)
        if callable(fn):
            pt = fn(px, py)
            if pt is not None:
                return pt
    except Exception:
        pass
    return None


class SnapTogglePanel(QWidget):
    def __init__(self, app):
        super().__init__()
        self._app = app
        self._checks = {}
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(8, 8, 8, 8)
        root.setSpacing(6)

        info = QLabel(
            "Check snaps to keep them <b>enabled</b>. "
            "Uncheck to <b>block</b> selected snap types."
        )
        info.setWordWrap(True)
        root.addWidget(info)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        form = QVBoxLayout(inner)
        form.setContentsMargins(0, 0, 0, 0)
        form.setSpacing(2)

        disabled = _disabled_set(self._app)
        for kind, label, desc in SNAP_KINDS:
            cb = QCheckBox(label)
            cb.setChecked(kind not in disabled)
            cb.setToolTip(f"{desc}\n(kind: {kind})")
            cb.stateChanged.connect(self._on_changed)
            form.addWidget(cb)
            self._checks[kind] = cb

        form.addStretch(1)
        scroll.setWidget(inner)
        root.addWidget(scroll, 1)

        btns = QHBoxLayout()
        all_btn = QPushButton("Enable all")
        none_btn = QPushButton("Block all")
        all_btn.clicked.connect(lambda: self._set_all(True))
        none_btn.clicked.connect(lambda: self._set_all(False))
        btns.addWidget(all_btn)
        btns.addWidget(none_btn)
        root.addLayout(btns)

        self._status = QLabel("")
        self._status.setWordWrap(True)
        root.addWidget(self._status)
        self._update_status()

    def _update_status(self):
        try:
            disabled = _disabled_set(self._app)
            self._status.setText(f"Blocked: {len(disabled)} type(s)")
        except Exception:
            pass

    def _set_all(self, enabled: bool):
        for cb in self._checks.values():
            cb.blockSignals(True)
            cb.setChecked(enabled)
            cb.blockSignals(False)
        self._apply()

    def _on_changed(self, _state):
        self._apply()

    def _apply(self):
        disabled = {k for k, cb in self._checks.items() if not cb.isChecked()}
        try:
            _set_disabled(self._app, disabled)
            self._status.setText(f"Blocked: {len(disabled)} type(s)")
        except Exception:
            log.exception("Failed to save snap settings")
            self._status.setText("Error saving settings (see log).")

    def refresh(self):
        try:
            disabled = _disabled_set(self._app)
        except Exception:
            return
        for kind, cb in self._checks.items():
            want = kind not in disabled
            if cb.isChecked() != want:
                cb.blockSignals(True)
                cb.setChecked(want)
                cb.blockSignals(False)
        self._status.setText(f"Blocked: {len(disabled)} type(s)")


def _filter_snap(snap, disabled, viewport=None, px=None, py=None):
    try:
        if snap is None:
            return None
        kind = _normalize_kind(getattr(snap, "kind", None))
        if kind in (None, "none"):
            return snap
        if kind in disabled:
            # Replace with the raw (unsnapped) point so the cursor does not lock.
            raw = None
            if viewport is not None and px is not None and py is not None:
                raw = _raw_world_point(viewport, px, py)
            point = raw if raw is not None else snap.point
            return SnapResult(point, "none", COLOR_NONE)
        return snap
    except Exception:
        log.exception("Error while filtering snap")
        return snap


def setup(app):
    panel_widget = SnapTogglePanel(app)
    dock = app.add_panel("Snaps", panel_widget, name="snap_toggle")

    try:
        app.on_document_changed(panel_widget.refresh)
    except Exception:
        log.exception("Could not connect on_document_changed")

    # Provider (applies across tabs/projects)
    def provider(viewport, snap, px, py):
        try:
            return _filter_snap(snap, _disabled_set(app), viewport, px, py)
        except Exception:
            log.exception("Snap provider error")
            return None

    try:
        app.add_snap_provider(provider)
    except Exception:
        log.exception("Could not register snap provider")

    # Fallback: wrap snap on the current viewport's inference engine
    try:
        vp = app.viewport
        inf = getattr(vp, "inference", None)
        if inf is not None and hasattr(inf, "snap"):
            orig = inf.snap
            owner_vp = getattr(inf, "viewport", vp)

            def wrapped_snap(px_x, px_y, modifiers, _orig=orig, _vp=owner_vp):
                res = _orig(px_x, px_y, modifiers)
                return _filter_snap(res, _disabled_set(app), _vp, px_x, px_y)

            inf.snap = wrapped_snap  # type: ignore[assignment]
    except Exception:
        log.exception("Could not apply viewport fallback")

    def show():
        try:
            app.show_panel(dock)
        except Exception:
            try:
                dock.show()
                dock.raise_()
            except Exception:
                log.exception("Could not show Snaps panel")

    try:
        app.add_menu_action(
            "Snaps…",
            show,
            tip="Block or unblock selected snap/inference types.",
        )
    except Exception:
        log.exception("Could not add menu action")

    log.info("Snap Toggle extension loaded (key=%s)", getattr(app, "key", "?"))
