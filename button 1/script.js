const container = document.getElementById("container")
container.style.margin = "20px auto"
container.style.backgroundColor = "white"
container.style.padding = "20px"
container.style.margin = "0px auto"
container.style.width = "300px"
container.style.textAlign = "center"

const kleuren = ["green", "red", "blue"]

for (let i = 0; i < kleuren.length; i++) {
    const button = document.createElement("button")
    button.textContent = "Knop " + (i + 1)

    button.style.backgroundColor = kleuren[i]
    button.style.color = "white"
    button.style.margin = "5px"

    button.addEventListener("click", () => {
        document.body.style.backgroundColor = kleuren[i]
    });
    
    container.appendChild(button)
}