const seats = document.getElementsByClassName('seat');
debugger;
const bookedSeats = {{ existing_seats }}; // Example of previously booked seats

function toggleSeatSelection() {
  if (this.classList.contains('selected')) {
    this.classList.remove('selected');
  } else {
    this.classList.add('selected');
  }
}
for (let i = 0; i < seats.length; i++) {

  const seatNumber = Number(seats[i].dataset.seatNumber);
  seats[i].addEventListener('click', toggleSeatSelection);

  if (bookedSeats.includes(seatNumber)) {
    seats[i].classList.add('booked');
    seats[i].removeEventListener('click', toggleSeatSelection);
  }
}

function generateFields() {
  const selectedSeats = document.getElementsByClassName('selected');
  const seatNumbers = [];
  console.log(selectedSeats)
  for (let i = 0; i < selectedSeats.length; i++) {
    seatNumbers.push(selectedSeats[i].dataset.seatNumber);
  }
  var numSeats = seatNumbers.length;
  var passengerFields = document.getElementById("passenger_fields");
  passengerFields.innerHTML = ""; // Clear previous fields (if any)
  for (var i = 1; i <= numSeats; i++) {
    var nameField = document.createElement("input");
    nameField.type = "text";
    nameField.id = "name_" + i;
    nameField.name = "name_" + i;
    nameField.placeholder = "Passenger " + i + " name";
    nameField.required = true;
    nameField.class = 'form-control'
    nameField.appendChild(document.createElement("br"));

    var ageField = document.createElement("input");
    ageField.type = "number";
    ageField.id = "age_" + i;
    ageField.name = "age_" + i;
    ageField.placeholder = "Passenger " + i + " age";
    ageField.required = true;
    ageField.class = 'form-control'
    ageField.appendChild(document.createElement("br"));

    var genderField = document.createElement("select");
    genderField.id = "gender_" + i;
    genderField.name = "gender_" + i;
    genderField.required = true;
    genderField.class = 'dropdown-menu'
    genderField.appendChild(document.createElement("br"));

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
function saveSelectedSeats() {
  debugger;
  const selectedSeats = document.getElementsByClassName('selected');
  console.log(selectedSeats)
  const seatNumbers = [];
  for (let i = 0; i < selectedSeats.length; i++) {
    seatNumbers.push(selectedSeats[i].dataset.seatNumber);
  }
  console.log(seatNumbers)
  var busId = {{ bus_id | safe }};// Replace with the actual bus ID
const csrftoken = Cookies.get('csrftoken');

const names = []
const ages = []
const genders = []
var numSeats = seatNumbers.length;
for (var i = 1; i <= numSeats; i++) {
  var pass_name = document.getElementById("name_" + i).value;
  var pass_age = document.getElementById("age_" + i).value;
  var pass_gender = document.getElementById("gender_" + i).value;
  names.push(pass_name)
  ages.push(pass_age)
  genders.push(pass_gender)
}
console.log(names, ages, genders)
// Use jQuery to send a POST request with the selected seat numbers
$.ajax({
  url: '/seat/',
  type: 'POST',
  data: {
    bus_id: busId,
    seat_numbers: seatNumbers,
    name: names,
    age: ages,
    gender: genders,
    csrfmiddlewaretoken: csrftoken
  },
  dataType: 'json',
  success: function (response) {
    window.location.href = '/';
    console.log('Selected seats saved successfully.');
  },
  error: function (xhr, status, error) {
    console.error('Error saving selected seats:', error);
  }
});
}

