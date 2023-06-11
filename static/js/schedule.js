function updateCreateModal(trainingID, specificTimeTrainingDate){
  $("#createModal #trainingID").val( trainingID ); 
  $("#createModal #specificTimeTrainingDate").val( specificTimeTrainingDate ); 
}

function updateDeleteModal(trainingID, specificTimeTrainingDate){
  $("#deleteModal #trainingID").val( trainingID ); 
  $("#deleteModal #specificTimeTrainingDate").val( specificTimeTrainingDate ); 
}


function validateForm() {
  var selectValue = document.getElementById("cancelForm").value;
  if (selectValue === "") {
    alert("Please choose an option");
    return false;
  }
  return true;
}