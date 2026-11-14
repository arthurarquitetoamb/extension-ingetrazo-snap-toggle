# Snap Toggle for IngeTrazo

A Python extension for [IngeTrazo](https://ingetrazo.com/) that lets you **block and unblock selected snap/inference types** while modeling.

![Snap Toggle for IngeTrazo - panel and viewport illustration](snap-toggle-illustration.svg)

It adds a **Snaps** panel and menu action so you can quickly disable specific snaps (for example, `On edge`, `Midpoint`, or `Intersection`) without changing your entire workflow.

## Features

- Enable/disable individual snap and inference types via checkboxes
- **Enable all** / **Block all** quick actions
- Truly blocks snapping (replaces the snapped result with the raw cursor point), not just the visual marker
- Per-document settings stored in IngeTrazo document data (`plugin_data`), with undo/redo support
- Works as an IngeTrazo extension using the Extension API (`setup(app)`)

## Supported snap types

The panel can toggle the following snap/inference kinds (when available):

- Endpoint
- Midpoint
- Arc midpoint
- Center
- Origin
- Component origin
- Intersection
- Intersection (edge lock)
- Intersection (face lock)
- On edge
- On face
- Close
- Extension
- From point
- Aligned
- Axis lock
- Axis inference
- Reference (parallel/perpendicular)
- Perpendicular to face
- On guide line
- On model axis
- Through point

> Note: IngeTrazo may emit additional or context-specific snap kinds depending on version/tool/context. If a specific snap is not blocked, open an issue with the snap name shown in the UI/status tip.

## Requirements

- IngeTrazo with Python extension support (Extension API with `setup(app)`)
- The extension uses IngeTrazo's runtime modules/APIs (e.g. `core.snap`, `PySide6`) and is intended to run inside IngeTrazo

## Installation

1. Download or copy `snap_toggle.py` from this repository.
2. Place it in your IngeTrazo **user plugins** folder:

   - **Windows:** `%APPDATA%\ingetrazo\plugins\`
   - **Linux:** `$XDG_DATA_HOME/ingetrazo/plugins` (usually `~/.local/share/ingetrazo/plugins`)
   - **macOS:** check IngeTrazo's user plugins directory for your installation (same Extension API location conventions as the app)

3. Restart IngeTrazo (plugins are discovered at startup).

### Why not install in `Program Files` / app internals?

Installing in application/internal folders (for example, under `Program Files` or packaged `_internal` directories) is not recommended because:
- the scanned plugin paths may differ from internal packaging layout,
- those locations often require administrator permissions,
- app updates/reinstalls may overwrite or remove custom files.

Use the user plugins folder for third-party extensions.

## Usage

1. Start IngeTrazo and open a model.
2. Open **Extensions ▸ Snaps…** (or the **Snaps** panel in the side tray).
3. Use the checkboxes to choose which snap types remain enabled:
   - Checked = enabled
   - Unchecked = blocked
4. Use **Enable all** or **Block all** for quick toggling.
5. Test with a drawing/editing tool (e.g. **Line**) over existing geometry.

### Behavior notes

- Settings are saved **per document** (in the document's plugin data), so different documents can have different snap configurations.
- Because settings are stored as document changes, toggling them creates undo/redo steps.
- When a blocked snap is encountered, the extension replaces it with a raw (unsnapped) world point, so the cursor does not lock to that snap type.

## How it works

The extension:
- registers a snap provider via `app.add_snap_provider(...)` to filter snap results across viewports/tabs, and
- applies a fallback wrapper on the current viewport's inference snap method (for compatibility).

If the current snap `kind` is in the blocked set, it returns a `SnapResult` with:
- kind: `"none"`
- point: raw world point under the cursor (from `_world_from_pixel`, when available)

## Limitations

- **No automatic "next best" snap recomputation:** the provider receives the engine's final snap result. Blocking a kind suppresses that result, but does not re-run the snap engine to select the next candidate of a different kind.
- Some snap kinds/names may vary by IngeTrazo version or context; the extension includes a common set and a few aliases, but may need updates for new/renamed kinds.
- Inference/axis behavior can also be affected by IngeTrazo's own inference modes and tool behavior.

## Troubleshooting

- **Menu/panel does not appear:** make sure `snap_toggle.py` is in the correct user plugins folder and restart IngeTrazo.
- **Snaps still lock after blocking:** ensure you restarted after installing the latest version of this extension (older versions hid markers but could keep the snapped point).
- **Settings seem to "reset":** remember settings are per document; check the configuration in the current document.

## Development

This is a single-file extension (`snap_toggle.py`) intended to be dropped into IngeTrazo's plugins directory.

Suggested improvements:
- auto-detect and list observed snap kinds dynamically
- optional global (app-level) preferences in addition to per-document settings
- fallback recomputation strategy for next-best snap candidates (if supported by API)

## License

Add your preferred license for this repository (for example, MIT or GPL-3.0-or-later), and include a `LICENSE` file.
