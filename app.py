from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)
target_data = {"phone": "", "count": 0}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>FATİH KRAL</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        body { background: #000; color: #0ff; font-family: 'Orbitron', sans-serif; text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100vh; margin: 0; }
        h1 { font-size: 4em; text-shadow: 0 0 20px #0ff; }
        input { background: #111; border: 1px solid #0ff; color: #0ff; padding: 10px; margin: 10px; font-family: 'Orbitron'; text-align: center; }
        button { background: #0ff; color: #000; border: none; padding: 15px 30px; cursor: pointer; font-family: 'Orbitron'; font-weight: bold; }
    </style>
</head>
<body>
    <h1>FATİH KRAL</h1>
    <input type="text" id="phone" placeholder="Telefon (0 olmadan)"> <br>
    <input type="number" id="count" placeholder="Miktar"> <br>
    <button onclick="sendToKali()">EMRİ VER</button>
    <p id="status"></p>
    <script>
        function sendToKali() {
            const phone = document.getElementById('phone').value;
            const count = document.getElementById('count').value;
            fetch('/set_target', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({phone: phone, count: count})
            }).then(() => { document.getElementById('status').innerText = "Emir Kali'ye iletildi!"; });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index(): return render_template_string(HTML_TEMPLATE)

@app.route('/set_target', methods=['POST'])
def set_target():
    global target_data
    target_data = request.json
    return jsonify({"status": "ok"})

@app.route('/get_target')
def get_target(): return jsonify(target_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000))
