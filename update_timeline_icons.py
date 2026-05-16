import re

with open('what-we-do.html', 'r', encoding='utf-8') as f:
    content = f.read()

def get_icon_for_content(text):
    text = text.lower()
    if 'drawing' in text or 'stationery' in text or 'books' in text or 'bag' in text:
        return 'fa-solid fa-book-open'
    if 'health' in text or 'medical' in text:
        return 'fa-solid fa-stethoscope'
    if 'tree' in text or 'plantation' in text:
        return 'fa-solid fa-leaf'
    if 'sanitary' in text or 'pad' in text or 'woman' in text or 'women' in text or 'girl' in text:
        return 'fa-solid fa-person-dress'
    if 'woolen' in text or 'blanket' in text or 'jacket' in text or 'winter' in text:
        return 'fa-solid fa-mitten'
    if 'nutrition' in text or 'food' in text or 'drinks' in text or 'juice' in text:
        return 'fa-solid fa-apple-whole'
    if 'shoe' in text or 'sleeper' in text:
        return 'fa-solid fa-shoe-prints'
    if 'celebration' in text or 'day' in text or 'jayanti' in text:
        return 'fa-solid fa-cake-candles'
    return 'fa-solid fa-hand-holding-heart'

start_idx = content.find('<div class="activity-list"')
end_idx = content.find('</div>\n                    </div>\n                \n                    <!-- Right Side:')

if start_idx != -1 and end_idx != -1:
    timeline_html = content[start_idx:end_idx]
    
    pattern = r'<div class="activity-card">\s*<img[^>]*>\s*<div class="activity-info">\s*<div class="activity-date[^>]*>(.*?)</div>\s*<div class="activity-desc">(.*?)</div>\s*</div>\s*</div>'
    
    def replacer(match):
        date = match.group(1).strip()
        desc = match.group(2).strip()
        icon = get_icon_for_content(desc)
        
        return f'''<div class="icon-timeline-item">
                        <div class="icon-timeline-icon"><i class="{icon}"></i></div>
                        <div class="icon-timeline-content">
                            <div class="icon-timeline-date text-gradient playfair">{date}</div>
                            <div class="icon-timeline-desc">{desc}</div>
                        </div>
                    </div>'''
    
    new_timeline_html = re.sub(pattern, replacer, timeline_html, flags=re.DOTALL)
    
    # Remove the inline styles causing scrolling
    new_timeline_html = new_timeline_html.replace('style="max-height: 800px; overflow-y: auto; padding: 1rem 1rem 1rem 0; width: 100%;"', 'style="width: 100%; position: relative;"')
    
    # Change class
    new_timeline_html = new_timeline_html.replace('class="activity-list"', 'class="icon-timeline"')
    
    new_content = content[:start_idx] + new_timeline_html + content[end_idx:]
    
    with open('what-we-do.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Timeline icons updated successfully")
else:
    print("Could not find timeline block")
