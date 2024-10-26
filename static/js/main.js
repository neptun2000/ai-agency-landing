// Initialize Feather Icons
feather.replace();

// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.querySelectorAll('.fade-in').forEach((element) => {
    observer.observe(element);
});

// Contact form submission
const contactForm = document.getElementById('contactForm');
contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(contactForm);
    
    try {
        const response = await fetch('/submit_contact', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            alert('Message sent successfully!');
            contactForm.reset();
        } else {
            alert('Error sending message. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error sending message. Please try again.');
    }
});
