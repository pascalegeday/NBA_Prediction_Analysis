// Get the container element
var navbarOptions = document.getElementById("navbar-options");

// Get all buttons with class="btn" inside the container
var anchors = navbarOptions.getElementsByClassName("nav-link");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < anchors.length; i++) {
    anchors[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}
