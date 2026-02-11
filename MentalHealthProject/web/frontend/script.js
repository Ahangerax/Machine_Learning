// frontend/script.js

const form = document.getElementById("predictionForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    // Collect form data
    const formData = new FormData(form);

    const data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Convert Age to number
    data["Age"] = Number(data["Age"]);

    try {

        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.error) {
            resultDiv.innerHTML = "Error: " + result.error;
            resultDiv.className = "danger";
            return;
        }

        resultDiv.innerHTML = "Prediction: " + result.result;

        if (result.result === "Depressed") {
            resultDiv.className = "danger";
        } else {
            resultDiv.className = "success";
        }

    } catch (error) {
        resultDiv.innerHTML = "Server not reachable";
        resultDiv.className = "danger";
    }

});
