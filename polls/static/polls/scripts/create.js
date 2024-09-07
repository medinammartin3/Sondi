window.onload = function(){
    updateDeleteButtons();
    DisableBackButton();
}

window.onpageshow = function(evt) { if (evt.persisted) DisableBackButton() }



// Choices form elements
let choiceForm = document.querySelectorAll(".choice-form");
let container = document.querySelector("#form-container");
let addButton = document.querySelector("#add-button");
let totalForms = document.querySelector("#id_form-TOTAL_FORMS");

let formNum = choiceForm.length - 1; // Current number of choice forms displayed

// Add event listener to the add button
addButton.addEventListener('click', addForm);


// Add a new choice form
function addForm(event) {
    event.preventDefault();

    let newForm = choiceForm[0].cloneNode(true); // Clone the choice form
    let formRegex = RegExp(`form-(\\d){1}-`,'g'); // Regex to find all instances of the form number

    formNum++; // Increment the form number for the new form
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`); // Update the new form with the correct form number
    container.insertBefore(newForm, addButton); // Insert the new form at the end of the list of forms

    totalForms.value = `${formNum + 1}`; // Update the total number of forms in the management form

    updateDeleteButtons();
}


// Delete a choice form
function deleteForm(event){
    event.preventDefault();

    let parentDiv = event.target.closest('.choice-form'); // Form we want to remove
    parentDiv.remove();

    formNum--; // Decrement the current number of forms
    totalForms.value = `${formNum + 1}`; // Update the total number of forms in the management form

    // Update the id and name attributes of all remaining choice forms to maintain correct sequence
    let formRegex = RegExp(`form-(\\d){1}-`,'g'); // Regex to find all instances of the form number
    let forms = document.querySelectorAll(".choice-form");
    forms.forEach((form, index) => {
        // Get all input elements of each choice form
        let inputs = form.querySelectorAll('input')
        // Update manually the id and name attributes of each input to keep the introduced text
        inputs.forEach(input => {
            let name = input.getAttribute('name').replace(formRegex, `form-${index}-`);
            let id = input.getAttribute('id').replace(formRegex, `form-${index}-`);
            input.setAttribute('name', name);
            input.setAttribute('id', id);
        });
    });

    updateDeleteButtons();
}


// Add event listener to all delete buttons
// Update the delete buttons to enable/disable them based on the number of choice forms
function updateDeleteButtons(){
    let deleteButtons = document.querySelectorAll(".delete-button");

    // Add event listener to each button
    deleteButtons.forEach(deleteButton =>{
        deleteButton.addEventListener('click', deleteForm);
    });

    // If only two choice forms remain, disable their delete buttons
    if (formNum <= 1) {
        deleteButtons.forEach(button => {
            button.disabled = true;
        });
    // Otherwise, enable all delete buttons
    }else{
        deleteButtons.forEach(button => {
            button.disabled = false;
        });
    }
}




// Disable the back button when the poll is created
function DisableBackButton(){
    window.history.forward();
}



// Get help message HTML element
let helpMessage = document.getElementById("help-message");


// Toggle the display of the help message when the help button is clicked
function openHelpMessage(){
    // Display if it's currently hidden
    if(helpMessage.classList.contains("hidden")){
        helpMessage.classList.remove("hidden");
    // Hide if it's currently displayed
    }else{
        helpMessage.classList.add("hidden");
    }
}


// Hide the help message when the close button is clicked
function closeHelpMessage(){
    helpMessage.classList.add("hidden");
}