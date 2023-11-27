let card = document.querySelectorAll(".card");
let BW = document.getElementById("BW");
let Color = document.getElementById("Color");
let checkCol = document.getElementById("checkCol");
let checkBW = document.getElementById("checkBW");
// checkBW.style.display = "none";
// checkCol.style.display = "none";
let cardBw = card[0];
let cardCol = card[1];

// let BwClicked = false;
// let ColClicked = false;

// cardBw.addEventListener("click", () => {
//     BW.classList.remove("card-heading");
//     BW.classList.add("card-headingS");
//     checkBW.classList.remove("hide");
//     checkBW.classList.add("show");

// });

// cardCol.addEventListener("click", () => {
//     Color.classList.remove("card-heading");
//     Color.classList.add("card-headingS");
//     checkCol.classList.remove("hide");
//     checkCol.classList.add("show");
// });

let TypeInputs = document.querySelectorAll('input[name="ColorType"]');

TypeInputs.forEach((input) => {
  input.addEventListener("change", (event) => {
    // Reset styles for both options
    Color.classList.remove("card-headingS");
    BW.classList.remove("card-headingS");
    checkCol.classList.add("hide");
    checkCol.classList.remove("show");
    checkBW.classList.add("hide");
    checkBW.classList.remove("show");

    if (event.target.checked) {
      type = event.target.value;
      if (type === "B&W") {
        BW.classList.add("card-headingS");
        checkBW.classList.remove("hide");
        checkBW.classList.add("show");
      } else if (type === "Color") {
        Color.classList.add("card-headingS");
        checkCol.classList.remove("hide");
        checkCol.classList.add("show");
      }
    }
  });
});

let orientationInputs = document.querySelectorAll('input[name="orientation"]');
// console.log(orientationInputs);

orientationInputs.forEach((input) => {
  input.addEventListener("change", (event) => {
    // Reset styles for all labels
    document.querySelectorAll('.checks label').forEach(label => {
      label.style.color = ''; // Reset to default color
    });

    if (event.target.checked) {
      const selectedLabel = document.querySelector(`label[for="${event.target.id}"]`);
      if (selectedLabel) {
        selectedLabel.style.color = '#fff';
      }
    }
  });
});
