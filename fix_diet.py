import re

with open("fitness_hub_v3.html", "r", encoding="utf-8") as f:
    html = f.read()

diet_html = """    <div id="diet" class="view">
      <div class="nav-scroll" style="margin-bottom:12px; border-bottom:1px solid var(--b2); padding-bottom:12px;" id="dietDaysNav">
      </div>
      <div id="dietContent">
      </div>
    </div>"""

diet_start = html.find('<div id="diet" class="view">')
diet_end = html.find('<div id="supps" class="view">')

if diet_start != -1 and diet_end != -1:
    html = html[:diet_start] + diet_html + '\n\n' + html[diet_end:]

js_logic = """    // ── DIET ──
    let activeDietDay = 0;
    const dietPlans = [];
    for(let i=0; i<15; i++) {
        let isRest = (i+1) % 7 === 0;
        let cals = isRest ? 2000 : 2200;
        let carbs = isRest ? 180 : 220;
        let type = isRest ? 'Rest Day' : 'Training Day';
        let macros = { cals: cals, prot: '180g', carb: carbs+'g', fat: '60g' };
        let micros = { iron: '15mg', calcium: '1000mg', vitD: '600 IU', zinc: '11mg' };
        
        let meals = [];
        if (!isRest) {
            meals = [
                { time: 'Breakfast', name: '5 whole eggs + 2 multigrain rotis + 1 cup milk', note: 'High protein morning anchor.', prot: '40g', color: 'var(--acc2)' },
                { time: 'Pre-workout', name: '1 banana + 30g oats + 1 scoop whey', note: 'Fast carbs + protein.', prot: '28g', color: 'var(--sky)' },
                { time: 'Post-workout', name: '1 scoop whey + 1 apple', note: 'Fast absorption.', prot: '25g', color: 'var(--grn)' },
                { time: 'Lunch', name: '200g paneer + 2 rotis + rajma + salad', note: 'Biggest meal. Max protein + fiber.', prot: '55g', color: 'var(--amb)' },
                { time: 'Dinner', name: '4 egg-whites + dal + 1 roti + sabzi', note: 'Low carb end of day.', prot: '35g', color: 'var(--acc)' }
            ];
        } else {
            meals = [
                { time: 'Breakfast', name: '4 whole eggs + 1 roti + milk', note: 'Slightly lower carbs.', prot: '35g', color: 'var(--acc2)' },
                { time: 'Lunch', name: '150g paneer + 2 rotis + salad', note: 'Moderate protein & fat.', prot: '40g', color: 'var(--amb)' },
                { time: 'Snack', name: 'Greek yogurt + almonds', note: 'Healthy fats & probiotics.', prot: '15g', color: 'var(--ora)' },
                { time: 'Dinner', name: 'Soya chunks sabzi + dal + 1 roti', note: 'High fiber, medium protein.', prot: '30g', color: 'var(--acc)' }
            ];
        }
        
        if (i%3===0) {
            meals[0].name = 'Oats porridge with whey + 3 boiled eggs';
            macros.cals += 50;
        } else if (i%4===0) {
            meals[meals.length-1].name = 'Chicken breast (150g) + veggies + 1 roti';
            macros.prot = '190g';
            micros.iron = '18mg';
        }
        
        dietPlans.push({ day: i+1, type: type, macros: macros, micros: micros, meals: meals });
    }

    function renderDietDays() {
      const nav = document.getElementById('dietDaysNav');
      nav.innerHTML = dietPlans.map((p, i) => `
        <button class="nb ${i === activeDietDay ? 'on' : ''}" onclick="selectDietDay(${i}, this)" style="flex-shrink:0">Day ${p.day}</button>
      `).join('');
    }

    function selectDietDay(idx, btn) {
      activeDietDay = idx;
      document.querySelectorAll('#dietDaysNav .nb').forEach(b => b.classList.remove('on'));
      if(btn) btn.classList.add('on');
      renderDietContent();
    }

    function renderDietContent() {
      const p = dietPlans[activeDietDay];
      const html = `
        <p class="slbl">${p.type} targets</p>
        <div class="metric-2">
          <div class="m"><div class="m-val" style="color:var(--acc2)">${p.macros.cals}</div><div class="m-lbl">kcal</div></div>
          <div class="m"><div class="m-val" style="color:var(--grn)">${p.macros.prot}</div><div class="m-lbl">protein</div></div>
          <div class="m"><div class="m-val" style="color:var(--sky)">${p.macros.carb}</div><div class="m-lbl">carbs</div></div>
          <div class="m"><div class="m-val" style="color:var(--amb)">${p.macros.fat}</div><div class="m-lbl">fats</div></div>
        </div>
        <p class="slbl" style="margin-top:16px">Micronutrients</p>
        <div style="display:flex;gap:8px;overflow-x:auto;padding-bottom:12px;scrollbar-width:none" class="nav-scroll">
          <div class="card" style="padding:8px 12px;min-width:80px;text-align:center">
            <div style="font-size:10px;color:var(--t3)">Iron</div>
            <div style="font-weight:600;color:var(--t1)">${p.micros.iron}</div>
          </div>
          <div class="card" style="padding:8px 12px;min-width:80px;text-align:center">
            <div style="font-size:10px;color:var(--t3)">Calcium</div>
            <div style="font-weight:600;color:var(--t1)">${p.micros.calcium}</div>
          </div>
          <div class="card" style="padding:8px 12px;min-width:80px;text-align:center">
            <div style="font-size:10px;color:var(--t3)">Vit D</div>
            <div style="font-weight:600;color:var(--t1)">${p.micros.vitD}</div>
          </div>
          <div class="card" style="padding:8px 12px;min-width:80px;text-align:center">
            <div style="font-size:10px;color:var(--t3)">Zinc</div>
            <div style="font-weight:600;color:var(--t1)">${p.micros.zinc}</div>
          </div>
        </div>
        <p class="slbl">Meal Plan</p>
        ${p.meals.map(m => `
          <div class="meal" style="--meal-acc:${m.color}">
            <div class="meal-time">${m.time}</div>
            <div class="meal-name">${m.name}</div>
            <div class="meal-note">${m.note}</div>
            <div class="meal-footer"><span class="meal-prot">~${m.prot} protein</span></div>
          </div>
        `).join('')}
      `;
      document.getElementById('dietContent').innerHTML = html;
    }
"""

if "// ── DIET ──" not in html:
    html = html.replace('// ── NAV ──', js_logic + '\n\n    // ── NAV ──')
    html = html.replace('renderSupps();', 'renderSupps();\n    renderDietDays();\n    renderDietContent();')

with open("fitness_hub_v3.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Diet module")
