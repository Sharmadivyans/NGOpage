import re

with open('what-we-do.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define image mappings based on keywords
def get_image_for_content(text):
    text = text.lower()
    if 'drawing' in text or 'stationery' in text or 'books' in text or 'bag' in text:
        return 'gallery_2.jpg'
    if 'health' in text or 'medical' in text:
        return 'gallery_19.jpg'
    if 'tree' in text or 'plantation' in text:
        return 'gallery_11.jpg'
    if 'sanitary' in text or 'pad' in text or 'woman' in text or 'women' in text or 'girl' in text:
        return 'gallery_20.jpg'
    if 'woolen' in text or 'blanket' in text or 'jacket' in text or 'winter' in text:
        return 'gallery_9.jpg'
    if 'nutrition' in text or 'food' in text or 'drinks' in text or 'juice' in text:
        return 'gallery_1.jpg'
    if 'shoe' in text or 'sleeper' in text:
        return 'gallery_14.jpg'
    if 'celebration' in text or 'day' in text or 'jayanti' in text:
        return 'gallery_28.jpg'
    return 'gallery_6.jpg' # default image

# We will find the timeline block
start_idx = content.find('<div class="timeline"')
end_idx = content.find('</div>\n                    </div>\n                \n                    <!-- Right Side:')

if start_idx != -1 and end_idx != -1:
    timeline_html = content[start_idx:end_idx]
    
    # We need to find all <div class="timeline-item"> blocks
    # Using regex to match items
    pattern = r'<div class="timeline-item">\s*<div class="timeline-date[^>]*>(.*?)</div>\s*<div class="timeline-content">(.*?)</div>\s*</div>'
    
    def replacer(match):
        date = match.group(1).strip()
        desc = match.group(2).strip()
        img = get_image_for_content(desc)
        
        return f'''<div class="activity-card">
                        <img src="{img}" alt="{desc}" class="activity-img">
                        <div class="activity-info">
                            <div class="activity-date playfair text-gradient">{date}</div>
                            <div class="activity-desc">{desc}</div>
                        </div>
                    </div>'''
    
    new_timeline_html = re.sub(pattern, replacer, timeline_html, flags=re.DOTALL)
    
    # Replace class timeline with activity-list
    new_timeline_html = new_timeline_html.replace('class="timeline"', 'class="activity-list"')
    
    new_content = content[:start_idx] + new_timeline_html + content[end_idx:]
    
    with open('what-we-do.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Timeline updated successfully")
else:
    print("Could not find timeline block")
