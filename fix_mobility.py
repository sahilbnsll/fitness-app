import re

with open("fitness_hub_v3.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add Mobility to More view
if "nav('mobility'" not in html:
    more_btn = """      <div class="card" style="margin-bottom:12px" onclick="nav('mobility', document.getElementById('bn-more'))">
        <div style="font-weight:600;font-size:15px;color:var(--t1)">🧘‍♂️ Mobility & Stretching</div>
      </div>"""
    html = html.replace('<div id="more" class="view">', '<div id="more" class="view">\n' + more_btn)

mobility_html = """    <!-- MOBILITY VIEW -->
    <div id="mobility" class="view">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
        <p class="slbl" style="margin:0">Routines</p>
        <button class="btn" style="background:var(--card2);padding:6px 12px;font-size:12px" onclick="document.getElementById('mobModal').style.display='flex'">+ Add</button>
      </div>
      <div id="mobilityList"></div>
    </div>"""

mob_modal = """
  <!-- MOBILITY MODAL -->
  <div id="mobModal" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.8);z-index:999;align-items:center;justify-content:center;padding:16px;backdrop-filter:blur(8px)">
    <div class="card" style="width:100%;max-width:400px">
      <div style="font-size:16px;font-weight:600;margin-bottom:16px">Add Mobility Routine</div>
      <input type="text" id="mobNameInput" class="input" placeholder="Routine Name (e.g. Morning Flow)" style="margin-bottom:12px">
      <input type="text" id="mobNoteInput" class="input" placeholder="Notes/Duration" style="margin-bottom:16px">
      <div style="display:flex;gap:8px">
        <button class="btn" style="flex:1;background:var(--card2)" onclick="document.getElementById('mobModal').style.display='none'">Cancel</button>
        <button class="btn" style="flex:1" onclick="addMob()">Save</button>
      </div>
    </div>
  </div>
"""

js_logic = """    // ── MOBILITY ──
    let mobilityRoutines = JSON.parse(localStorage.getItem('ft_mobility_v1')) || [
      { id: Date.now()+'_1', name: 'Pre-workout Dynamic', note: '5 mins. Leg swings, arm circles.', checked: false, lastDate: '' },
      { id: Date.now()+'_2', name: 'Post-workout Static', note: '10 mins. Hamstring, chest, hips.', checked: false, lastDate: '' }
    ];
    
    function saveMobility() {
      localStorage.setItem('ft_mobility_v1', JSON.stringify(mobilityRoutines));
    }
    
    function renderMobility() {
      const list = document.getElementById('mobilityList');
      if (!list) return;
      const today = new Date().toDateString();
      
      list.innerHTML = mobilityRoutines.map(m => {
        if (m.lastDate !== today) { m.checked = false; }
        return `
        <div class="card" style="margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-weight:600; font-size:15px; color: ${m.checked ? 'var(--t3)' : 'var(--t1)'}; text-decoration: ${m.checked ? 'line-through' : 'none'}">${m.name}</div>
            <div style="font-size:12px; color:var(--t2)">${m.note}</div>
          </div>
          <div style="display:flex; gap:12px; align-items:center;">
            <div onclick="toggleMob('${m.id}')" style="width:24px; height:24px; border-radius:50%; border:2px solid ${m.checked ? 'var(--grn)' : 'var(--b2)'}; background: ${m.checked ? 'var(--grn)' : 'transparent'}; display:flex; align-items:center; justify-content:center; cursor:pointer;">
              ${m.checked ? '<span style="color:#000; font-size:12px; font-weight:bold">✓</span>' : ''}
            </div>
            <button onclick="delMob('${m.id}')" style="background:none; border:none; color:var(--red); font-size:16px; cursor:pointer">×</button>
          </div>
        </div>
        `;
      }).join('');
      saveMobility();
    }
    
    function toggleMob(id) {
      const m = mobilityRoutines.find(x => x.id === id);
      if (m) {
        m.checked = !m.checked;
        m.lastDate = m.checked ? new Date().toDateString() : '';
        renderMobility();
      }
    }
    
    function delMob(id) {
      if(confirm('Delete routine?')) {
        mobilityRoutines = mobilityRoutines.filter(x => x.id !== id);
        renderMobility();
      }
    }
    
    function addMob() {
      const name = document.getElementById('mobNameInput').value.trim();
      const note = document.getElementById('mobNoteInput').value.trim();
      if (!name) return;
      mobilityRoutines.push({ id: Date.now()+'', name, note, checked: false, lastDate: '' });
      document.getElementById('mobNameInput').value = '';
      document.getElementById('mobNoteInput').value = '';
      document.getElementById('mobModal').style.display = 'none';
      renderMobility();
    }
"""

if 'id="mobility"' not in html:
    html = html.replace('<!-- BOTTOM NAV -->', mobility_html + '\n\n    <!-- BOTTOM NAV -->')

if 'id="mobModal"' not in html:
    html = html.replace('<script>', mob_modal + '\n  <script>')

if '// ── MOBILITY ──' not in html:
    html = html.replace('// ── NAV ──', js_logic + '\n\n    // ── NAV ──')
    html = html.replace('renderSupps();', 'renderSupps();\n    renderMobility();')

with open("fitness_hub_v3.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Mobility")
