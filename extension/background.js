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

        // ✅ CHECK IF USER ALLOWED THIS URL
        if (allowList[tab.url]) {
            console.log("Allowed by user:", tab.url);
            return;
        }

        fetch("https://ai-powered-website-phishing-detection.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: tab.url })
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
        .catch(err => console.error(err));
    }
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    if (message.action === "allow_url") {

        allowList[message.url] = true;

        console.log("User allowed:", message.url);

        // OPTIONAL: remove after 1 minute
        setTimeout(() => {
            delete allowList[message.url];
            console.log("Removed from allow list:", message.url);
        }, 60000);
    }

});
let currentURL = window.location.href;

fetch("https://ai-powered-website-phishing-detection.onrender.com/predict", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ url: currentURL })
})
.then(response => response.json())
.then(data => {

    if (data.result === "phishing") {

        chrome.storage.local.set({ blockedURL: currentURL });

        chrome.tabs.update({
            url: chrome.runtime.getURL("warning.html")
        });
    }

})
.catch(error => {
    console.error("API Error:", error);
});