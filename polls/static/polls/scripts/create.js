// TODO: Fix bug when the first choice form is deleted,
// error messages are displayed even if theres two choices added

window.onload = function(){
    removeLabels();
    updateDeleteButtons();
    DisableBackButton();
}

window.onpageshow = function(evt) { if (evt.persisted) DisableBackButton() }



// Choices form elements
let choiceForm = document.querySelectorAll(".choice-form");
let container = document.querySelector("#form-container");
let addButton = document.querySelector("#add-button");
let deleteButtons = document.querySelectorAll(".delete-button");
let totalForms = document.querySelector;("#id_form-TOTAL_FORMS");

let formNum = choiceForm.length - 1; // Current number of choice forms displayed

// Add event listeners to the add and delete buttons 
// to detect when a choice form is added or deleted
addButton.addEventListener('click', addForm);
deleteButtons.forEach(deleteButton =>{
    deleteButton.addEventListener('click', deleteForm);
});

// Add a new choice form
function addForm(event) {
    event.preventDefault();

    let newForm = choiceForm[0].cloneNode(true); // Clone the choice form
    let formRegex = RegExp(`form-(\\d){1}-`,'g'); // Regex to find all instances of the form number

    formNum++; // Increment the form number for the new form
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`); // Update the new form with the correct form number
    container.insertBefore(newForm, addButton); // Insert the new form at the end of the list of forms

    totalForms.value = `${formNum + 1}`; // Update the total number of forms in the management form

    // Add event listener to the delete button of the new form
    deleteButtons = document.querySelectorAll(".delete-button");
    deleteButtons[deleteButtons.length - 1].addEventListener('click', deleteForm)

    updateDeleteButtons();
    removeLabels();
}


// Delete a choice form
function deleteForm(event){
    event.preventDefault();

    let parentDiv = event.target.closest('.choice-form'); // Form we want to remove
    parentDiv.remove();

    formNum--; // Decrement the current number of forms
    totalForms.value = `${formNum + 1}`; // Update the total number of forms in the management form

    // Update the id of all remaining choice forms to maintain correct sequence
    let forms = document.querySelectorAll(".choice-form");
    forms.forEach((form, index) => {
        let input = form.querySelector('input');
        input.id= `id_form-${index}-choice_text`
    });

    updateDeleteButtons();
    removeLabels();
}


// Update the delete buttons to enable/disable them based on the number of choice forms
function updateDeleteButtons(){
    let deleteButtons = document.querySelectorAll(".delete-button");
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




// Remove all django default form labels, except those related to visibility
function removeLabels(){
    let labels = document.querySelectorAll("label");
    labels.forEach(label => {
        if(label.getAttribute('for') && label.getAttribute('for').includes('visibility')){
            return;
        }
        label.remove();
    });
}




// Disable the back button when the poll is created
function DisableBackButton(){
    window.history.forward();
}




// Get help message HTML element
let helpMessage = document.getElementById("help-message");


// Toggle the display of the help message when the help button is clicked
function openHelpMessage(){
    // Display the help message if it's currently hidden
    if(helpMessage.classList.contains("hidden")){
        helpMessage.classList.remove("hidden");
    // Hide the help message if it's currently displayed
    }else{
        helpMessage.classList.add("hidden");
    }
}


// Hide the help message when the close button is clicked
function closeHelpMessage(){
    helpMessage.classList.add("hidden");
}