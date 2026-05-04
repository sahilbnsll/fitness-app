import re

with open("fitness_hub_v3.html", "r") as f:
    html = f.read()

# Add CSS for bottom nav
css_nav = """    .bottom-nav {
      position: fixed;
      bottom: 0; left: 0; right: 0;
      background: rgba(10, 10, 10, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-top: 1px solid var(--b2);
      display: flex;
      justify-content: space-around;
      padding: 10px 10px calc(10px + env(safe-area-inset-bottom, 20px));
      z-index: 1000;
    }
    .bn {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      color: var(--t3);
      background: none;
      border: none;
      font-size: 10px;
      font-weight: 500;
      transition: color 0.2s;
      flex: 1;
      padding: 4px 0;
    }
    .bn.on { color: var(--t1); }
    .bn-icon {
      font-size: 22px;
      margin-bottom: 2px;
      filter: grayscale(100%) opacity(0.5);
      transition: all 0.2s;
    }
    .bn.on .bn-icon {
      filter: grayscale(0%) opacity(1);
    }
"""

if ".bottom-nav {" not in html:
    html = html.replace('</style>', css_nav + '\n  </style>')

# Ensure .app has padding-bottom
if "padding-bottom: 90px" not in html:
    html = html.replace('.app {', '.app {\n      padding-bottom: 90px;')

# Replace old nav HTML with bottom-nav
old_nav_regex = r'<!-- NAV -->\s*<div class="nav-wrap">.*?</div>\s*</div>'

new_nav = """<!-- MORE VIEW (Created for extra tabs) -->
    <div id="more" class="view">
      <p class="slbl">More</p>
      <div class="card" style="margin-bottom:12px" onclick="nav('cardio', document.getElementById('bn-more'))">
        <div style="font-weight:600;font-size:15px;color:var(--t1)">🏃‍♂️ Cardio</div>
      </div>
      <div class="card" style="margin-bottom:12px" onclick="nav('deload', document.getElementById('bn-more'))">
        <div style="font-weight:600;font-size:15px;color:var(--t1)">🧘 Deload Protocol</div>
      </div>
    </div>

    <!-- BOTTOM NAV -->
    <div class="bottom-nav">
      <button class="bn on" onclick="nav('workouts',this)" id="bn-workouts">
        <div class="bn-icon">🏋️</div>
        <div>Workout</div>
      </button>
      <button class="bn" onclick="nav('diet',this)">
        <div class="bn-icon">🥩</div>
        <div>Diet</div>
      </button>
      <button class="bn" onclick="nav('supps',this)">
        <div class="bn-icon">💊</div>
        <div>Supps</div>
      </button>
      <button class="bn" onclick="nav('tracking',this)">
        <div class="bn-icon">📈</div>
        <div>Track</div>
      </button>
      <button class="bn" onclick="nav('more',this)" id="bn-more">
        <div class="bn-icon">⋯</div>
        <div>More</div>
      </button>
    </div>"""

html = re.sub(old_nav_regex, '', html, flags=re.DOTALL)

# Insert bottom nav at the end of .app
html = re.sub(r'(</div>\s*<!-- ── MODALS ── -->)', new_nav + r'\n\n\1', html)

# If modals comment doesn't exist, try before <script>
if "BOTTOM NAV" not in html:
    html = html.replace('  <script>', '  </div>\n\n' + new_nav + '\n\n  <script>')
    html = html.replace('<body>\n  <div class="app">', '<body>\n  <div class="app" style="padding-bottom:100px;">') # Fallback padding

with open("fitness_hub_v3.html", "w") as f:
    f.write(html)
print("Updated nav successfully")
