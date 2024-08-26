// Disable the back button when the vote is submitted
function DisableBackButton(){
    window.history.forward()
}

window.onload = DisableBackButton();
window.onpageshow = function(evt) { if (evt.persisted) DisableBackButton() }