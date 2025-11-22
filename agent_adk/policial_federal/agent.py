from flask import Flask, request, jsonify, render_template
from google.adk.agents import Agent

app = Flask(__name__)

root_agent = Agent(
    name="capitao_nascimento_3000",
    model="gemini-2.5-flash",
    description="Agente estilo BOPE..."
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Mensagem ausente"}), 400

    user_message = data["message"]

    # CHAMADA CORRETA DO AGENTE
    response = root_agent.generate(message=user_message)

    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
