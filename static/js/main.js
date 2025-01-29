function check_me(input_id) {
    // Select the checkbox input and label using the provided input_id
    var checked_input = document.querySelector("input[id='" + input_id + "']");
    var checked_label = document.querySelector("label[for='" + input_id + "']");

    // Apply line-through style if the checkbox is checked, remove it otherwise
    if (checked_input.checked) {
        checked_label.style.textDecoration = "line-through";
    } else {
        checked_label.style.textDecoration = "";
    }

    // Select the remove button
    var btn = document.getElementById("remove_btn");

    // Change the button's appearance and text when a checkbox is clicked
    btn.value = "REMOVE ITEMS";
    btn.style.color = "#FFFFFF"; // White text color
    btn.style.backgroundColor = "#FE7575"; // Red background color
    btn.style.cursor = "pointer"; // Pointer cursor to indicate it's clickable
}
