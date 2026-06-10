def chatbot():
    print("🤖 Basic Chatbot")
    print("Type 'bye' to exit the chat.\n")

    while True:
        user_input = input("You: ").lower()

        # Predefined replies
        if user_input == "hello":
            print("Bot: Hi!")
        
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        
        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()
