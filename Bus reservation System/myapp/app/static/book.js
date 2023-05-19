
    function generateFields() {

      var numSeats = document.getElementById("no_seats").value;
      var passengerFields = document.getElementById("passenger_fields");
      passengerFields.innerHTML = ""; // Clear previous fields (if any)

      for (var i = 1; i <= numSeats; i++) {
        var nameField = document.createElement("input");
        nameField.type = "text";
        nameField.id = "name_" + i;
        nameField.name = "name_" + i;
        nameField.placeholder = "Passenger " + i + " name";
        nameField.required = true;

        var ageField = document.createElement("input");
        ageField.type = "number";
        ageField.id = "age_" + i;
        ageField.name = "age_" + i;
        ageField.placeholder = "Passenger " + i + " age";
        ageField.required = true;

        var genderField = document.createElement("select");
        genderField.id = "gender_" + i;
        genderField.name = "gender_" + i;
        genderField.required = true;

        var genderOption1 = document.createElement("option");
        genderOption1.value = "male";
        genderOption1.text = "Male";
        genderField.appendChild(genderOption1);

        var genderOption2 = document.createElement("option");
        genderOption2.value = "female";
        genderOption2.text = "Female";
        genderField.appendChild(genderOption2);

        var genderOption3 = document.createElement("option");
        genderOption3.value = "other";
        genderOption3.text = "Other";
        genderField.appendChild(genderOption3);

        passengerFields.appendChild(nameField);
        passengerFields.appendChild(ageField);
        passengerFields.appendChild(genderField);
        passengerFields.appendChild(document.createElement("br"));
      }
    }

    function submitForm(event) {
      event.preventDefault();
      debugger;

      var numSeats = document.getElementById("no_seats").value;
      var formData = [];

      for (var i = 1; i <= numSeats; i++) {
        var name = document.getElementById("name_" + i).value;
        var age = document.getElementById("age_" + i).value;
        var gender = document.getElementById("gender_" + i).value;

        formData.push({
          name: name,
          age: age,
          gender: gender
        });
      }
      debugger;
      console.log("Form data is "+formData);
      debugger;}



