window.onload = function() {
    const fadeInImg = document.getElementById("hi-img");    
    const fadeInMessage = document.getElementById("other-welcome-message");
    
    fadeInImg.style.opacity = 1;
    fadeInImg.style.transform = "translateY(0)";
    
    setTimeout(function() {
        fadeInMessage.style.opacity = 1;
        fadeInImg.style.transform = "translateY(0)";
      }, 3500);
    
};

const observer = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
        if (entry.isIntersecting){
            const fadeInCard = entry.target.querySelector('.fadeInCard');
            const fadeFPCardOne = entry.target.querySelector('.fade-fp-card-1');
            fadeInCard.style.opacity = 1;
            fadeInCard.style.transform = 'translateY(0)';

            setTimeout(function() {
                fadeFPCardOne.style.opacity = 1;
                fadeFPCardOne.style.transform = "translateY(0)";
              }, 2500);
        }
    });
}, {
    threshold: 0.5
});

const sections = document.querySelectorAll('section');
sections.forEach(function(section){
    observer.observe(section);
});