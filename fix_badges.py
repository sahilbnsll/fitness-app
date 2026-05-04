import re

with open("fitness_hub_v3.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("badge: '🛡️🦍'", "badge: '🦍'")
html = html.replace("badge: '🔙🦾'", "badge: '🦾'")
html = html.replace("badge: '🦵🦿'", "badge: '🦿'")

with open("fitness_hub_v3.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated badges")
