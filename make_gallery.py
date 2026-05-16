import os
import glob
import re

def natural_keys(text):
    return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', text)]

# 1. Generate gallery.html from media.html boilerplate
with open("media.html", "r") as f:
    content = f.read()

# Replace title
content = re.sub(r"<title>.*?</title>", "<title>Gallery | Jan Manas Foundation</title>", content)

# Remove the In The News section
content = re.sub(r"<!-- Main Content -->.*?<!-- Our Memories Gallery -->", "<!-- Our Memories Gallery -->", content, flags=re.DOTALL)

# Find all images
all_images = glob.glob("gallery_*.jpg") + glob.glob("photo_*.jpeg")
all_images.sort(key=natural_keys)

gallery_html = ""
for img in all_images:
    alt = "NGO Gallery Image"
    gallery_html += f'            <div class="masonry-item"><img src="{img}" alt="{alt}"><div class="overlay"><span>{alt}</span></div></div>\n'

# Replace the masonry gallery contents
content = re.sub(r'<div class="masonry-gallery">.*?</section>', f'<div class="masonry-gallery">\n{gallery_html}        </div>\n    </section>', content, flags=re.DOTALL)

# Set active class for GALLERY in gallery.html
content = content.replace('<li><a href="media.html" class="active">MEDIA</a></li>', '<li><a href="media.html">MEDIA</a></li>')

with open("gallery.html", "w") as f:
    f.write(content)

print("Generated gallery.html")

# 2. Update navigation in all HTML files
html_files = glob.glob("*.html")

for file in html_files:
    with open(file, "r") as f:
        html = f.read()
    
    changed = False
    
    if "GALLERY" not in html and "gallery.html" not in html:
        # Nav links replacement
        new_html = re.sub(r'(<li><a href="media.html"[^>]*>MEDIA</a></li>)', r'\1\n                    <li><a href="gallery.html">GALLERY</a></li>', html)
        # Footer links replacement
        new_html = re.sub(r'(<li><a href="media.html">Media</a></li>)', r'\1\n                    <li><a href="gallery.html">Gallery</a></li>', new_html)
        
        if new_html != html:
            changed = True
            html = new_html

    if file == "gallery.html" and 'class="active">GALLERY' not in html:
        html = html.replace('<li><a href="gallery.html">GALLERY</a></li>', '<li><a href="gallery.html" class="active">GALLERY</a></li>')
        changed = True

    if changed:
        with open(file, "w") as f:
            f.write(html)
        print(f"Updated nav in {file}")

# 3. Clean up media.html by removing the gallery section
with open("media.html", "r") as f:
    media_html = f.read()

# We might want to keep the media page focused on news
media_html_new = re.sub(r'<!-- Our Memories Gallery -->.*?</section>', '', media_html, flags=re.DOTALL)
if media_html != media_html_new:
    with open("media.html", "w") as f:
        f.write(media_html_new)
    print("Removed gallery from media.html")

