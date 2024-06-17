document.addEventListener('DOMContentLoaded', function() {
    var dateInputs = document.querySelectorAll('input[name="start_date"], input[name="refi_start_date"]');
    dateInputs.forEach(function(dateInput) {
        dateInput.addEventListener('input', function() {
                var regex = /^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{4}$/;
            if (!regex.test(dateInput.value)) {
                dateInput.setCustomValidity('Please enter a date in the format MM/DD/YYYY');
            } else {
                dateInput.setCustomValidity('');
            }
        });
    });
});