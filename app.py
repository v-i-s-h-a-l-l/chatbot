from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
client = OpenAI(
    api_key="API Key is not pasted here for security reasons",
)


@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_message}]
        )

        bot_response = response.choices[0].message.content.strip()
        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(debug=True)
