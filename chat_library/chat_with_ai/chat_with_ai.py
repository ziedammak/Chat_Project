import openai

class Chat:
    def __init__(self, api_key, system_prompt, model="gpt-3.5-turbo"):
        openai.api_key = api_key
        self.system_prompt = system_prompt
        self.chat_history = ""
        self.model = model

    def ask(self, user_input):
        prompt = f"{self.system_prompt}\nUser: {user_input}\nAI:"
        response = openai.ChatCompletion.create(  # Use ChatCompletion for chat models
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input},
            ],
        )
        message = response.choices[0].message["content"]
        self.chat_history += f"\nUser: {user_input}\nAI: {message}"
        return message

    def reset(self):
        self.chat_history = ""
