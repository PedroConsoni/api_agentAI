from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/gemini", methods=["POST"])
def gemini_api():
    data = request.json
    prompt = data.get("prompt", "")


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return jsonify({
        "response": response.text
    })

if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)
  