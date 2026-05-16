document.addEventListener("DOMContentLoaded", () => {
    // 1. Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinksList = document.querySelector('.nav-links');
    if (hamburger && navLinksList) {
        hamburger.addEventListener('click', () => {
            navLinksList.classList.toggle('active');
        });
        navLinksList.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinksList.classList.remove('active');
            });
        });
    }

    // Hero Slider
    const slides = document.querySelectorAll('.hero-slide');
    const prevBtn = document.querySelector('.slider-prev');
    const nextBtn = document.querySelector('.slider-next');
    
    if (slides.length > 0) {
        let currentSlide = 0;
        let slideInterval;

        const nextSlide = () => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        };

        const prevSlide = () => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide - 1 + slides.length) % slides.length;
            slides[currentSlide].classList.add('active');
        };

        const startSlider = () => {
            slideInterval = setInterval(nextSlide, 4000);
        };

        const resetSlider = () => {
            clearInterval(slideInterval);
            startSlider();
        };

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                nextSlide();
                resetSlider();
            });
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                prevSlide();
                resetSlider();
            });
        }

        startSlider();
    }

    // 2. Sticky Navbar
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // 3. Intersection Observer for Fade Animations & Counters
    const observerOptions = { root: null, rootMargin: '0px', threshold: 0.01 };

    const countUp = (el) => {
        const target = +el.getAttribute('data-target');
        const count = +el.innerText.replace(/,/g, '');
        const increment = target / 100;
        if (count < target) {
            el.innerText = Math.ceil(count + increment).toLocaleString();
            setTimeout(() => countUp(el), 20);
        } else {
            el.innerText = target.toLocaleString() + '+';
        }
    };

    const observer = new IntersectionObserver((entries, observerInstance) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Trigger counters
                const counters = entry.target.querySelectorAll('.counter');
                counters.forEach(counter => {
                    if (!counter.classList.contains('counted')) {
                        countUp(counter);
                        counter.classList.add('counted');
                    }
                });
                observerInstance.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

    // 4. Advanced 3D Tilt Card Effect (Enhanced z-axis pop)
    const tiltElements = document.querySelectorAll('.tilt');
    tiltElements.forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            // Limit tilt magnitude to be much more subtle
            const rotateX = ((y - centerY) / centerY) * -3;
            const rotateY = ((x - centerX) / centerX) * 3;
            
            el.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.01, 1.01, 1.01)`;
        });
        
        el.addEventListener('mouseleave', () => {
            el.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
            el.style.transition = 'transform 0.5s ease-out';
            setTimeout(() => el.style.transition = '', 500);
        });
    });

    // 5. FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if(question) {
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                faqItems.forEach(i => i.classList.remove('active'));
                if (!isActive) item.classList.add('active');
            });
        }
    });

});

// Global function for copying UPI ID
window.copyUPI = function() {
    const upiText = document.getElementById('upi-text');
    const btn = document.getElementById('copy-btn');
    if (upiText && btn) {
        navigator.clipboard.writeText(upiText.innerText).then(() => {
            const originalText = btn.innerText;
            btn.innerText = 'Copied!';
            btn.style.background = 'var(--accent-leaf)';
            btn.style.color = '#fff';
            setTimeout(() => {
                btn.innerText = originalText;
                btn.style.background = '';
                btn.style.color = '';
            }, 2000);
        });
    }
};
