def chatbot():
    print("🤖 Chatbot: Hi! I'm your friendly chatbot.")
    print("Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there! 😊")
        
        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm just running some code, but I'm doing great! 😄")
        
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I'm a basic Python chatbot created for practice.")
        
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a wonderful day! 👋")
            break
        
        else:
            print("Chatbot: Sorry, I didn't understand that. Please try again!")
            

# Run chatbot
if __name__ == "__main__":
    chatbot()
