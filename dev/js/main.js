document.addEventListener("DOMContentLoaded", function () {

    // ================== Header Navbar ==================
    // ================== Burger Button ==================
    // ===================================================
    const navbar = document.querySelector(".sidenav");
    const burgerButton = document.querySelector(".burger-button");
    burgerButton.toggle = () => {
        burgerButton.classList.toggle("burger-button__selected");

    }

    const navbarInstance = M.Sidenav.init(navbar, {
        edge: "left",
        draggable: false,
        onOpenStart: burgerButton.toggle,
        onCloseStart: burgerButton.toggle
    });

    burgerButton.onclick = () => {
        if (navbarInstance.isOpen) navbarInstance.close();
        else navbarInstance.open();
    };

    window.onresize = () => {
        if (window.innerWidth > 992) navbarInstance.close();
    }



    // ================= Carousel Slider =================
    // ===================================================
    
    const carousel = document.querySelector('.carousel');
    const carouselInstance = M.Carousel.init(carousel, {
        dist: 0,
        padding: 0,
        fullWidth: false,
        indicators: true,
        duration: 100,
    });

    setInterval(() => {
        carouselInstance.next();
    }, 5500);

    
    // ================= Parallax Effect =================
    // ===================================================
    const parallax = document.querySelectorAll('.parallax');
    var parallaxInstance = M.Parallax.init(parallax, {});

});