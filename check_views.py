import re

with open("fitness_hub_v3.html", "r") as f:
    html = f.read()

views = re.findall(r'<div id="([^"]+)" class="view', html)
print("Views:", views)
