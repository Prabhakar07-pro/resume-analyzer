document.addEventListener("DOMContentLoaded", function () {

    const button = document.querySelector(".top");

    // Hide initially
    button.style.display = "none";

    window.addEventListener("scroll", function () {

        if (window.scrollY > 250) {   // show after 300px scroll
            button.style.display = "block";
        } else {
            button.style.display = "none";
        }

    });

});

function goToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}