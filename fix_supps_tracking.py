import re

with open("fitness_hub_v3.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Supps section
supps_new = """    <div id="supps" class="view">
      <div class="card" style="margin-bottom:12px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
          <div style="font-weight:600;font-size:15px;color:var(--t1)">Daily Intake</div>
          <div style="font-size:12px;color:var(--t2)" id="suppDate"></div>
        </div>
        <div id="suppLogList"></div>
      </div>

      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;padding:0 4px">
        <div style="font-size:14px;font-weight:600;color:var(--t2)">My Stack</div>
        <button class="btn" style="background:var(--card2);padding:6px 12px;font-size:12px" onclick="document.getElementById('suppModal').style.display='flex'">+ Add</button>
      </div>
      <div id="suppStack"></div>
    </div>"""

# Replace Tracking section
tracking_new = """    <div id="tracking" class="view">
      <div class="card" style="margin-bottom:12px">
        <div style="font-weight:600;font-size:15px;color:var(--t1);margin-bottom:12px">Weight Trend</div>
        <div style="display:flex;gap:12px;margin-bottom:16px">
          <div>
            <div style="font-size:12px;color:var(--t2)">Current</div>
            <div style="font-size:18px;font-weight:700" id="trackCurrentWeight">-- kg</div>
          </div>
          <div>
            <div style="font-size:12px;color:var(--t2)">Change</div>
            <div style="font-size:18px;font-weight:700;color:var(--sky)" id="trackWeightChange">-- kg</div>
          </div>
        </div>
        <div id="weightChart" style="height:140px;background:var(--bg);border-radius:var(--r);position:relative;overflow:hidden"></div>
        <div style="display:flex;gap:8px;margin-top:12px">
          <input type="number" id="newWeight" class="input" placeholder="Weight (kg)" style="flex:1" inputmode="decimal">
          <button class="btn" onclick="logWeight()">Log</button>
        </div>
      </div>

      <div style="display:flex;gap:12px;margin-bottom:12px">
        <div class="card" style="flex:1;display:flex;flex-direction:column;align-items:center">
          <div style="font-size:13px;color:var(--t2);margin-bottom:8px">Weight Goal</div>
          <div class="ring" id="ringWeight" style="--p:0;--c:var(--sky)"></div>
        </div>
        <div class="card" style="flex:1;display:flex;flex-direction:column;align-items:center">
          <div style="font-size:13px;color:var(--t2);margin-bottom:8px">Waist Goal</div>
          <div class="ring" id="ringWaist" style="--p:0;--c:var(--grn)"></div>
        </div>
      </div>

      <div class="card" style="margin-bottom:12px">
        <div style="font-weight:600;font-size:15px;color:var(--t1);margin-bottom:12px">Body Measurements</div>
        <div id="measurementsList"></div>
        <div style="display:flex;gap:8px;margin-top:12px">
          <input type="text" id="newMeasName" class="input" placeholder="e.g. Waist" style="flex:1">
          <input type="number" id="newMeasVal" class="input" placeholder="Value" style="width:70px" inputmode="decimal">
          <button class="btn" onclick="logMeasurement()">Log</button>
        </div>
      </div>
    </div>"""

# Replace Supp Modal
supp_modal_new = """
  <!-- SUPP MODAL -->
  <div id="suppModal" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.8);z-index:999;align-items:center;justify-content:center;padding:16px;backdrop-filter:blur(8px)">
    <div class="card" style="width:100%;max-width:400px">
      <div style="font-size:16px;font-weight:600;margin-bottom:16px">Add Supplement</div>
      <input type="text" id="suppNameInput" class="input" placeholder="Name (e.g. Creatine)" style="margin-bottom:12px">
      <input type="text" id="suppDoseInput" class="input" placeholder="Dosage (e.g. 5g daily)" style="margin-bottom:12px">
      <input type="text" id="suppWhyInput" class="input" placeholder="Purpose" style="margin-bottom:16px">
      <div style="display:flex;gap:8px">
        <button class="btn" style="flex:1;background:var(--card2)" onclick="document.getElementById('suppModal').style.display='none'">Cancel</button>
        <button class="btn" style="flex:1" onclick="addSupp()">Save</button>
      </div>
    </div>
  </div>
"""

# Regex replacements
content = re.sub(r'<div id="supps" class="view">.*?(?=<div id="tracking" class="view">)', supps_new + '\n\n', content, flags=re.DOTALL)
content = re.sub(r'<div id="tracking" class="view">.*?(?=<div id="deload" class="view">)', tracking_new + '\n\n', content, flags=re.DOTALL)

# Inject suppModal before <script>
content = re.sub(r'(<script>)', supp_modal_new + '\n  \\1', content)

with open("fitness_hub_v3.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")
