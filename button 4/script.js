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

kleuren = ["red", "purple", "blue"]

for (let i = 0; i < 30; i++) {
    const button = document.createElement("button")
    button.textContent = i + 1

    button.style.backgroundColor = "green"
    button.style.color = "black"
    button.style.margin = "5px"
    button.style.padding = "20px"
    button.style.fontSize = "18px"
    
    let kleurIndex = 0


    button.addEventListener("click", () => {
        if (kleurIndex < kleuren.length) {
            button.style.backgroundColor = kleuren[kleurIndex];
            kleurIndex++;
        } else if (button.style.backgroundColor !== "black") {
            button.style.backgroundColor = "black";
        } else {
            button.remove();
        }
    });
    container.appendChild(button)
}