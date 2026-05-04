import re

with open("fitness_hub_v3.html", "r", encoding="utf-8") as f:
    html = f.read()

lib_html = """
  <!-- EXERCISE LIBRARY MODAL -->
  <div id="libModal" style="display:none;position:fixed;inset:0;background:var(--bg);z-index:999;flex-direction:column;animation:slideIn 0.3s cubic-bezier(.32,1,.28,1)">
    <div style="padding:env(safe-area-inset-top,20px) 16px 12px;background:var(--card);border-bottom:1px solid var(--b2);display:flex;align-items:center;gap:12px">
      <button class="btn" style="width:36px;height:36px;padding:0;background:var(--bg2)" onclick="closeLibrary()">✕</button>
      <div style="flex:1">
        <input type="text" id="libSearch" class="input" placeholder="Search exercises..." style="width:100%" oninput="filterLibrary()">
      </div>
    </div>
    
    <div style="padding:12px 16px;display:flex;gap:8px;overflow-x:auto;border-bottom:1px solid var(--b2);scrollbar-width:none">
      <button class="tag active" id="libFilter_all" onclick="setLibFilter('all')">All</button>
      <button class="tag" id="libFilter_chest" onclick="setLibFilter('chest')">Chest</button>
      <button class="tag" id="libFilter_back" onclick="setLibFilter('back')">Back</button>
      <button class="tag" id="libFilter_legs" onclick="setLibFilter('legs')">Legs</button>
      <button class="tag" id="libFilter_shoulders" onclick="setLibFilter('shoulders')">Shoulders</button>
      <button class="tag" id="libFilter_arms" onclick="setLibFilter('arms')">Arms</button>
      <button class="tag" id="libFilter_core" onclick="setLibFilter('core')">Core</button>
    </div>
    
    <div id="libList" style="flex:1;overflow-y:auto;padding:12px 16px;"></div>
    
    <div style="padding:16px;padding-bottom:calc(16px + env(safe-area-inset-bottom, 20px));border-top:1px solid var(--b2);background:var(--card)">
      <div style="font-weight:600;font-size:14px;margin-bottom:8px">Create Custom</div>
      <div style="display:flex;gap:8px">
        <input type="text" id="libCustomInput" class="input" placeholder="Custom exercise name" style="flex:1">
        <button class="btn" onclick="addCustomExercise()">Add</button>
      </div>
    </div>
  </div>
"""

lib_js = """    // ── EXERCISE LIBRARY ──
    const EX_DB = [
      { name: 'Flat Barbell Bench Press', muscle: 'chest', tags: ['barbell', 'compound'] },
      { name: 'Incline Dumbbell Press', muscle: 'chest', tags: ['dumbbell', 'compound'] },
      { name: 'Cable Chest Fly (mid)', muscle: 'chest', tags: ['cable', 'isolation'] },
      { name: 'Weighted Pull-ups', muscle: 'back', tags: ['bodyweight', 'compound'] },
      { name: 'Wide Grip Lat Pulldown', muscle: 'back', tags: ['cable', 'compound'] },
      { name: 'Barbell Bent-over Row', muscle: 'back', tags: ['barbell', 'compound'] },
      { name: 'Seated Cable Row', muscle: 'back', tags: ['cable', 'compound'] },
      { name: 'Barbell Back Squat', muscle: 'legs', tags: ['barbell', 'compound'] },
      { name: 'Leg Press', muscle: 'legs', tags: ['machine', 'compound'] },
      { name: 'Romanian Deadlift (RDL)', muscle: 'legs', tags: ['barbell', 'compound'] },
      { name: 'Bulgarian Split Squat', muscle: 'legs', tags: ['dumbbell', 'compound'] },
      { name: 'Barbell Overhead Press', muscle: 'shoulders', tags: ['barbell', 'compound'] },
      { name: 'Seated DB Shoulder Press', muscle: 'shoulders', tags: ['dumbbell', 'compound'] },
      { name: 'DB Lateral Raises', muscle: 'shoulders', tags: ['dumbbell', 'isolation'] },
      { name: 'Cable Lateral Raise', muscle: 'shoulders', tags: ['cable', 'isolation'] },
      { name: 'Incline DB Curl', muscle: 'arms', tags: ['dumbbell', 'isolation'] },
      { name: 'Triceps Rope Pushdown', muscle: 'arms', tags: ['cable', 'isolation'] },
      { name: 'Skull Crushers (EZ bar)', muscle: 'arms', tags: ['barbell', 'isolation'] },
      { name: 'Cable Crunches', muscle: 'core', tags: ['cable', 'isolation'] },
      { name: 'Hanging Leg Raises', muscle: 'core', tags: ['bodyweight', 'isolation'] },
    ];
    
    let activeDayForLib = null;
    let currentLibFilter = 'all';
    
    function openLibrary(dayId) {
      activeDayForLib = dayId;
      document.getElementById('libModal').style.display = 'flex';
      setLibFilter('all');
    }
    
    function closeLibrary() {
      document.getElementById('libModal').style.display = 'none';
      activeDayForLib = null;
    }
    
    function setLibFilter(f) {
      currentLibFilter = f;
      const btns = ['all','chest','back','legs','shoulders','arms','core'];
      btns.forEach(b => {
        const el = document.getElementById('libFilter_' + b);
        if(el) {
          if(b === f) el.classList.add('active');
          else el.classList.remove('active');
        }
      });
      filterLibrary();
    }
    
    function filterLibrary() {
      const q = document.getElementById('libSearch').value.toLowerCase();
      const list = document.getElementById('libList');
      list.innerHTML = '';
      
      const filtered = EX_DB.filter(ex => {
        if(currentLibFilter !== 'all' && ex.muscle !== currentLibFilter) return false;
        if(q && !ex.name.toLowerCase().includes(q)) return false;
        return true;
      });
      
      filtered.forEach(ex => {
        const t = [ex.muscle, ...ex.tags].map(tag => `<span class="tag" style="background:var(--bg2)">${tag}</span>`).join('');
        list.innerHTML += `
        <div class="card" style="margin-bottom:8px;padding:12px;cursor:pointer" onclick="selectLibExercise('${ex.name}')">
          <div style="font-weight:600;font-size:15px;color:var(--t1)">${ex.name}</div>
          <div style="display:flex;gap:4px;margin-top:6px;flex-wrap:wrap">${t}</div>
        </div>`;
      });
    }
    
    function selectLibExercise(name) {
      if(!activeDayForLib) return;
      if(!exercises[activeDayForLib]) exercises[activeDayForLib] = [];
      exercises[activeDayForLib].push({ name, detail: '3 × 10', tags: [] });
      saveExercises();
      buildDayCards(); // refresh
      closeLibrary();
    }
    
    function addCustomExercise() {
      const name = document.getElementById('libCustomInput').value.trim();
      if(name) {
        selectLibExercise(name);
        document.getElementById('libCustomInput').value = '';
      }
    }
"""

if 'id="libModal"' not in html:
    html = html.replace('<!-- REST TIMER -->', lib_html + '\n  <!-- REST TIMER -->')

if '// ── EXERCISE LIBRARY ──' not in html:
    html = html.replace('// ── WORKOUT LOGGER ──', lib_js + '\n\n    // ── WORKOUT LOGGER ──')

# Replace the old `showAddForm` logic to just call `openLibrary(d.id)`
old_btn = `<div class="edit-btn" onclick="showAddForm('${d.id}')">+ Add exercise</div>`
new_btn = `<div class="edit-btn" onclick="openLibrary('${d.id}')">+ Add exercise</div>`
html = html.replace(old_btn, new_btn)

with open("fitness_hub_v3.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated library")
