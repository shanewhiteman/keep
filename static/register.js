function showElement(elementId) {
    let element = document.getElementById(elementId);
    element.style.display = "block";
};

document.addEventListener("DOMContentLoaded", function(event) {
    let passwordInput = document.getElementById("password");

    passwordInput.onclick = function() {
        showElement('password-requirements');
    };
});