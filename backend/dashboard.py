from flask import Flask

app = Flask(__name__)

@app.route("/")
def dashboard():
    return """
    <html>
    <head>
        <title>AI Phishing Dashboard</title>
    </head>
    <body style="font-family:Arial; text-align:center; margin-top:30px;">

        <h1>🛡 AI Phishing Detection Dashboard</h1>

        <table border="1" style="margin:auto; margin-top:20px;">
            <thead>
                <tr>
                    <th>URL</th>
                    <th>Result</th>
                    <th>Confidence</th>
                </tr>
            </thead>
            <tbody id="data"></tbody>
        </table>

        <script>
        fetch("http://127.0.0.1:5000/logs")
        .then(res => res.json())
        .then(data => {

            let table = document.getElementById("data")

            data.forEach(item => {

                let row = `<tr>
                    <td>${item.url}</td>
                    <td>${item.result}</td>
                    <td>${item.confidence}%</td>
                </tr>`

                table.innerHTML += row
            })
        })
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(port=5002, debug=True)