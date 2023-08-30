from flask import Flask, render_template, request, jsonify
from chat_library.chat_with_ai.chat_with_ai  import Chat
app = Flask(__name__,template_folder='web_interface/templates')

api_key = "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"
system_prompt = "You are a helpful assistant.\n"
chatbot = Chat(api_key, system_prompt)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        chat_history.append({"role": "user", "content": user_input})
        ai_response = chatbot.ask(user_input)
        chat_history.append({"role": "ai", "content": ai_response})
    return render_template("chat.html", chat_history=chat_history)

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("user_input")
    chat_history.append({"role": "user", "content": user_input})
    ai_response = chatbot.ask(user_input)
    chat_history.append({"role": "ai", "content": ai_response})
    return jsonify({"ai_response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
