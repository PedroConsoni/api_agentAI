from flask import Flask, request, jsonify
from google.adk.runtime import run_agent
from policial_federal.agent import root_agent

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask_agent():
    data = request.get_json()

    if not data or "pergunta" not in data:
        return jsonify({"erro": "Envie um JSON com o campo 'pergunta'."}), 400

    pergunta = data["pergunta"]

    # Executa o agente ADK
    resultado = run_agent(
        agent=root_agent,
        user_message=pergunta
    )

    return jsonify({
        "pergunta": pergunta,
        "resposta": resultado.text
    })

if __name__ == "__main__":
    app.run(debug=True)
