import os

labels_light = """<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="10" font-weight="600" fill="#57606a">
  <text x="-36" y="27">Mon</text>
  <text x="-36" y="59">Wed</text>
  <text x="-36" y="91">Fri</text>
  <text x="2" y="-12">Nov 2025</text>
  <text x="66" y="-12">Dec</text>
  <text x="130" y="-12">Jan 2026</text>
  <text x="210" y="-12">Feb</text>
  <text x="274" y="-12">Mar</text>
  <text x="338" y="-12">Apr</text>
  <text x="418" y="-12">May</text>
  <text x="482" y="-12">Jun</text>
  <text x="562" y="-12">Jul</text>
  <text x="626" y="-12">Aug</text>
  <text x="690" y="-12">Sep</text>
  <text x="770" y="-12">Oct</text>
  <text x="826" y="-12">Nov</text>
</g>"""

labels_dark = labels_light.replace("#57606a", "#c9d1d9")

files = [
    ("dist/github-contribution-grid-snake.svg", labels_light),
    ("dist/github-contribution-grid-snake-dark.svg", labels_dark)
]

for rel_path, labels in files:
    if not os.path.exists(rel_path):
        print(f"Skipping {rel_path}: file does not exist")
        continue
    with open(rel_path, "r", encoding="utf-8") as f:
        c = f.read()
    
    # Expand viewBox to leave margin on left for Mon, Wed, Fri
    c = c.replace('viewBox="-16 -32 880 192" width="880" height="192"', 'viewBox="-42 -32 910 192" width="910" height="192"')
    
    # If labels already exist, do not duplicate
    if '<text x="-36" y="27">Mon</text>' not in c:
        idx = c.rfind("</svg>")
        if idx != -1:
            c = c[:idx] + labels + "</svg>"
            with open(rel_path, "w", encoding="utf-8") as f:
                f.write(c)
            print("Successfully injected labels into:", rel_path)
