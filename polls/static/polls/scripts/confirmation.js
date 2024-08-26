// Copy the code and manage the copy message
function copyCode(){
    let code = document.getElementById("code").innerHTML;
    navigator.clipboard.writeText(code);

    var tooltip = document.getElementById("myTooltipCode");
    tooltip.innerHTML = "Copied!";
}

// Reset copy  button text when the mouse is out
function copyCodeOut() {
    var tooltip = document.getElementById("myTooltipCode");
    tooltip.innerHTML = "Copy";
}


// Copy the link and manage the copy message
function copyLink(){
    let link = document.getElementById("link").innerHTML;
    navigator.clipboard.writeText(link);

    var tooltip = document.getElementById("myTooltipLink");
    tooltip.innerHTML = "Copied!";
}

// Reset copy  button text when the mouse is out
function copyLinkOut() {
    var tooltip = document.getElementById("myTooltipLink");
    tooltip.innerHTML = "Copy";
}