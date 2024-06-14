function navigateSection(event, sectionName) {
    var i, sections;

    // Prevent default anchor behavior
    event.preventDefault();

    // Hide all sections
    sections = document.getElementsByClassName("form-section");
    for (i = 0; i < sections.length; i++) {
        sections[i].classList.remove("active");
    }

    // Show the current section
    var currentSection = document.getElementById(sectionName);
    currentSection.classList.add("active");
}

// Set the default active section
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("standard_section").classList.add("active");
});
