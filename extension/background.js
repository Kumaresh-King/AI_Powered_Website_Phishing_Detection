let allowList = {};

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {

    if (changeInfo.status === "complete" && tab.url) {

        // Ignore internal pages
        if (
            tab.url.startsWith("chrome://") ||
            tab.url.startsWith("edge://") ||
            tab.url.startsWith("about:") ||
            tab.url.startsWith("chrome-extension://")
        ) return;

        // Skip allowed URLs
        if (allowList[tab.url]) return;

        console.log("🔍 Checking URL:", tab.url);

        fetch("https://ai-powered-website-phishing-detection.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: tab.url })
        })
        .then(res => res.json())
        .then(data => {

            console.log("✅ API RESULT:", data);

            if (data.result === "phishing") {

                console.log("🚨 PHISHING DETECTED");

                let blockedURL = encodeURIComponent(tab.url);

                chrome.tabs.update(tabId, {
                    url: chrome.runtime.getURL("warning.html") + "?blocked=" + blockedURL
                });
            }
        })
        .catch(err => console.error("❌ API ERROR:", err));
    }
});