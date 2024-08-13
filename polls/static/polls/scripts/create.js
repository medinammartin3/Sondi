let choiceForm = document.querySelectorAll(".choice-form");
let container = document.querySelector("#form-container");
let addButton = document.querySelector("#add-button");
let deleteButtons = document.querySelectorAll(".delete-button");
let totalForms = document.querySelector;("#id_form-TOTAL_FORMS");

let formNum = choiceForm.length - 1;

addButton.addEventListener('click', addForm);
deleteButtons.forEach(deleteButton =>{
    deleteButton.addEventListener('click', deleteForm);
});

removeLabels();

function addForm(event) {
    event.preventDefault();

    let newForm = choiceForm[0].cloneNode(true); //Clone the choice form
    let formRegex = RegExp(`form-(\\d){1}-`,'g'); //Regex to find all instances of the form number

    formNum++; //Increment the form number
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`); //Update the new form to have the correct form number
    container.insertBefore(newForm, addButton); //Insert the new form at the end of the list of forms

    totalForms.value = `${formNum + 1}`; //Increment the number of total forms in the management form

    // Add event listener to new form delete button
    deleteButtons = document.querySelectorAll(".delete-button");
    deleteButtons[deleteButtons.length - 1].addEventListener('click', deleteForm)

    updateDeleteButtons();
    removeLabels();
}

function deleteForm(event){
    event.preventDefault();

    let parentDiv = event.target.closest('.choice-form'); // Form we want to remove
    parentDiv.remove();

    formNum--;
    totalForms.value = `${formNum + 1}`;

    let forms = document.querySelectorAll(".choice-form");
    forms.forEach((form, index) => {
        let input = form.querySelector('input');
        input.id= `id_form-${index}-choice_text`
    });

    updateDeleteButtons();
    removeLabels();
}

function updateDeleteButtons(){
    if (formNum <= 1) {
        let deleteButtons = document.querySelectorAll(".delete-button");
        deleteButtons.forEach(button => {
            button.disabled = true;
        });
    }else{
        let deleteButtons = document.querySelectorAll(".delete-button");
        deleteButtons.forEach(button => {
            button.disabled = false;
        });
    }
}

function removeLabels(){
    let labels = document.querySelectorAll("label");
    labels.forEach(label => {
        label.remove()
    });
}

function DisableBackButton(){
    window.history.forward()
   }
   DisableBackButton();
   window.onload = DisableBackButton;
   window.onpageshow = function(evt) { if (evt.persisted) DisableBackButton() }
   window.onload = function() {void(0)}