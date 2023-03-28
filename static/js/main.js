window.onload = function() {
    const fadeInImg = document.getElementById("hi-img");
    const fadeInArrow = document.getElementById("arrow-down");
    
    fadeInImg.style.opacity = 1;
    fadeInImg.style.transform = "translateY(0)";
    
    setTimeout(function() {
        fadeInArrow.style.opacity = 1;
      }, 3500);
    
};
