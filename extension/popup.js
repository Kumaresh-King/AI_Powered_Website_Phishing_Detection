document.getElementById("check").addEventListener("click", function(){

chrome.tabs.query({active:true,currentWindow:true}, function(tabs){

let url = tabs[0].url;

fetch("http://127.0.0.1:5000/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({url:url})

})

.then(response => response.json())

.then(data => {


})

.catch(error => {

document.getElementById("result").innerText="Server Offline"

})

})

})
document.getElementById("check").addEventListener("click", function(){

chrome.tabs.query({active:true,currentWindow:true}, function(tabs){

let url = tabs[0].url;

fetch("http://127.0.0.1:5000/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({url:url})

})

.then(response => response.json())

.then(data => {

let resultBox = document.getElementById("result")
let confidenceBox = document.getElementById("confidence")

if(data.result === "phishing"){

resultBox.innerHTML = "PHISHING WEBSITE"
resultBox.style.color = "red"

}else{

resultBox.innerHTML = "SAFE WEBSITE"
resultBox.style.color = "lime"

}

confidenceBox.innerHTML = "Confidence: " + data.confidence + "%"

})

.catch(error => {

document.getElementById("result").innerText="Server Offline"

})

})

})