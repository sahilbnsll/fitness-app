import re

with open("fitness_hub_v3.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add CSS for logger
css_logger = """
    .logger-wrap {
      background: var(--bg);
      border-radius: 8px;
      padding: 12px;
      margin-top: 8px;
      display: none;
      flex-direction: column;
      gap: 8px;
    }
    .logger-row {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .logger-num {
      font-size: 13px; font-weight: 700; color: var(--t2); width: 20px; text-align: center;
    }
    .logger-input {
      flex: 1;
      background: var(--bg2);
      border: 1px solid var(--b2);
      border-radius: 8px;
      color: var(--t1);
      font-size: 16px;
      font-weight: 600;
      padding: 10px 8px;
      text-align: center;
      min-width: 0;
    }
    .logger-input:focus {
      border-color: var(--sky);
      outline: none;
    }
    .logger-btn {
      width: 44px; height: 44px;
      border-radius: 8px;
      background: var(--card2);
      border: 1px solid var(--b2);
      display: flex; align-items: center; justify-content: center;
      font-weight: 700; color: var(--t1);
      cursor: pointer;
      flex-shrink: 0;
    }
    .logger-btn.done {
      background: var(--grn);
      color: #000;
      border-color: var(--grn);
    }
    .rest-timer {
      position: fixed;
      bottom: 80px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--card2);
      border: 1px solid var(--sky);
      border-radius: 20px;
      padding: 8px 16px;
      display: none;
      align-items: center;
      gap: 12px;
      z-index: 100;
      box-shadow: 0 4px 12px rgba(0,0,0,0.5);
      backdrop-filter: blur(10px);
    }
    .rest-timer.active {
      display: flex;
    }
"""

if ".logger-wrap" not in html:
    html = html.replace("</style>", css_logger + "\n  </style>")

# Modify buildDayCards
old_build_day_cards = """        exList.forEach((ex, i) => {
          const tags = ex.tags.map(t => `<span class="tag ${t}">${t}</span>`).join('');
          exHTML += `<div class="ex-row" id="exrow_${d.id}_${i}">
        <div class="ex-num">${i + 1}</div>
        <div class="ex-content">
          <div class="ex-name">${ex.name}</div>
          <div class="ex-detail">${ex.detail}</div>
          ${tags ? `<div class="ex-tags">${tags}</div>` : ''}
        </div>
        <div class="ex-del" onclick="deleteEx('${d.id}',${i})">×</div>
      </div>`;
        });"""

new_build_day_cards = """        exList.forEach((ex, i) => {
          const tags = ex.tags.map(t => `<span class="tag ${t}">${t}</span>`).join('');
          exHTML += `<div class="ex-row" id="exrow_${d.id}_${i}" onclick="toggleLogger('${d.id}', ${i})">
        <div class="ex-num">${i + 1}</div>
        <div class="ex-content">
          <div class="ex-name">${ex.name}</div>
          <div class="ex-detail">${ex.detail}</div>
          ${tags ? `<div class="ex-tags">${tags}</div>` : ''}
        </div>
        <div class="ex-del" onclick="event.stopPropagation(); deleteEx('${d.id}',${i})">×</div>
      </div>
      <div class="logger-wrap" id="logger_${d.id}_${i}"></div>`;
        });"""

if "toggleLogger" not in html:
    html = html.replace(old_build_day_cards, new_build_day_cards)

# Add logger logic
logger_js = """    // ── WORKOUT LOGGER ──
    const SK_LOGS = 'ft_workout_logs_v1';
    let workoutLogs = JSON.parse(localStorage.getItem(SK_LOGS)) || {};
    
    function saveLogs() {
      localStorage.setItem(SK_LOGS, JSON.stringify(workoutLogs));
    }
    
    function getTodayKey() {
      return new Date().toISOString().slice(0, 10);
    }
    
    function toggleLogger(dayId, exIdx) {
      const wrap = document.getElementById(`logger_${dayId}_${exIdx}`);
      if (wrap.style.display === 'flex') {
        wrap.style.display = 'none';
        return;
      }
      wrap.style.display = 'flex';
      renderLogger(dayId, exIdx);
    }
    
    function renderLogger(dayId, exIdx) {
      const wrap = document.getElementById(`logger_${dayId}_${exIdx}`);
      const ex = exercises[dayId][exIdx];
      const today = getTodayKey();
      
      if (!workoutLogs[today]) workoutLogs[today] = {};
      if (!workoutLogs[today][ex.name]) {
        // Default to 3 sets
        workoutLogs[today][ex.name] = [
          { w: '', r: '', done: false },
          { w: '', r: '', done: false },
          { w: '', r: '', done: false }
        ];
      }
      
      const sets = workoutLogs[today][ex.name];
      
      let html = `<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;padding:0 4px">
        <div style="font-size:12px;color:var(--t2);width:20px;text-align:center">Set</div>
        <div style="font-size:12px;color:var(--t2);flex:1;text-align:center">kg</div>
        <div style="font-size:12px;color:var(--t2);flex:1;text-align:center">Reps</div>
        <div style="font-size:12px;color:var(--t2);width:44px;text-align:center">✔</div>
      </div>`;
      
      sets.forEach((s, sIdx) => {
        html += `
        <div class="logger-row">
          <div class="logger-num">${sIdx + 1}</div>
          <input type="number" inputmode="decimal" class="logger-input" placeholder="-" value="${s.w}" onchange="updateSet('${ex.name}', ${sIdx}, 'w', this.value)">
          <input type="number" inputmode="numeric" class="logger-input" placeholder="-" value="${s.r}" onchange="updateSet('${ex.name}', ${sIdx}, 'r', this.value)">
          <div class="logger-btn ${s.done ? 'done' : ''}" onclick="toggleSetDone('${ex.name}', ${sIdx}, this)">✓</div>
        </div>`;
      });
      
      html += `
      <div style="display:flex;justify-content:center;margin-top:4px">
        <button class="btn" style="background:transparent;border:1px dashed var(--b2);color:var(--t2);padding:6px 16px;font-size:13px" onclick="addSet('${dayId}', ${exIdx}, '${ex.name}')">+ Add Set</button>
      </div>`;
      
      wrap.innerHTML = html;
    }
    
    function updateSet(exName, sIdx, field, val) {
      const today = getTodayKey();
      workoutLogs[today][exName][sIdx][field] = val;
      saveLogs();
    }
    
    function toggleSetDone(exName, sIdx, btnEl) {
      const today = getTodayKey();
      const s = workoutLogs[today][exName][sIdx];
      s.done = !s.done;
      saveLogs();
      if (s.done) {
        btnEl.classList.add('done');
        startRestTimer(90); // Default 90s rest
      } else {
        btnEl.classList.remove('done');
      }
    }
    
    function addSet(dayId, exIdx, exName) {
      const today = getTodayKey();
      workoutLogs[today][exName].push({ w: '', r: '', done: false });
      saveLogs();
      renderLogger(dayId, exIdx);
    }
    
    // ── REST TIMER ──
    let restInterval;
    let restTime = 0;
    
    function startRestTimer(seconds) {
      clearInterval(restInterval);
      restTime = seconds;
      const tWrap = document.getElementById('restTimer');
      const tVal = document.getElementById('restTimerVal');
      tWrap.classList.add('active');
      
      function update() {
        if (restTime <= 0) {
          clearInterval(restInterval);
          tWrap.classList.remove('active');
          navigator.vibrate && navigator.vibrate([200, 100, 200]);
          return;
        }
        const m = Math.floor(restTime / 60);
        const s = restTime % 60;
        tVal.textContent = `${m}:${s.toString().padStart(2, '0')}`;
        restTime--;
      }
      update();
      restInterval = setInterval(update, 1000);
    }
    
    function closeRestTimer() {
      clearInterval(restInterval);
      document.getElementById('restTimer').classList.remove('active');
    }
    function addRestTime(secs) {
      restTime += secs;
    }
"""

if "function toggleLogger" not in html:
    html = html.replace("// ── TRACKER ──", logger_js + "\n\n    // ── TRACKER ──")

timer_html = """
  <!-- REST TIMER -->
  <div class="rest-timer" id="restTimer">
    <div style="font-size:18px">⏱</div>
    <div id="restTimerVal" style="font-size:18px;font-weight:700;color:var(--t1);width:48px;text-align:center">1:30</div>
    <button style="background:var(--bg2);border:none;color:var(--t1);padding:6px 10px;border-radius:6px;font-weight:600;font-size:12px;cursor:pointer" onclick="addRestTime(30)">+30s</button>
    <button style="background:none;border:none;color:var(--t2);font-size:16px;cursor:pointer;padding:0 4px" onclick="closeRestTimer()">×</button>
  </div>
"""

if 'id="restTimer"' not in html:
    html = html.replace("</body>", timer_html + "\n</body>")

with open("fitness_hub_v3.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated workout logger")
