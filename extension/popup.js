document.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("scanBtn");

    if (!btn) {
        console.error("Button not found!");
        return;
    }

    btn.addEventListener("click", () => {

        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {

            let url = tabs[0].url;

            fetch("https://ai-powered-website-phishing-detection.onrender.com/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ url: url })
            })
            .then(res => res.json())
            .then(data => {
                alert("Result: " + data.result);
            })
            .catch(err => console.error("API ERROR:", err));
        });

    });

});