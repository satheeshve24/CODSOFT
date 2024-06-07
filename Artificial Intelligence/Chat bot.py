
print("Welcome to the Color Chatbot!")
print("You can ask me about colors.")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Color Chatbot: Goodbye!")
        break
    elif "what is your favorite color" in user_input:
        print("Color Chatbot: My favorite color is blue.")
    elif "what color is the sky" in user_input:
        print("Color Chatbot: The sky is usually blue.")
    elif "what color is the grass" in user_input:
        print("Color Chatbot: The grass is usually green.")
    elif "what color is the sun" in user_input:
        print("Color Chatbot: The sun appears yellow.")
    else:
        print("Color Chatbot: I'm sorry, I don't understand that.")

