document.getElementById("textForm").addEventListener("submit", function() {
    document.getElementById("loading").classList.remove("hidden");
});
document.getElementById("loading").addEventListener("htmx:afterRequest", function() {
    const animation = lottie.loadAnimation({
        container: document.getElementById('lottie-animation'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: 'https://assets10.lottiefiles.com/packages/lf20_knu8q3vm.json'
    });
    animation.destroy();
    document.getElementById("loading").classList.add("hidden");
});