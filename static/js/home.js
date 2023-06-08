function validateForm() {
    var selectValue = document.getElementById("cancelForm").value;
    if (selectValue === "") {
      alert("Please choose an option");
      return false;
    }
    return true;
  }