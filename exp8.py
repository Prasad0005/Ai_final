
def chatbot():
    print("Chatbot: Hello! How can I help you?")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Chatbot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Chatbot: I am fine. Thank you!")

        elif user == "what is your name":
            print("Chatbot: I am a simple Python chatbot.")

        elif user == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
