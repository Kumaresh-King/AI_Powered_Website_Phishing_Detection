const params = new URLSearchParams(window.location.search);
const blockedURL = decodeURIComponent(params.get("blocked") || "");

document.getElementById("urlText").innerText = blockedURL;

let risk = Math.floor(Math.random() * 40) + 60;
document.getElementById("riskScore").innerText = risk + "%";

function goBack() {
    window.location.href = "https://www.google.com";
}

function proceedAnyway() {

    // ✅ Tell background to allow this URL
    chrome.runtime.sendMessage({
        action: "allow_url",
        url: blockedURL
    });

    // Open site
    window.location.href = blockedURL;
}

document.getElementById("safeBtn").addEventListener("click", goBack);
document.getElementById("unsafeBtn").addEventListener("click", proceedAnyway);