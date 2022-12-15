// show hidden elements
function showElement(elementId) {
    let element = document.getElementById(elementId);
    element.style.display = "block";
};

function checkPassRequirementRegex(regex, reqClass) {
    const exclamation_img = "url(https://user-images.githubusercontent.com/31552294/207744447-45d4124c-ce11-4cbb-b038-2e3fbdadaa2a.svg)";
    const checkmark_img = "url(https://user-images.githubusercontent.com/31552294/207744453-e004b26e-a8cb-47fc-bbea-c4a291ee75e6.svg)";

    const passwordInput = document.getElementById("password");

    if (passwordInput.value.match(regex)) {
        changePassRequirementImage(checkmark_img, reqClass);
    } else {
        changePassRequirementImage(exclamation_img, reqClass);
    };
};

// change password "minimum requirements" bullet point images based on form input
function changePassRequirementImage(image, reqClass) {
    let element = document.querySelector(reqClass);
    element.style.backgroundImage = image;
};

document.addEventListener("DOMContentLoaded", function(event) {
    const passwordInput = document.getElementById("password");

    passwordInput.onclick = function() {
        showElement('password-requirements');
    };
});

document.addEventListener("input", function(event) {
    // password minimum requirement classes
    const requirementEight = '.requirement-eight';
    const requirementNum = '.requirement-number';
    const requirementUpper = '.requirement-upper';
    const requirementLower = '.requirement-lower';
    const requirementSpecial = '.requirement-special';

    // regex for minimum requirements
    const req_min_char_length = /^.{8,}$/;
    const req_min_num = /^(?=.*\d)/;
    const req_min_upper = /^(?=.*[A-Z])/;
    const req_min_lower = /^(?=.*[a-z])/;
    const req_min_special = /^(?=.*[@$!%*?&])/;

    checkPassRequirementRegex(req_min_char_length, requirementEight);
    checkPassRequirementRegex(req_min_num, requirementNum);
    checkPassRequirementRegex(req_min_upper, requirementUpper);
    checkPassRequirementRegex(req_min_lower, requirementLower);
    checkPassRequirementRegex(req_min_special, requirementSpecial);
});