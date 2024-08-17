let labels = document.querySelectorAll("label");

labels.forEach(label => {
    label.remove()
});



let title = document.getElementById("public-questions-topic-title");

let most_recent_button = document.getElementById("most-recent");
let most_voted_button = document.getElementById("most-voted");
let trending_button = document.getElementById("trending");
let random_button = document.getElementById("random");

let most_recent_questions = document.getElementById("most-recent-questions")
let most_voted_questions = document.getElementById("most-voted-questions")
let trending_questions = document.getElementById("trending-questions")
let random_questions = document.getElementById("random-questions")

function mostRecentSelected(){
    most_recent_button.classList.add('selected');
    most_voted_button.classList.remove('selected');
    trending_button.classList.remove('selected');
    random_button.classList.remove('selected');

    title.innerHTML = "Polls created recently:";

    most_recent_questions.classList.remove('hidden');
    most_voted_questions.classList.add('hidden');
    trending_questions.classList.add('hidden');
    random_questions.classList.add('hidden');
}

function mostVotedSelected(){
    most_voted_button.classList.add('selected');
    most_recent_button.classList.remove('selected');
    trending_button.classList.remove('selected');
    random_button.classList.remove('selected');

    title.innerHTML = "Most voted polls:";

    most_voted_questions.classList.remove('hidden');
    most_recent_questions.classList.add('hidden');
    trending_questions.classList.add('hidden');
    random_questions.classList.add('hidden');
}

function trendingSelected(){
    trending_button.classList.add('selected');
    most_recent_button.classList.remove('selected');
    most_voted_button.classList.remove('selected');
    random_button.classList.remove('selected');

    title.innerHTML = "Popular polls right now:";

    trending_questions.classList.remove('hidden');
    most_recent_questions.classList.add('hidden');
    most_voted_questions.classList.add('hidden');
    random_questions.classList.add('hidden');
}

function randomSelected(){
    random_button.classList.add('selected');
    most_recent_button.classList.remove('selected');
    most_voted_button.classList.remove('selected');
    trending_button.classList.remove('selected');

    title.innerHTML = "Randomly selected polls:";

    random_questions.classList.remove('hidden');
    most_recent_questions.classList.add('hidden');
    most_voted_questions.classList.add('hidden');
    trending_questions.classList.add('hidden');
}