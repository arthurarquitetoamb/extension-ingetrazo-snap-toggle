<img width="960" height="540" alt="snap-toggle-illustration" src="https://github.com/user-attachments/assets/e405d4c4-ea25-443a-adaf-84dfaae60078" /># Snap Toggle for IngeTrazo

A Python extension for [IngeTrazo](https://ingetrazo.com/) that lets you **block and unblock selected snap/inference types** while modeling.

![Uploading snap-toggle-illustration.<svg xmlns="http://www.w3.org/2000/svg" width="960" height="540" viewBox="0 0 960 540">
  <defs>
    <style>
      .bg { fill: #f4f6f8; }
      .app { fill: #e9edf2; stroke: #c9d2dc; }
      .viewport { fill: #ffffff; stroke: #cfd8e3; }
      .panel { fill: #ffffff; stroke: #cfd8e3; }
      .header { fill: #2f3b52; }
      .header-text { fill: #ffffff; font: 600 18px Arial, sans-serif; }
      .title { fill: #1f2937; font: 700 26px Arial, sans-serif; }
      .sub { fill: #4b5563; font: 14px Arial, sans-serif; }
      .label { fill: #1f2937; font: 14px Arial, sans-serif; }
      .muted { fill: #6b7280; font: 13px Arial, sans-serif; }
      .box { fill: #ffffff; stroke: #94a3b8; }
      .check { stroke: #16a34a; stroke-width: 3; fill: none; stroke-linecap: round; stroke-linejoin: round; }
      .blocked { fill: #fef2f2; stroke: #ef4444; }
      .x { stroke: #dc2626; stroke-width: 2.5; stroke-linecap: round; }
      .btn { fill: #eef2ff; stroke: #94a3b8; }
      .btn2 { fill: #fff7ed; stroke: #94a3b8; }
      .btn-text { fill: #1f2937; font: 13px Arial, sans-serif; }
      .edge { stroke: #64748b; stroke-width: 3; }
      .snap-on { fill: #16a34a; stroke: #166534; stroke-width: 2; }
      .snap-off { fill: none; stroke: #dc2626; stroke-width: 2; stroke-dasharray: 4 3; }
      .cursor { stroke: #2563eb; stroke-width: 2; }
      .legend { fill: #ffffff; stroke: #d1d5db; }
      .pill-on { fill: #dcfce7; stroke: #86efac; }
      .pill-off { fill: #fee2e2; stroke: #fca5a5; }
      .pill-text-on { fill: #166534; font: 600 12px Arial, sans-serif; }
      .pill-text-off { fill: #991b1b; font: 600 12px Arial, sans-serif; }
    </style>
  </defs>

  <rect class="bg" x="0" y="0" width="960" height="540"/>

  <text class="title" x="40" y="48">Snap Toggle for IngeTrazo</text>
  <text class="sub" x="40" y="72">Block or unblock selected snap/inference types while keeping others enabled</text>

  <!-- App window -->
  <rect class="app" x="40" y="95" width="880" height="410" rx="12"/>
  <rect class="header" x="40" y="95" width="880" height="36" rx="12"/>
  <rect class="header" x="40" y="119" width="880" height="12"/>
  <text class="header-text" x="58" y="119">IngeTrazo — Extensions ▸ Snaps…</text>

  <!-- Viewport -->
  <rect class="viewport" x="60" y="150" width="520" height="335" rx="8"/>
  <text class="muted" x="78" y="175">Model viewport</text>

  <!-- Geometry -->
  <line class="edge" x1="130" y1="420" x2="430" y2="420"/>
  <line class="edge" x1="130" y1="420" x2="130" y2="240"/>
  <line class="edge" x1="130" y1="240" x2="430" y2="240"/>
  <line class="edge" x1="430" y1="240" x2="430" y2="420"/>
  <line class="edge" x1="130" y1="240" x2="430" y2="420"/>

  <!-- Enabled snap marker (Endpoint) -->
  <circle class="snap-on" cx="430" cy="240" r="8"/>
  <rect class="pill-on" x="446" y="214" width="70" height="22" rx="11"/>
  <text class="pill-text-on" x="481" y="229" text-anchor="middle">Endpoint</text>
  <text class="muted" x="446" y="252">Enabled: cursor locks</text>

  <!-- Blocked snap marker area (Midpoint) -->
  <circle class="snap-off" cx="280" cy="420" r="9"/>
  <line class="x" x1="273" y1="413" x2="287" y2="427"/>
  <line class="x" x1="287" y1="413" x2="273" y2="427"/>
  <rect class="pill-off" x="296" y="394" width="70" height="22" rx="11"/>
  <text class="pill-text-off" x="331" y="409" text-anchor="middle">Midpoint</text>
  <text class="muted" x="296" y="432">Blocked: no lock, raw cursor point</text>

  <!-- Cursor -->
  <line class="cursor" x1="266" y1="420" x2="294" y2="420"/>
  <line class="cursor" x1="280" y1="406" x2="280" y2="434"/>

  <!-- Side panel -->
  <rect class="panel" x="600" y="150" width="300" height="335" rx="8"/>
  <text class="label" x="622" y="178" style="font-weight:700;font-size:16px;">Snaps</text>
  <text class="muted" x="622" y="198">Check to enable, uncheck to block</text>

  <!-- Rows -->
  <!-- Endpoint (enabled) -->
  <rect class="box" x="622" y="220" width="18" height="18" rx="3"/>
  <polyline class="check" points="626,229 630,233 636,225"/>
  <text class="label" x="648" y="234">Endpoint</text>

  <!-- Midpoint (blocked) -->
  <rect class="blocked" x="622" y="250" width="18" height="18" rx="3"/>
  <text class="label" x="648" y="264">Midpoint</text>

  <!-- Center (enabled) -->
  <rect class="box" x="622" y="280" width="18" height="18" rx="3"/>
  <polyline class="check" points="626,289 630,293 636,285"/>
  <text class="label" x="648" y="294">Center</text>

  <!-- Intersection (blocked) -->
  <rect class="blocked" x="622" y="310" width="18" height="18" rx="3"/>
  <text class="label" x="648" y="324">Intersection</text>

  <!-- On edge (blocked) -->
  <rect class="blocked" x="622" y="340" width="18" height="18" rx="3"/>
  <text class="label" x="648" y="354">On edge</text>

  <!-- On face (enabled) -->
  <rect class="box" x="622" y="370" width="18" height="18" rx="3"/>
  <polyline class="check" points="626,379 630,383 636,375"/>
  <text class="label" x="648" y="384">On face</text>

  <!-- Extension (enabled) -->
  <rect class="box" x="622" y="400" width="18" height="18" rx="3"/>
  <polyline class="check" points="626,409 630,413 636,405"/>
  <text class="label" x="648" y="414">Extension</text>

  <!-- Buttons -->
  <rect class="btn" x="622" y="432" width="120" height="30" rx="6"/>
  <text class="btn-text" x="682" y="452" text-anchor="middle">Enable all</text>
  <rect class="btn2" x="752" y="432" width="120" height="30" rx="6"/>
  <text class="btn-text" x="812" y="452" text-anchor="middle">Block all</text>

  <text class="muted" x="622" y="478">Status: Blocked: 3 type(s)</text>

  <!-- Legend -->
  <rect class="legend" x="60" y="455" width="520" height="20" rx="4" fill-opacity="0.0" stroke-opacity="0.0"/>
  <circle class="snap-on" cx="75" cy="465" r="6"/>
  <text class="muted" x="90" y="469">Enabled snap type (locks when detected)</text>
  <circle class="snap-off" cx="360" cy="465" r="6"/>
  <line class="x" x1="355" y1="460" x2="365" y2="470"/>
  <line class="x" x1="365" y1="460" x2="355" y2="470"/>
  <text class="muted" x="375" y="469">Blocked snap type (suppressed)</text>
</svg>
svg…]()


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
