// Type of view buttons
let classicView = document.getElementById("classic");
let graphView = document.getElementById("graph");

// HTML elements for each type of view
let graph = document.getElementById("graphContainer");
let graphErrorMessage = document.getElementById("graph-error-message");
let classic = document.getElementById("classic-display");
let question = document.getElementById("question-text")

// List view
function classicSelected(){
    // Mark button as selected
    classicView.classList.add('selected');
    graphView.classList.remove('selected');

    // Hide graph and display list view
    graph.classList.add('hidden');
    graphErrorMessage.classList.add('hidden');
    classic.classList.remove('hidden');
}

// Graph view
function graphSelected(){
    // Mark button as selected
    classicView.classList.remove('selected');
    graphView.classList.add('selected');
    
    // Hide list view
    classic.classList.add('hidden');
    
    // If the datapoints are not empty (total votes > 0)
    if(Object.keys(datapoints).length > 0){
        // Display graph
        graph.classList.remove('hidden');
    } else{
        // Display error message
        graphErrorMessage.classList.remove('hidden');
    }
    
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