document.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("scanBtn");

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

                // ✅ SHOW RESULT IN UI
                document.getElementById("result").innerText =
                    "Result: " + data.result;

                document.getElementById("confidence").innerText =
                    "Confidence: " + (data.confidence * 100).toFixed(2) + "%";

                // 🎨 OPTIONAL COLOR
                if (data.result === "phishing") {
                    document.getElementById("result").style.color = "red";
                } else {
                    document.getElementById("result").style.color = "green";
                }

            })
            .catch(err => console.error(err));
        });

    });

});