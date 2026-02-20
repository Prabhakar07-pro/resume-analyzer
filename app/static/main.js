function goToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".top").style.display = "none";
});

window.addEventListener("scroll", function () {

    const button = document.querySelector(".top");

    const scrollPosition = window.scrollY;
    const pageHeight = document.documentElement.scrollHeight;
    const windowHeight = window.innerHeight;

    const halfwayPoint = (pageHeight - windowHeight) / 2;

    if (scrollPosition > halfwayPoint) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
});

function goToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}