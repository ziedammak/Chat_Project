from chat import Chat

api_key = "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"
system_prompt = "You are a helpful assistant.\n"
chatbot = Chat(api_key, system_prompt)

response = chatbot.ask("Hello, how can you help?")
print(response)

chatbot.reset()
