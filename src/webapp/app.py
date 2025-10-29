from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Click Demo</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="font-family: system-ui, sans-serif; padding: 2rem;">
  <h1>Azure App Service demo</h1>
  <button id="showBtn" style="padding:.6rem 1rem; font-size:1rem;">Click me</button>
  <p id="msg" style="display:none; margin-top:1rem; font-size:1.1rem;">Hello from Franks Azure app! 🎉</p>

  <script>
    document.getElementById('showBtn').addEventListener('click', function () {
      var p = document.getElementById('msg');
      p.style.display = 'block';
    });
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    # Local dev run
    app.run(host="0.0.0.0", port=5000)
