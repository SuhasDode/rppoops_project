const radioButtons = document.querySelectorAll('.app_mess_radio');

const input_Field = document.querySelector("div.form-group.col-md-6.mess_token");
// Loop through each radio button and add a click event listener
radioButtons.forEach(radioButton => {
    radioButton.addEventListener('click', function() {
        // Get the value of the clicked radio button
        const checkedValue = this.value;
        if(checkedValue == 'option1'){
            input_Field.style.display = 'block';
            // inputField.setAttribute('','required');
        }
        else{
            input_Field.style.display = 'none';
        }
    });
});

const inputField1 = document.getElementById('mess_app1');

// Function to toggle the 'required' attribute based on a condition
function toggleRequired(isRequired) {
    if (isRequired) {
        inputField1.setAttribute('required', 'required'); // Set the attribute name to 'required'
    } else {
        inputField1.removeAttribute('required');
    }
}

// Example usage: Toggle the 'required' attribute based on the value of the radio button
document.querySelectorAll('.app_mess_radio').forEach(radioButton => {
    radioButton.addEventListener('click', function() {
        const isChecked = this.value === 'option1'; // Change condition as per your requirement
        toggleRequired(isChecked);
    });
});