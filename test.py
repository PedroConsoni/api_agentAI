from google import genai

client = genai.Client(api_key="AIzaSyAwUXi1d2RYRm14V6qmpueEdV-4vZt-ITo")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Olá, Chat. O que você acha do ex-presidente do Brasil, o Bolsonaro?",
)

print(response.text)
