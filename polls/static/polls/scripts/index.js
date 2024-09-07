// Public polls list display by category

// List title
let title = document.getElementById("public-questions-topic-title");

// Categories buttons
let most_recent_button = document.getElementById("most-recent");
let most_voted_button = document.getElementById("most-voted");
let trending_button = document.getElementById("trending");
let random_button = document.getElementById("random");

// HTML code for each category
let most_recent_questions = document.getElementById("most-recent-questions")
let most_voted_questions = document.getElementById("most-voted-questions")
let trending_questions = document.getElementById("trending-questions")
let random_questions = document.getElementById("random-questions")

// Most recent polls
function mostRecentSelected(){
    // Mark button as selected
    most_recent_button.classList.add('selected');
    most_voted_button.classList.remove('selected');
    trending_button.classList.remove('selected');
    random_button.classList.remove('selected');

    // Change list title
    title.innerHTML = "Polls created recently:";

    // Hide all other lists
    most_recent_questions.classList.remove('hidden');
    most_voted_questions.classList.add('hidden');
    trending_questions.classList.add('hidden');
    random_questions.classList.add('hidden');
}

// Most voted polls
function mostVotedSelected(){
    // Mark button as selected
    most_voted_button.classList.add('selected');
    most_recent_button.classList.remove('selected');
    trending_button.classList.remove('selected');
    random_button.classList.remove('selected');

    // Change list title
    title.innerHTML = "Most voted polls:";

    // Hide all other lists
    most_voted_questions.classList.remove('hidden');
    most_recent_questions.classList.add('hidden');
    trending_questions.classList.add('hidden');
    random_questions.classList.add('hidden');
}

// Trending polls
function trendingSelected(){
    // Mark button as selected
    trending_button.classList.add('selected');
    most_recent_button.classList.remove('selected');
    most_voted_button.classList.remove('selected');
    random_button.classList.remove('selected');

    // Change list title
    title.innerHTML = "Popular polls right now:";

    // Hide all other lists
    trending_questions.classList.remove('hidden');
    most_recent_questions.classList.add('hidden');
    most_voted_questions.classList.add('hidden');
    random_questions.classList.add('hidden');
}

// Random polls
function randomSelected(){
    // Mark button as selected
    random_button.classList.add('selected');
    most_recent_button.classList.remove('selected');
    most_voted_button.classList.remove('selected');
    trending_button.classList.remove('selected');

    // Change list title
    title.innerHTML = "Randomly selected polls:";

    // Hide all other lists
    random_questions.classList.remove('hidden');
    most_recent_questions.classList.add('hidden');
    most_voted_questions.classList.add('hidden');
    trending_questions.classList.add('hidden');
}