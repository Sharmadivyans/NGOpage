import re
from collections import defaultdict

with open('what-we-do.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div class="icon-timeline"')
end_idx = content.find('</div>\n                    </div>\n                \n                    <!-- Right Side:')

if start_idx != -1 and end_idx != -1:
    timeline_html = content[start_idx:end_idx]
    pattern = r'<div class="icon-timeline-date[^>]*>(.*?)</div>\s*<div class="icon-timeline-desc">(.*?)</div>'
    matches = re.findall(pattern, timeline_html, flags=re.DOTALL)
    
    categories = defaultdict(list)
    
    for date, desc in matches:
        text = desc.lower()
        date = date.strip()
        desc = desc.strip()
        
        if any(w in text for w in ['drawing', 'stationery', 'books', 'bag', 'school']):
            categories['Education & Child Support'].append((date, desc))
        elif any(w in text for w in ['health', 'medical']):
            categories['Healthcare & Medical'].append((date, desc))
        elif any(w in text for w in ['tree', 'plantation']):
            categories['Environmental Actions'].append((date, desc))
        elif any(w in text for w in ['sanitary', 'pad', 'woman', 'women', 'girl', 'saari']):
            categories['Women Empowerment'].append((date, desc))
        elif any(w in text for w in ['financial', 'aadhar', 'demographic']):
            categories['Awareness & Services'].append((date, desc))
        elif any(w in text for w in ['celebration', 'day', 'jayanti', 'holi', 'diwali', 'independence']):
            categories['Festivals & National Days'].append((date, desc))
        else:
            categories['Community Relief (Nutrition & Winter)'].append((date, desc))

    # Build new HTML
    new_html = '<div class="categorized-activities" style="width: 100%;">\n'
    
    category_icons = {
        'Education & Child Support': 'fa-book-open',
        'Healthcare & Medical': 'fa-stethoscope',
        'Environmental Actions': 'fa-leaf',
        'Women Empowerment': 'fa-person-dress',
        'Awareness & Services': 'fa-bullhorn',
        'Festivals & National Days': 'fa-cake-candles',
        'Community Relief (Nutrition & Winter)': 'fa-hand-holding-heart'
    }
    
    for cat, items in categories.items():
        if not items: continue
        icon = category_icons.get(cat, 'fa-star')
        
        new_html += f'''
        <div class="activity-category-section" style="margin-bottom: 3rem;">
            <h3 class="playfair text-gradient" style="font-size: 1.8rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 10px;">
                <i class="fa-solid {icon}"></i> {cat}
            </h3>
            <div class="category-items-grid" style="display: flex; flex-direction: column; gap: 1rem;">
        '''
        for date, desc in items:
            new_html += f'''
                <div class="cat-item" style="background: rgba(255,255,255,0.7); border-radius: 10px; padding: 1rem 1.5rem; border: 1px solid rgba(255,255,255,0.9); display: flex; flex-direction: column; gap: 0.25rem;">
                    <div style="font-weight: 800; font-size: 0.95rem; color: var(--accent-secondary); text-transform: uppercase; letter-spacing: 0.5px;">{date}</div>
                    <div style="font-size: 1.1rem; color: var(--text-main); font-weight: 500;">{desc}</div>
                </div>
            '''
        new_html += '''
            </div>
        </div>
        '''
        
    new_html += '</div>'
    
    # Remove tilt class from page-content
    content = content.replace('class="glass card glass-glow page-content fade-up tilt"', 'class="glass card glass-glow page-content fade-up"')
    
    new_content = content[:start_idx] + new_html + content[end_idx:]
    
    with open('what-we-do.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Activities categorized and updated successfully")
else:
    print("Could not find timeline block")
