document.addEventListener('DOMContentLoaded', function() {
    const yesRadio = document.getElementById('refi_yes');
    const noRadio = document.getElementById('refi_no');
    const conditionalInput = document.getElementById('refinance-inputs');
    const refi_interest_input = document.getElementById('refi_interest');
    const refi_loan_duration_input = document.getElementById('refi_loan_duration');
    const refi_start_date_input = document.getElementById('refi_start_date');

    function radioDependentFields() {
        if (yesRadio.checked) {
          conditionalInput.style.display = 'block';
          refi_interest_input.required = true;
          refi_loan_duration_input.required = true;
          refi_start_date_input.required = true;
        } else {
          conditionalInput.style.display = 'none';
          refi_interest_input.required = false;
          refi_loan_duration_input.required = false;
          refi_start_date_input.required = false;
        }
      }
    
      yesRadio.addEventListener('change', radioDependentFields);
      noRadio.addEventListener('change', radioDependentFields);
  
      // Ensure the correct state on page load
      radioDependentFields();
});