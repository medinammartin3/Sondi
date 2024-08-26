// Type of view buttons
let classicView = document.getElementById("classic");
let graphView = document.getElementById("graph");

// HTML elements for each type of view
let graph = document.getElementById("graphContainer");
let classic = document.getElementById("classic-display");
let question = document.getElementById("question-text")

// List view
function classicSelected(){
    // Mark button as selected
    classicView.classList.add('selected');
    graphView.classList.remove('selected');

    // Hide graph
    graph.classList.add('hidden');
    classic.classList.remove('hidden');
}

// Graph view
function graphSelected(){
    // Mark button as selected
    classicView.classList.remove('selected');
    graphView.classList.add('selected');

    // Hide list view
    graph.classList.remove('hidden');
    classic.classList.add('hidden');
}


// Graph configuration
window.onload = function () {
    var graph = new CanvasJS.Chart("graphContainer", {
        theme: "light2",
        animationEnabled: true,
        title:{
            text: question.textContent
        },
        data: [{
            type: "pie",
            startAngle: -90,
            yValueFormatString: "#,###'%'",
            dataPoints: datapoints
        }]
    });
    graph.render();
}