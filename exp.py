from chat import Chat

api_key = "insert_Key"
system_prompt = "You are a helpful assistant.\n"
chatbot = Chat(api_key, system_prompt)

response = chatbot.ask("Hello, how can you help?")
print(response)

chatbot.reset()
