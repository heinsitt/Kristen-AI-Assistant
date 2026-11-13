#!/usr/bin/env python3
"""Generate Kristen's HUD assets: banner + section rule, dark and light.

Design language: arc-reactor interface. Cyan holographic linework, blueprint grid,
rotating tick rings around a glowing core, corner brackets, telemetry meters and a
slow scanline. Pure SVG + SMIL so the motion plays inside a GitHub README <img>.

Run inside assets/:  python3 gen_kristen_assets.py
"""

W, H = 1000, 300
SANS = "-apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "dark": dict(
        bg=[("#02060D", 0), ("#04101A", 55), ("#010409", 100)],
        grid="#0E3446", grid_op=0.55,
        accent="#45E0FF", accent_dim="#0E6D86",
        amber="#FFB74D",
        ink="#EAFBFF", muted="#7FA6B5",
        core_in="#FFFFFF", core_mid="#8FF2FF",
        panel_fill="#06202C", panel_op=0.55,
        scan="#8DEBFF", scan_op=0.07,
        border="rgba(69,224,255,0.22)",
        frame="rgba(255,255,255,0.08)",
        glow_op=0.5,
    ),
    "light": dict(
        bg=[("#F6FBFE", 0), ("#E6F1F8", 55), ("#FCFEFF", 100)],
        grid="#A7C6D7", grid_op=0.55,
        accent="#0A6E88", accent_dim="#8FC0CF",
        amber="#B45309",
        ink="#06121B", muted="#4C6675",
        core_in="#FFFFFF", core_mid="#22D3EE",
        panel_fill="#FFFFFF", panel_op=0.55,
        scan="#0A6E88", scan_op=0.05,
        border="rgba(10,110,136,0.28)",
        frame="rgba(6,18,27,0.10)",
        glow_op=0.28,
    ),
}


def defs(t):
    bg = "".join(f'\n      <stop offset="{p}%" stop-color="{c}"/>' for c, p in t["bg"])
    return f'''  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0.6" y2="1">{bg}
    </linearGradient>

    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0 H0 V40" fill="none" stroke="{t["grid"]}" stroke-opacity="{t["grid_op"]}" stroke-width="0.6"/>
    </pattern>

    <radialGradient id="core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{t["core_in"]}" stop-opacity="1"/>
      <stop offset="34%" stop-color="{t["core_mid"]}" stop-opacity="0.95"/>
      <stop offset="68%" stop-color="{t["accent"]}" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="{t["accent"]}" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="coreHalo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{t["accent"]}" stop-opacity="{t["glow_op"]}"/>
      <stop offset="55%" stop-color="{t["accent"]}" stop-opacity="{round(t["glow_op"]*0.28, 3)}"/>
      <stop offset="100%" stop-color="{t["accent"]}" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t["accent_dim"]}"/>
      <stop offset="65%" stop-color="{t["accent"]}"/>
      <stop offset="100%" stop-color="{t["core_in"]}" stop-opacity="0.9"/>
    </linearGradient>

    <linearGradient id="hudrule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t["accent"]}" stop-opacity="0.9"/>
      <stop offset="55%" stop-color="{t["accent"]}" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="{t["accent"]}" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{t["scan"]}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{t["scan"]}" stop-opacity="{t["scan_op"]}"/>
      <stop offset="100%" stop-color="{t["scan"]}" stop-opacity="0"/>
    </linearGradient>

    <radialGradient id="vig" cx="50%" cy="50%" r="70%">
      <stop offset="45%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="{0.55 if t["core_in"] == "#FFFFFF" and t["ink"] == "#EAFBFF" else 0.10}"/>
    </radialGradient>

    <clipPath id="frame"><rect x="0" y="0" width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>'''


def reactor(t):
    a, amber = t["accent"], t["amber"]
    return f'''  <g transform="translate(170 150)">
    <circle r="132" fill="url(#coreHalo)"/>

    <circle r="100" fill="none" stroke="{a}" stroke-opacity="0.18" stroke-width="1"/>
    <circle r="88" fill="none" stroke="{a}" stroke-opacity="0.42" stroke-width="10" stroke-dasharray="1.2 6.6"/>
    <circle r="104" fill="none" stroke="{a}" stroke-opacity="0.28" stroke-width="1.6" stroke-dasharray="26 14">
      <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="64s" repeatCount="indefinite"/>
    </circle>

    <g>
      <circle r="79" fill="none" stroke="{a}" stroke-opacity="0.85" stroke-width="2.4" stroke-dasharray="48 12 6 12"/>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="26s" repeatCount="indefinite"/>
    </g>
    <g>
      <circle r="67" fill="none" stroke="{a}" stroke-opacity="0.5" stroke-width="1.4" stroke-dasharray="16 7"/>
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="17s" repeatCount="indefinite"/>
    </g>
    <g>
      <circle r="56" fill="none" stroke="{amber}" stroke-opacity="0.55" stroke-width="3.2"
              stroke-dasharray="9 27" stroke-linecap="round">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="42s" repeatCount="indefinite"/>
      </circle>
    </g>

    <circle r="45" fill="url(#core)"/>
    <circle r="45" fill="none" stroke="{t["core_in"]}" stroke-opacity="0.55" stroke-width="1.2">
      <animate attributeName="stroke-opacity" values="0.55;0.15;0.55" dur="3.4s" repeatCount="indefinite"/>
    </circle>
    <circle r="27" fill="none" stroke="{t["core_in"]}" stroke-opacity="0.75" stroke-width="1">
      <animate attributeName="stroke-opacity" values="0.75;0.3;0.75" dur="2.6s" repeatCount="indefinite"/>
    </circle>
    <circle r="12" fill="{t["core_in"]}" opacity="0.9">
      <animate attributeName="opacity" values="0.9;0.55;0.9" dur="4.2s" repeatCount="indefinite"/>
    </circle>

    <g stroke="{a}" stroke-opacity="0.6" stroke-width="1.2">
      <path d="M0,-112 V-104"/><path d="M0,112 V104"/>
      <path d="M-112,0 H-104"/><path d="M112,0 H104"/>
    </g>
  </g>'''


def telemetry(t):
    a, amber, muted = t["accent"], t["amber"], t["muted"]
    rows = [("CORE", 122, 96, 5.5, 0), ("REASONING", 148, 108, 7.5, -1.4), ("TOOLING", 174, 92, 6.2, -3.1), ("MEMORY", 200, 118, 8.4, -2.2)]
    parts = [f'''  <g>
    <rect x="694" y="66" width="252" height="152" rx="4" fill="{t["panel_fill"]}" opacity="{t["panel_op"]}"/>
    <path d="M694 80 H694 V66 H708" fill="none" stroke="{a}" stroke-opacity="0.55" stroke-width="1.6"/>
    <path d="M932 66 H946 V80" fill="none" stroke="{a}" stroke-opacity="0.55" stroke-width="1.6"/>
    <path d="M694 204 V218 H708" fill="none" stroke="{a}" stroke-opacity="0.55" stroke-width="1.6"/>
    <path d="M932 218 H946 V204" fill="none" stroke="{a}" stroke-opacity="0.55" stroke-width="1.6"/>
    <text x="712" y="88" font-family="{MONO}" font-size="9" letter-spacing="2.6" fill="{muted}">TELEMETRY</text>
    <circle cx="926" cy="85" r="2.6" fill="{amber}">
      <animate attributeName="opacity" values="1;0.15;1" dur="1.9s" repeatCount="indefinite"/>
    </circle>''']

    for label, y, width, dur, begin in rows:
        parts.append(f'''    <text x="712" y="{y}" font-family="{MONO}" font-size="9" letter-spacing="1.8" fill="{muted}">{label}</text>
    <rect x="796" y="{y-8}" width="132" height="5" rx="2.5" fill="{a}" opacity="0.14"/>
    <rect x="796" y="{y-8}" width="{width}" height="5" rx="2.5" fill="url(#bar)">
      <animate attributeName="width" values="{width};{width+24};{width}" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>
    </rect>''')

    parts.append(f'''    <text x="712" y="240" font-family="{MONO}" font-size="8.4" letter-spacing="1.9" fill="{muted}" opacity="0.85">BASE44 NODE · READY</text>
  </g>
  <text x="34" y="40" font-family="{MONO}" font-size="9" letter-spacing="2.4" fill="{muted}">AI SUPERAGENT // INTERFACE</text>''')
    return "\n".join(parts)


def brackets(t):
    a = t["accent"]
    c = []
    for x, y, sx, sy in [(18, 18, 1, 1), (982, 18, -1, 1), (18, 282, 1, -1), (982, 282, -1, -1)]:
        c.append(f'<path d="M{x} {y + 22*sy} V{y} H{x + 22*sx}" fill="none" stroke="{a}" stroke-opacity="0.4" stroke-width="1.4"/>')
    return '  <g>\n    ' + '\n    '.join(c) + '\n  </g>'


def build_banner(t):
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ttl dsc">')
    o.append('  <title id="ttl">Kristen — personal AI Superagent</title>')
    o.append('  <desc id="dsc">HUD style banner: an arc reactor ring system beside the name Kristen, with telemetry meters, corner brackets and a slow scanline. Personal AI Superagent running on Base44.</desc>')
    o.append(defs(t))
    o.append('')
    o.append('  <g clip-path="url(#frame)">')
    o.append(f'    <rect width="{W}" height="{H}" fill="url(#bg)"/>')
    o.append(f'    <rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.75"/>')
    o.append('    <rect width="1000" height="300" fill="url(#vig)"/>')

    o.append(reactor(t))

    # link line from reactor to the name
    o.append(f'''    <g stroke="{t["accent"]}" stroke-opacity="0.5" stroke-width="1">
      <path d="M300 150 H326"/>
      <path d="M326 150 v-6" stroke-opacity="0.6"/>
    </g>
    <circle cx="300" cy="150" r="3" fill="{t["accent"]}" opacity="0.9">
      <animate attributeName="opacity" values="0.9;0.2;0.9" dur="2.8s" repeatCount="indefinite"/>
    </circle>''')

    # type block, left aligned
    o.append(f'''
    <text x="344" y="104" font-family="{MONO}" font-size="10.5" letter-spacing="3.2" fill="{t["accent"]}">PERSONAL AI AGENT · SYSTEM ONLINE</text>

    <text x="340" y="164" font-family="{SANS}" font-size="52" font-weight="700" letter-spacing="7" fill="{t["ink"]}">KRISTEN</text>

    <g>
      <path d="M344 182 H596" stroke="url(#hudrule)" stroke-width="1.6"/>
      <g stroke="{t["accent"]}" stroke-opacity="0.45" stroke-width="1">
        <path d="M360 178 v8"/><path d="M392 180 v4"/><path d="M424 178 v8"/>
        <path d="M456 180 v4"/><path d="M488 178 v8"/><path d="M520 180 v4"/>
      </g>
      <circle cx="344" cy="182" r="4" fill="none" stroke="{t["amber"]}" stroke-opacity="0.9" stroke-width="1.6">
        <animate attributeName="stroke-opacity" values="0.9;0.25;0.9" dur="3.6s" repeatCount="indefinite"/>
      </circle>
    </g>

    <text x="344" y="212" font-family="{SANS}" font-size="14.5" font-weight="400" fill="{t["muted"]}">Research · Planning · Writing · Execution</text>

    <text x="344" y="240" font-family="{MONO}" font-size="9.6" letter-spacing="1.9" fill="{t["muted"]}" opacity="0.9">LINK BASE44 · MODE ASSIST · SESSION ACTIVE</text>''')

    o.append(telemetry(t))
    o.append(brackets(t))

    # scanline
    o.append(f'''    <rect x="0" y="-140" width="1000" height="140" fill="url(#scan)">
      <animate attributeName="y" values="-140;300" dur="9s" repeatCount="indefinite"/>
    </rect>''')

    o.append('  </g>')
    o.append(f'  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{t["frame"]}"/>')
    o.append('</svg>')
    return "\n".join(o) + "\n"


def build_rule(t):
    a, amber = t["accent"], t["amber"]
    ticks = "".join(f'<path d="M{x} 11 v{6 if i % 4 == 0 else 3}"/>' for i, x in enumerate(range(0, 1001, 25)))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="24" viewBox="0 0 1000 24" role="img" aria-label="Section divider">
  <defs>
    <linearGradient id="hudline" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{a}" stop-opacity="0"/>
      <stop offset="18%" stop-color="{a}" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="{a}" stop-opacity="0.75"/>
      <stop offset="82%" stop-color="{a}" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="{a}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <path d="M0 12 H1000" stroke="url(#hudline)" stroke-width="1.2"/>
  <g stroke="{a}" stroke-opacity="0.32" stroke-width="1">{ticks}</g>
  <g transform="translate(500 12)">
    <circle r="9" fill="none" stroke="{a}" stroke-opacity="0.55" stroke-width="1.2" stroke-dasharray="3 3">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="18s" repeatCount="indefinite"/>
    </circle>
    <rect x="-3.2" y="-3.2" width="6.4" height="6.4" fill="{amber}" opacity="0.95">
      <animate attributeName="opacity" values="0.95;0.35;0.95" dur="3.2s" repeatCount="indefinite"/>
    </rect>
  </g>
  <g stroke="{a}" stroke-opacity="0.6" stroke-width="1.4" fill="none">
    <path d="M4 6 V18"/><path d="M996 6 V18"/>
  </g>
</svg>
'''


def main():
    for theme, t in THEMES.items():
        with open(f"banner-{theme}.svg", "w", encoding="utf-8") as f:
            f.write(build_banner(t))
        with open(f"rule-{theme}.svg", "w", encoding="utf-8") as f:
            f.write(build_rule(t))
        print(f"wrote banner-{theme}.svg + rule-{theme}.svg")


if __name__ == "__main__":
    main()
