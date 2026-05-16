import os

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the grid opening tag to add id="reviews-grid"
old_grid_start = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">'
new_grid_start = '<div id="reviews-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">'
content = content.replace(old_grid_start, new_grid_start)

new_reviews = """
            <!-- New Reviews -->
            <div class="glass card tilt" style="padding: 2rem; border-radius: 15px; border-left: 4px solid var(--accent-primary);">
                <div class="tilt-inner">
                    <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(135deg, var(--accent-primary), #00c6ff); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem; font-weight: bold; margin-right: 15px;">
                            CS
                        </div>
                        <div>
                            <h4 class="playfair" style="font-size: 1.2rem; margin: 0;">Chatanya Sharma</h4>
                            <p style="font-size: 0.85rem; color: var(--accent-secondary); margin: 0; font-weight: 700; text-transform: uppercase;">Volunteer</p>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                        "Working with the Jan Manas Foundation has been an eye-opening experience. The dedication the team shows towards uplifting the underprivileged children is truly inspiring. I've seen firsthand how a little effort can bring huge smiles to these kids."
                    </p>
                </div>
            </div>

            <div class="glass card tilt" style="padding: 2rem; border-radius: 15px; border-left: 4px solid var(--accent-secondary);">
                <div class="tilt-inner">
                    <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(135deg, var(--accent-secondary), #ff2a00); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem; font-weight: bold; margin-right: 15px;">
                            DG
                        </div>
                        <div>
                            <h4 class="playfair" style="font-size: 1.2rem; margin: 0;">Daksh Ghai</h4>
                            <p style="font-size: 0.85rem; color: var(--accent-primary); margin: 0; font-weight: 700; text-transform: uppercase;">SRM University</p>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                        "The impact that Jan Manas makes on grassroots levels is incredible. Participating in their distribution drives made me realize the power of collective community action. A fantastic initiative that I'm proud to support."
                    </p>
                </div>
            </div>

            <div class="glass card tilt" style="padding: 2rem; border-radius: 15px; border-left: 4px solid var(--accent-primary);">
                <div class="tilt-inner">
                    <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(135deg, var(--accent-primary), #00c6ff); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem; font-weight: bold; margin-right: 15px;">
                            AK
                        </div>
                        <div>
                            <h4 class="playfair" style="font-size: 1.2rem; margin: 0;">Aditiya Kumar</h4>
                            <p style="font-size: 0.85rem; color: var(--accent-secondary); margin: 0; font-weight: 700; text-transform: uppercase;">DTU</p>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                        "I am continually amazed by the transparency and efficiency of this NGO. They ensure that every donation and volunteer hour goes directly to those who need it the most. The educational programs are particularly outstanding."
                    </p>
                </div>
            </div>

            <div class="glass card tilt" style="padding: 2rem; border-radius: 15px; border-left: 4px solid var(--accent-secondary);">
                <div class="tilt-inner">
                    <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(135deg, var(--accent-secondary), #ff2a00); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem; font-weight: bold; margin-right: 15px;">
                            JB
                        </div>
                        <div>
                            <h4 class="playfair" style="font-size: 1.2rem; margin: 0;">Jagrit Bhola</h4>
                            <p style="font-size: 0.85rem; color: var(--accent-primary); margin: 0; font-weight: 700; text-transform: uppercase;">DTU</p>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                        "Being part of the health checkup camps gave me immense satisfaction. Jan Manas Foundation is doing phenomenal work bridging the healthcare gap in slum areas. It's an honor to contribute to such a noble cause."
                    </p>
                </div>
            </div>

            <div class="glass card tilt" style="padding: 2rem; border-radius: 15px; border-left: 4px solid var(--accent-primary);">
                <div class="tilt-inner">
                    <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(135deg, var(--accent-primary), #00c6ff); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem; font-weight: bold; margin-right: 15px;">
                            DS
                        </div>
                        <div>
                            <h4 class="playfair" style="font-size: 1.2rem; margin: 0;">Divyansh Sharma</h4>
                            <p style="font-size: 0.85rem; color: var(--accent-secondary); margin: 0; font-weight: 700; text-transform: uppercase;">GGSIPU</p>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                        "What stands out about Jan Manas is their structured approach to problem-solving. It's not just temporary relief; they focus on sustainable empowerment, especially their initiatives for women. Keep up the brilliant work!"
                    </p>
                </div>
            </div>

            <div class="glass card tilt" style="padding: 2rem; border-radius: 15px; border-left: 4px solid var(--accent-secondary);">
                <div class="tilt-inner">
                    <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(135deg, var(--accent-secondary), #ff2a00); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem; font-weight: bold; margin-right: 15px;">
                            JK
                        </div>
                        <div>
                            <h4 class="playfair" style="font-size: 1.2rem; margin: 0;">Janika Kataria</h4>
                            <p style="font-size: 0.85rem; color: var(--accent-primary); margin: 0; font-weight: 700; text-transform: uppercase;">Christ University</p>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                        "Volunteering here completely changed my perspective on society. The foundation provides an excellent platform for youth to engage in meaningful social work. The smiles on the kids' faces are the ultimate reward."
                    </p>
                </div>
            </div>

            <div class="glass card tilt" style="padding: 2rem; border-radius: 15px; border-left: 4px solid var(--accent-primary);">
                <div class="tilt-inner">
                    <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(135deg, var(--accent-primary), #00c6ff); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem; font-weight: bold; margin-right: 15px;">
                            JB
                        </div>
                        <div>
                            <h4 class="playfair" style="font-size: 1.2rem; margin: 0;">Jeet Biswas</h4>
                            <p style="font-size: 0.85rem; color: var(--accent-secondary); margin: 0; font-weight: 700; text-transform: uppercase;">Supporter</p>
                        </div>
                    </div>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                        "The transparency and dedication of the Jan Manas team are unparalleled. You can literally see your contributions turning into tangible results on the ground. I highly recommend anyone looking to make a difference to join them."
                    </p>
                </div>
            </div>
"""

form_html = """
        <!-- Add Review Form -->
        <div class="glass card fade-up" style="max-width: 600px; margin: 4rem auto 0; padding: 2rem;">
            <h3 class="playfair text-gradient" style="text-align: center; margin-bottom: 1.5rem; font-size: 2rem;">Leave a Review</h3>
            <form id="review-form" style="display: flex; flex-direction: column; gap: 1rem;">
                <input type="text" id="rev-name" placeholder="Your Name" required style="padding: 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.8); font-family: inherit; font-size: 1rem; color: #333;">
                <input type="text" id="rev-org" placeholder="University / Organization (Optional)" style="padding: 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.8); font-family: inherit; font-size: 1rem; color: #333;">
                <textarea id="rev-text" placeholder="Write your review here..." required rows="4" style="padding: 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.8); font-family: inherit; font-size: 1rem; resize: vertical; color: #333;"></textarea>
                <button type="submit" class="btn-donate-solid" style="align-self: center; border: none; cursor: pointer; padding: 1rem 2rem; font-size: 1.1rem; border-radius: 50px;">Submit Review</button>
            </form>
        </div>
"""

js_code = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const form = document.getElementById('review-form');
            const grid = document.getElementById('reviews-grid');
            
            if (form && grid) {
                // Load saved reviews from localStorage
                const savedReviews = JSON.parse(localStorage.getItem('userReviews')) || [];
                savedReviews.forEach(rev => appendReview(rev));

                form.addEventListener('submit', (e) => {
                    e.preventDefault();
                    const name = document.getElementById('rev-name').value.trim();
                    let org = document.getElementById('rev-org').value.trim();
                    const text = document.getElementById('rev-text').value.trim();
                    
                    if(!org) org = "Supporter";
                    
                    const newReview = { name, org, text };
                    appendReview(newReview);
                    
                    // Save to localStorage so it persists
                    savedReviews.push(newReview);
                    localStorage.setItem('userReviews', JSON.stringify(savedReviews));
                    
                    form.reset();
                    alert("Thank you! Your review has been added.");
                });
                
                function appendReview(review) {
                    const initials = review.name.split(' ').map(n => n[0]).join('').substring(0,2).toUpperCase();
                    // Alternate colors randomly
                    const isPrimary = Math.random() > 0.5;
                    const borderColor = isPrimary ? 'var(--accent-primary)' : 'var(--accent-secondary)';
                    const gradient = isPrimary ? 'linear-gradient(135deg, var(--accent-primary), #00c6ff)' : 'linear-gradient(135deg, var(--accent-secondary), #ff2a00)';
                    const roleColor = isPrimary ? 'var(--accent-secondary)' : 'var(--accent-primary)';
                    
                    const div = document.createElement('div');
                    div.className = 'glass card tilt fade-up visible';
                    div.style.padding = '2rem';
                    div.style.borderRadius = '15px';
                    div.style.borderLeft = `4px solid ${borderColor}`;
                    
                    div.innerHTML = `
                        <div class="tilt-inner">
                            <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                                <div style="width: 50px; height: 50px; border-radius: 50%; background: ${gradient}; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem; font-weight: bold; margin-right: 15px;">
                                    ${initials}
                                </div>
                                <div>
                                    <h4 class="playfair" style="font-size: 1.2rem; margin: 0;">${review.name}</h4>
                                    <p style="font-size: 0.85rem; color: ${roleColor}; margin: 0; font-weight: 700; text-transform: uppercase;">${review.org}</p>
                                </div>
                            </div>
                            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                                "${review.text}"
                            </p>
                        </div>
                    `;
                    
                    grid.appendChild(div);
                }
            }
        });
    </script>
"""

# Find the closing tag of the testimonials grid
grid_end_idx = content.find('</section>', content.find('Voices of Impact'))
if grid_end_idx != -1:
    # We want to insert the new_reviews inside the grid, right before the </div> that closes the grid.
    # The grid is closed right before the </section>.
    grid_close_idx = content.rfind('</div>', 0, grid_end_idx)
    
    content = content[:grid_close_idx] + new_reviews + content[grid_close_idx:]

    # Now add the form_html right after the grid closes, inside the section.
    # We must find the grid_end_idx again because string length changed.
    grid_end_idx2 = content.find('</section>', content.find('Voices of Impact'))
    content = content[:grid_end_idx2] + form_html + "\n" + content[grid_end_idx2:]

# Insert the js_code right before </body>
content = content.replace('</body>', js_code + '\n</body>')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
