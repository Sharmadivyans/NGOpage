import re
from collections import defaultdict

with open('what-we-do.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all dates and descriptions using regex
# We look for the date div and the desc div. Since HTML is malformed, we use robust regex.
pattern = r'<div style="font-weight: 800;[^>]*>([^<]+)</div>\s*<div style="font-size: 1.1rem;[^>]*>([^<]*?(?:</div>|<|\n\s*</details>))'

matches = re.findall(pattern, content)

events = []
for date, desc in matches:
    desc = desc.replace('</div>', '').replace('</details>', '').replace('<', '').strip()
    date = date.strip()
    if date and desc:
        events.append((date, desc))

categories = defaultdict(list)
for date, desc in events:
    text = desc.lower()
    if any(w in text for w in ['drawing', 'stationery', 'books', 'bag', 'school', 'career']):
        categories['Education & Child Support'].append((date, desc))
    elif any(w in text for w in ['health', 'medical', 'check up', 'ecg', 'diabetes']):
        categories['Healthcare & Medical'].append((date, desc))
    elif any(w in text for w in ['tree', 'plantation', 'environment', 'climate']):
        categories['Environmental Actions'].append((date, desc))
    elif any(w in text for w in ['sanitary', 'pad', 'woman', 'women', 'girl', 'saari']):
        categories['Women Empowerment'].append((date, desc))
    elif any(w in text for w in ['financial', 'aadhar', 'demographic', 'literacy']):
        categories['Awareness & Services'].append((date, desc))
    elif any(w in text for w in ['celebration', 'day', 'jayanti', 'holi', 'diwali', 'independence', 'new year']):
        categories['Festivals & National Days'].append((date, desc))
    else:
        categories['Community Relief (Nutrition & Winter)'].append((date, desc))

category_icons = {
    'Education & Child Support': 'fa-book-open',
    'Healthcare & Medical': 'fa-stethoscope',
    'Environmental Actions': 'fa-leaf',
    'Women Empowerment': 'fa-person-dress',
    'Awareness & Services': 'fa-bullhorn',
    'Festivals & National Days': 'fa-cake-candles',
    'Community Relief (Nutrition & Winter)': 'fa-hand-holding-heart'
}

# Generate new Accordion HTML
timeline_html = '<div class="categorized-activities" style="width: 100%;">\n'

# We make the first one open
first = True
for cat, items in categories.items():
    if not items: continue
    icon = category_icons.get(cat, 'fa-star')
    open_attr = 'open' if first else ''
    first = False
    
    timeline_html += f'''
    <details {open_attr} class="activity-accordion glass" style="margin-bottom: 1rem; border-radius: 10px; cursor: pointer;">
        <summary class="playfair" style="padding: 1.25rem 1.5rem; font-size: 1.25rem; font-weight: 700; display: flex; align-items: center; gap: 10px; color: var(--accent-primary); outline: none; list-style: none;">
            <i class="fa-solid {icon}"></i> {cat}
            <i class="fa-solid fa-chevron-down" style="margin-left: auto; font-size: 1rem; color: var(--text-muted);"></i>
        </summary>
        <div style="padding: 0 1.5rem 1.5rem; display: flex; flex-direction: column; gap: 1rem; max-height: 400px; overflow-y: auto;">
    '''
    for date, desc in items:
        timeline_html += f'''
            <div class="cat-item" style="background: rgba(255,255,255,0.8); border-radius: 8px; padding: 1rem 1.5rem; border-left: 4px solid var(--accent-secondary); box-shadow: 0 2px 5px rgba(0,0,0,0.05); display: flex; flex-direction: column; gap: 0.25rem;">
                <div style="font-weight: 800; font-size: 0.9rem; color: var(--accent-secondary); text-transform: uppercase; letter-spacing: 0.5px;">{date}</div>
                <div style="font-size: 1.05rem; color: var(--text-main); font-weight: 600;">{desc}</div>
            </div>
        '''
    timeline_html += '''
        </div>
    </details>
    '''
timeline_html += '</div>'

# Rebuilding the full HTML structure for what-we-do.html
new_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>What We Do | Jan Manas Foundation</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="style.css">
    <style>
        .activity-accordion summary::-webkit-details-marker {{ display: none; }}
        .activity-accordion[open] summary .fa-chevron-down {{ transform: rotate(180deg); }}
        .activity-accordion summary .fa-chevron-down {{ transition: transform 0.3s ease; }}
    </style>
</head>
<body>
    <!-- Animated NGO Background -->
    <div class="ngo-nature-bg">
        <div class="css-leaf" style="left: 10%; animation-delay: 0s;"></div>
        <div class="css-heart" style="left: 30%; animation-delay: 5s;"></div>
        <div class="css-leaf" style="left: 60%; animation-delay: 12s; transform: scale(0.6)"></div>
        <div class="css-heart" style="left: 80%; animation-delay: 2s; transform: scale(1.5)"></div>
        <div class="css-leaf" style="left: 45%; animation-delay: 18s;"></div>
    </div>

    <!-- Navigation -->
    <nav id="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo"><img src="logo.png" alt="Jan Manas Foundation Logo"></a>
            <div class="nav-right-container">
                <div class="top-row">
                    <a href="donate.html" class="btn-donate-solid">DONATE NOW</a>
                    <div class="social-icons">
                        <a href="#" aria-label="Profile"><i class="fa-regular fa-user"></i></a>
                        <a href="https://x.com/JanManasFdnNGO" target="_blank" aria-label="X"><i class="fa-brands fa-x-twitter"></i></a>
                        <a href="https://www.facebook.com/share/18qwDYbKRt/" target="_blank" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="https://www.instagram.com/jan_manas_foundation?igsh=dWd1djZsOHhkZTBi" target="_blank" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
                        <a href="https://www.linkedin.com/in/sheetal-sharma-at-jan-manas-foundation-12ba6a2a5" target="_blank" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
                    </div>
                </div>
                <ul class="nav-links">
                    <li><a href="index.html">HOME</a></li>
                    <li><a href="about.html">ABOUT US</a></li>
                    <li><a href="what-we-do.html" class="active">WHAT WE DO</a></li>
                    <li><a href="media.html">MEDIA</a></li>
                    <li><a href="contact.html">CONTACT US</a></li>
                </ul>
            </div>
            <div class="hamburger">
                <span></span><span></span><span></span>
            </div>
        </div>
    </nav>

    <!-- Page Header -->
    <section class="page-header fade-up">
        <div class="section-subtitle">Our Initiatives</div>
        <h1 class="page-title playfair text-gradient">What We Do</h1>
        <p class="page-subtitle" style="max-width: 700px; margin: 0 auto;">Our mission spans critical social pillars. We organize drives and programs deeply rooted in grassroots realities to uplift underserved communities across India.</p>
    </section>

    <!-- Core Pillars Grid -->
    <section class="fade-up" style="padding-top: 0;">
        <div class="grid-container">
            <div class="card glass tilt">
                <div class="tilt-inner">
                    <h3 class="playfair text-gradient"><i class="fa-solid fa-book-open"></i> Education</h3>
                    <p>Providing direct interventions in schools to dramatically improve learning outcomes, supply essential learning materials, and reduce dropout rates among vulnerable youth.</p>
                </div>
            </div>
            <div class="card glass tilt">
                <div class="tilt-inner">
                    <h3 class="playfair text-gradient" style="color: var(--accent-secondary);"><i class="fa-solid fa-heart-pulse"></i> Healthcare</h3>
                    <p>Delivering immediate medical relief, funding healthcare drives, and spreading crucial awareness regarding hygiene and maternal health in underdeveloped regions.</p>
                </div>
            </div>
            <div class="card glass tilt">
                <div class="tilt-inner">
                    <h3 class="playfair text-gradient"><i class="fa-solid fa-hand-fist"></i> Empowerment</h3>
                    <p>Championing gender justice and financial independence for women through skill-building workshops, micro-finance support, and comprehensive rights advocacy.</p>
                </div>
            </div>
            <div class="card glass tilt">
                <div class="tilt-inner">
                    <h3 class="playfair text-gradient" style="color: var(--accent-secondary);"><i class="fa-solid fa-leaf"></i> Environment</h3>
                    <p>Executing localized climate-action initiatives, tree-planting drives, and community-led waste management programs to secure a sustainable future.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Activity Log Section -->
    <section class="fade-up" style="background: rgba(255, 255, 255, 0.4); backdrop-filter: blur(10px); border-top: 1px solid rgba(255, 255, 255, 0.6); border-bottom: 1px solid rgba(255, 255, 255, 0.6);">
        <div class="section-header">
            <div class="section-subtitle">Real Impact</div>
            <h2 class="section-title playfair">Our Activity Log</h2>
            <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto;">Details of activities and interventions successfully carried out by JAN MANAS FOUNDATION on the ground.</p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 4rem; align-items: start;">
            <!-- Left Side: Interactive Timeline -->
            <div class="timeline-container">
                {timeline_html}
            </div>

            <!-- Right Side: Vertical Image Stack -->
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; position: sticky; top: 100px;">
                <img src="gallery_56.jpg" alt="Field activity" style="width: 100%; height: auto; display: block; border-radius: 12px; box-shadow: var(--shadow-sm); grid-column: span 2;">
                <img src="gallery_57.jpg" alt="Volunteer engagement" style="width: 100%; height: auto; display: block; border-radius: 12px; box-shadow: var(--shadow-sm);">
                <img src="gallery_58.jpg" alt="Awareness drive" style="width: 100%; height: auto; display: block; border-radius: 12px; box-shadow: var(--shadow-sm);">
                <img src="gallery_11.jpg" alt="Local impact" style="width: 100%; height: auto; display: block; border-radius: 12px; box-shadow: var(--shadow-sm);">
                <img src="gallery_20.jpg" alt="Children support" style="width: 100%; height: auto; display: block; border-radius: 12px; box-shadow: var(--shadow-sm);">
            </div>
        </div>
    </section>

    <!-- Ongoing Programs -->
    <section class="fade-up" style="padding-bottom: 8rem;">
        <div style="padding: 4rem 3rem; border-radius: var(--radius-xl); background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-dark) 100%); color: white; box-shadow: var(--shadow-hover); max-width: 1000px; margin: 0 auto; position: relative; overflow: hidden;">
            <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: rgba(255,255,255,0.1); border-radius: 50%;"></div>
            <div style="position: absolute; bottom: -50px; left: -50px; width: 150px; height: 150px; background: rgba(255,255,255,0.1); border-radius: 50%;"></div>
            
            <h3 class="playfair" style="margin-bottom: 2rem; color: #fff; font-size: 2.2rem; text-align: center; position: relative; z-index: 1;">Ongoing Regular Programs</h3>
            <ul style="list-style: none; max-width: 800px; margin: 0 auto; color: rgba(255, 255, 255, 0.95); font-size: 1.15rem; line-height: 1.8; position: relative; z-index: 1;">
                <li style="margin-bottom: 1.5rem; display: flex; align-items: flex-start; gap: 15px;">
                    <i class="fa-solid fa-cookie-bite" style="font-size: 1.5rem; margin-top: 4px;"></i> 
                    <span><strong>Snacks Distribution to Kids:</strong> Every weekend (Saturday) we celebrate by distributing snacks (Samosa, bread pakoda, jalebi, kachodi etc.) to children.</span>
                </li>
                <li style="display: flex; align-items: flex-start; gap: 15px;">
                    <i class="fa-solid fa-user-graduate" style="font-size: 1.5rem; margin-top: 4px;"></i> 
                    <span><strong>Free Career Counseling:</strong> We provide free career counseling to teenagers to help them navigate their future education and career needs.</span>
                </li>
            </ul>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-container fade-up">
            <div class="footer-col">
                <a href="index.html" class="logo" style="display:block; margin-bottom: 1rem;"><img src="logo.png" alt="Jan Manas Foundation Logo"></a>
                <p>BE 384 STREET NUMBER 7 HARI NAGAR</p>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="about.html">About us</a></li>
                    <li><a href="what-we-do.html">What we do</a></li>
                    <li><a href="media.html">Media</a></li>
                    <li><a href="contact.html">Contact us</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Contact</h4>
                <p>contact@janmanasfoundation.co.in</p>
                <p>+91 935 462 7100<br>+91 931 580 8651</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Jan Manas Foundation. All rights reserved.</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

with open('what-we-do.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Rebuilt what-we-do.html with {len(events)} events.")
