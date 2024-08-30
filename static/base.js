let userMenu = document.getElementById('user-menu');
let userInfo = document.getElementById('user-info');
let userMenuArrow = document.getElementById('user-menu-arrow');

// Toggle the display of the user's actions menu
function userMenuDisplay(){
    // Display if it's currently hidden
    if(userMenu.classList.contains("hidden")){
        userMenu.classList.remove("hidden");
        // Replace the down arrow with an up arrow.
        userMenuArrow.classList.remove('fa-chevron-down');
        userMenuArrow.classList.add("fa-chevron-up");
    // Hide if it's currently displayed
    }else{
        hideUserMenu();
    }
}

// Hide the user's actions menu
function hideUserMenu(){
    userMenu.classList.add("hidden");
    // Replace the up arrow with an down arrow
    userMenuArrow.classList.remove('fa-chevron-up');
    userMenuArrow.classList.add("fa-chevron-down");
}

// Add a click event listener to the document to hide the user's
// actions menu when the user clicks anywhere outside it
document.addEventListener('click', function(event) {
    // Check if the click was outside the user menu and the user's info
    if (!userMenu.contains(event.target) && !userInfo.contains(event.target)) {
        hideUserMenu();
    }
});