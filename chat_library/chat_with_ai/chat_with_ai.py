import openai

class Chat:
    def __init__(self, api_key, system_prompt):
        openai.api_key = api_key
        self.system_prompt = system_prompt
        self.chat_history = ""

    def ask(self, user_input):
        prompt = f"{self.system_prompt}\nUser: {user_input}\nAI:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100,
        )
        message = response.choices[0].text.strip()
        self.chat_history += f"\nUser: {user_input}\nAI: {message}"
        return message

    def reset(self):
        self.chat_history = ""
