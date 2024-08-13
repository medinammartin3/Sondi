function copyCode(){
    let code = document.getElementById("code").innerHTML;
    navigator.clipboard.writeText(code);

    var tooltip = document.getElementById("myTooltipCode");
    tooltip.innerHTML = "Copied!";
}

function copyCodeOut() {
    var tooltip = document.getElementById("myTooltipCode");
    tooltip.innerHTML = "Copy";
}

function copyLink(){
    let link = document.getElementById("link").innerHTML;
    navigator.clipboard.writeText(link);

    var tooltip = document.getElementById("myTooltipLink");
    tooltip.innerHTML = "Copied!";
}

function copyLinkOut() {
    var tooltip = document.getElementById("myTooltipLink");
    tooltip.innerHTML = "Copy";
}