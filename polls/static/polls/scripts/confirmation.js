function copyCode(){
    let code = document.getElementById("code").innerHTML;
    navigator.clipboard.writeText(code);

    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copied!";
}

function copyCodeOut() {
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copy";
}