let classicView = document.getElementById("classic");
let graphView = document.getElementById("graph");

let graph = document.getElementById("graphContainer");
let classic = document.getElementById("classic-display");
let question = document.getElementById("question-text")

function classicSelected(){
    classicView.classList.add('selected');
    graphView.classList.remove('selected');

    graph.classList.add('hidden');
    classic.classList.remove('hidden');
}

function graphSelected(){
    classicView.classList.remove('selected');
    graphView.classList.add('selected');

    graph.classList.remove('hidden');
    classic.classList.add('hidden');
}

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