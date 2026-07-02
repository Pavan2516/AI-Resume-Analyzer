// ==========================================
// Theme Toggle (Dark / Light Mode)
// ==========================================

const themeBtn = document.getElementById("themeBtn");

// Load saved theme
if (localStorage.getItem("theme") === "light") {
    document.body.classList.add("light");
    if (themeBtn) {
        themeBtn.innerHTML = "☀️ Light Mode";
    }
}

// Theme button click
if (themeBtn) {

    themeBtn.addEventListener("click", function () {

        document.body.classList.toggle("light");

        if (document.body.classList.contains("light")) {

            localStorage.setItem("theme", "light");

            themeBtn.innerHTML = "☀️ Light Mode";

        } else {

            localStorage.setItem("theme", "dark");

            themeBtn.innerHTML = "🌙 Dark Mode";

        }

    });

}


// ==========================================
// File Upload Validation
// ==========================================

const fileInput = document.getElementById("resume");

if (fileInput) {

    fileInput.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) return;

        // Check PDF
        if (file.type !== "application/pdf") {

            alert("Please upload only PDF files.");

            this.value = "";

            return;

        }

        // Maximum Size 5MB
        if (file.size > 5 * 1024 * 1024) {

            alert("File size should be less than 5 MB.");

            this.value = "";

            return;

        }

        alert("Selected File: " + file.name);

    });

}


// ==========================================
// Animate Progress Bars
// ==========================================

window.addEventListener("load", function () {

    const bars = document.querySelectorAll(".progress-bar");

    bars.forEach(bar => {

        const width = bar.style.width;

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.width = width;

        }, 300);

    });

});


// ==========================================
// Score Circle Animation
// ==========================================

window.addEventListener("load", function () {

    const score = document.querySelector(".score-circle");

    if (score) {

        score.style.transform = "scale(0)";

        setTimeout(() => {

            score.style.transition = "0.8s";

            score.style.transform = "scale(1)";

        }, 200);

    }

});


// ==========================================
// Card Fade Animation
// ==========================================

window.addEventListener("load", function () {

    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform = "translateY(20px)";

        setTimeout(() => {

            card.style.transition = "0.6s";

            card.style.opacity = "1";

            card.style.transform = "translateY(0)";

        }, index * 150);

    });

});


// ==========================================
// Button Hover Effect
// ==========================================

const buttons = document.querySelectorAll("button, .btn");

buttons.forEach(button => {

    button.addEventListener("mouseenter", function () {

        this.style.transform = "scale(1.05)";

    });

    button.addEventListener("mouseleave", function () {

        this.style.transform = "scale(1)";

    });

});


// ==========================================
// Console Message
// ==========================================

console.log("AI Resume Analyzer Loaded Successfully!");