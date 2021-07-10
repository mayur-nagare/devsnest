let seats = 0;
const rectangles = document.querySelectorAll(".box");
Array.from(rectangles).forEach((box) => {
  box.addEventListener("click", () => {
    let result = box.classList.toggle("active");
    if (result) seats++;
    else seats--;
    document.querySelector(".bs").innerHTML = "Booked Seats : " + seats;
    const remaining = (document.querySelector(".rs").innerHTML =
      "Remaining Seats : " + (34 - seats));
  });
});
