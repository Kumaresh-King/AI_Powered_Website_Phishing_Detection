console.log("Background script running 🚀");
let allowList = {};

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {

    if (changeInfo.status === "complete" && tab.url) {
        console.log("Scanning URL:", tab.url);

        if (
            tab.url.startsWith("chrome://") ||
            tab.url.startsWith("edge://") ||
            tab.url.startsWith("about:") ||
            tab.url.startsWith("chrome-extension://")
        ) return;

        if (allowList[tab.url]) return;

        fetch("https://ai-powered-website-phishing-detection.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url:  "http://fake-paypal-login-secure.com" })

        })
        .then(res => res.json())
        .then(data => {
            if (data.result === "phishing") {

                let blockedURL = encodeURIComponent(tab.url);

                chrome.tabs.update(tabId, {
                    url: chrome.runtime.getURL("warning.html") + "?blocked=" + blockedURL
                });
            }
        })
        .catch(err => console.error("API ERROR:", err));
    }
});