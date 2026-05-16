import re

with open('what-we-do.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div class="icon-timeline"')
end_idx = content.find('</div>\n                    </div>\n                \n                    <!-- Right Side:')

if start_idx != -1 and end_idx != -1:
    timeline_html = content[start_idx:end_idx]
    pattern = r'<div class="icon-timeline-date[^>]*>(.*?)</div>\s*<div class="icon-timeline-desc">(.*?)</div>'
    matches = re.findall(pattern, timeline_html, flags=re.DOTALL)
    for date, desc in matches:
        print(f"- {date}: {desc}")
