let currentURL = window.location.href;

fetch("http://127.0.0.1:5000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ url: currentURL })
})
.then(response => response.json())
.then(data => {

  console.log("Prediction:", data);

  if(data.result === "phishing"){
      alert("⚠ WARNING: This website may be a phishing site!");
  }

})
.catch(error => console.log("Error:", error));