function validateForm() {
  var selectValue = document.getElementById("cancelForm").value;
  if (selectValue === "") {
    alert("Please choose an option");
    return false;
  }
  return true;
}

function send_mail() {  
  $.ajax({
    url: '/send_mail',
    type: 'POST',
    success: function() {
      // Handle success
      console.log('Cancellation request sent successfully.');
      // You can perform any additional actions here if needed
    },
    error: function() {
      // Handle error
      console.error('Failed to send cancellation request.');
      // You can display an error message or perform any additional error handling here
    }
  });
}