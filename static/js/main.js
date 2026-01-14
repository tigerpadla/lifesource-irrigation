// Lifesource Irrigation - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Navbar background change on scroll
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow');
            } else {
                navbar.classList.remove('shadow');
            }
        });
    }

    // Animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fadeInUp');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });

    // Gallery lightbox functionality
    const galleryItems = document.querySelectorAll('.gallery-item[data-bs-toggle="modal"]');
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const imgSrc = this.querySelector('img').src;
            const imgAlt = this.querySelector('img').alt;
            const modalImg = document.querySelector('#galleryModal .modal-body img');
            const modalTitle = document.querySelector('#galleryModal .modal-title');
            
            if (modalImg) {
                modalImg.src = imgSrc;
                modalImg.alt = imgAlt;
            }
            if (modalTitle) {
                modalTitle.textContent = imgAlt;
            }
        });
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Newsletter form AJAX submission with modal
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const emailInput = document.getElementById('newsletterEmail');
            const email = emailInput.value.trim();
            const csrfToken = this.querySelector('[name=csrfmiddlewaretoken]').value;
            
            // Basic email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!email || !emailRegex.test(email)) {
                showNewsletterModal(false, 'Invalid Email', 'Please enter a valid email address.');
                return;
            }
            
            // Submit via AJAX
            fetch(this.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                },
                body: `email=${encodeURIComponent(email)}&csrfmiddlewaretoken=${csrfToken}`
            })
            .then(response => response.json())
            .then(data => {
                showNewsletterModal(data.success, data.success ? 'Thank You!' : 'Oops!', data.message);
                if (data.success) {
                    emailInput.value = '';
                }
            })
            .catch(error => {
                showNewsletterModal(false, 'Error', 'Something went wrong. Please try again.');
            });
        });
    }
    
    // Show newsletter modal
    function showNewsletterModal(success, title, message) {
        const modal = document.getElementById('newsletterModal');
        const icon = document.getElementById('newsletterModalIcon');
        const titleEl = document.getElementById('newsletterModalTitle');
        const messageEl = document.getElementById('newsletterModalMessage');
        
        if (success) {
            icon.innerHTML = '<i class="bi bi-check-circle-fill text-success display-1"></i>';
        } else {
            icon.innerHTML = '<i class="bi bi-exclamation-circle-fill text-warning display-1"></i>';
        }
        
        titleEl.textContent = title;
        messageEl.textContent = message;
        
        const bsModal = new bootstrap.Modal(modal);
        bsModal.show();
    }
    
    // Contact form validation
    const contactForm = document.querySelector('.contact-form form');
    if (contactForm) {
        // Phone validation
        const phoneInput = document.getElementById('id_phone');
        if (phoneInput) {
            phoneInput.addEventListener('input', function() {
                // Allow digits, spaces, dashes, parentheses, plus
                this.value = this.value.replace(/[^\d\s\-\(\)\+]/g, '');
            });
            
            phoneInput.addEventListener('blur', function() {
                const digits = this.value.replace(/\D/g, '');
                if (digits.length > 0 && digits.length < 10) {
                    this.setCustomValidity('Please enter a valid phone number');
                    this.classList.add('is-invalid');
                } else {
                    this.setCustomValidity('');
                    if (digits.length >= 10) this.classList.remove('is-invalid');
                }
            });
        }
        
        // Email validation
        const emailInput = document.getElementById('id_email');
        if (emailInput) {
            emailInput.addEventListener('blur', function() {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (this.value && !emailRegex.test(this.value)) {
                    this.setCustomValidity('Please enter a valid email address');
                    this.classList.add('is-invalid');
                } else {
                    this.setCustomValidity('');
                    if (this.value) this.classList.remove('is-invalid');
                }
            });
        }
        
        // Services validation - at least one must be selected
        contactForm.addEventListener('submit', function(e) {
            const checkboxes = this.querySelectorAll('input[name="services_needed"]:checked');
            if (checkboxes.length === 0) {
                e.preventDefault();
                const servicesFieldset = this.querySelector('fieldset:has(input[name="services_needed"])') || 
                                         this.querySelectorAll('fieldset')[2];
                if (servicesFieldset) {
                    servicesFieldset.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    const firstCheckbox = this.querySelector('input[name="services_needed"]');
                    if (firstCheckbox) {
                        firstCheckbox.setCustomValidity('Please select at least one service');
                        firstCheckbox.reportValidity();
                    }
                }
                return false;
            }
            
            // Clear custom validity on all service checkboxes
            this.querySelectorAll('input[name="services_needed"]').forEach(cb => {
                cb.setCustomValidity('');
            });
        });
        
        // Clear services validation when any is checked
        contactForm.querySelectorAll('input[name="services_needed"]').forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                this.setCustomValidity('');
            });
        });
    }

    // Back to top button
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '<i class="bi bi-arrow-up"></i>';
    backToTop.className = 'btn btn-success back-to-top position-fixed';
    backToTop.style.cssText = 'bottom: 20px; right: 20px; z-index: 1000; display: none; width: 45px; height: 45px; border-radius: 50%;';
    document.body.appendChild(backToTop);

    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    });

    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});
