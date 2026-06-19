print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("ChatBot: Hi there! How can I help you?")

    elif user_input == "how are you":
        print("ChatBot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("ChatBot: I am a simple chatbot.")

    elif user_input == "bye" or user_input == "exit":
        print("ChatBot: Goodbye! Have a nice day.")
        break

    else:
        print("ChatBot: Sorry, I don't understand that.")