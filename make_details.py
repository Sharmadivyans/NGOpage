import re

with open('what-we-do.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div class="categorized-activities"')
end_idx = content.find('</div>\n                \n                    <!-- Right Side:')

if start_idx != -1 and end_idx != -1:
    cat_html = content[start_idx:end_idx]
    
    # We want to replace the category section div with <details>
    # <div class="activity-category-section" style="...">
    #     <h3 ...> <i ...></i> Title </h3>
    #     <div class="category-items-grid" style="...">
    #         ... items ...
    #     </div>
    # </div>
    
    # Let's extract each category block
    pattern = r'<div class="activity-category-section"[^>]*>\s*<h3 class="playfair text-gradient" style="font-size: 1.8rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 10px;">\s*(.*?)\s*</h3>\s*<div class="category-items-grid"[^>]*>(.*?)</div>\s*</div>'
    
    def replacer(match):
        header = match.group(1).strip() # <i class="..."></i> Title
        items = match.group(2).strip()
        
        return f'''
        <details class="activity-accordion" style="margin-bottom: 1rem; background: rgba(255,255,255,0.7); border-radius: 10px; border: 1px solid rgba(255,255,255,0.9); box-shadow: var(--shadow-sm); backdrop-filter: blur(10px);">
            <summary style="padding: 1.25rem 1.5rem; font-size: 1.25rem; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 10px; color: var(--accent-primary); outline: none;">
                {header}
            </summary>
            <div style="padding: 0 1.5rem 1.5rem; display: flex; flex-direction: column; gap: 1rem; max-height: 400px; overflow-y: auto;">
                {items}
            </div>
        </details>
        '''
    
    new_html = re.sub(pattern, replacer, cat_html, flags=re.DOTALL)
    
    # Change the first <details> to <details open>
    new_html = new_html.replace('<details class="activity-accordion"', '<details open class="activity-accordion"', 1)
    
    new_content = content[:start_idx] + new_html + content[end_idx:]
    
    with open('what-we-do.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Accordions updated successfully")
else:
    print("Could not find categories block")
