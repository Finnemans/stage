const container = document.getElementById("container")
container.style.margin = "20px auto"
container.style.backgroundColor = "white"
container.style.padding = "20px"
container.style.margin = "0px auto"
container.style.width = "500px"
container.style.textAlign = "center"

container.style.display = "grid"
container.style.gridTemplateColumns = "repeat(5, 1fr)"
container.style.gap = "10px"

for (let i = 0; i < 30; i++) {
    const button = document.createElement("button")
    button.textContent = i + 1

    button.style.backgroundColor = "green"
    button.style.color = "black"
    button.style.margin = "5px"
    button.style.padding = "20px"
    button.style.fontSize = "18px"

   button.addEventListener("click", () => {
      if (button.style.backgroundColor === "red") {
         button.style.backgroundColor = "green";
      } else {
         button.style.backgroundColor = "red";
      }
   });
    container.appendChild(button)
}