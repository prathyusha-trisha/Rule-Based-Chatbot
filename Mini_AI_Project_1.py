def simple_ai_chatbot():
    print("=" * 60)
    print("🤖 PyBot: Rule-Based Assistant Initialized (type 'bye' to exit)")
    print("=" * 60)
    
    while True:
        user_input = input("\nYou: ").strip()
        clean_text = user_input.lower()
        if clean_text in ["bye", "exit", "quit", "goodbye"]:
            print("Bot: Goodbye! Have a productive day ahead.")
            break
        
        elif any(greeting in clean_text for greeting in ["hello", "hi", "hey"]):
            print("Bot: Hello! Welcome. How can I assist your studies today?")
            
        elif "how are you" in clean_text:
            print("Bot: I'm operating at peak performance. Thanks for asking!")
            
        elif "what is ai" in clean_text or "define ai" in clean_text:
            print("Bot: AI stands for Artificial Intelligence—the simulation of human intelligence by computers.")
            
        elif "who made you" in clean_text or "who created you" in clean_text:
            print("Bot: I was created as a rule-based Python project for Week 1 AI Assignment.")
            
        elif "help" in clean_text:
            print("Bot: You can ask me about AI, greet me, ask how I'm doing, or type 'bye' to exit.")
            
        elif clean_text == "":
            print("Bot: It seems you submitted an empty line. Say something!")
            
        else:
            print("Bot: I'm sorry, I am a rule-based bot and do not recognize that query yet. Type 'help' for options.")

if __name__ == "__main__":
    simple_ai_chatbot()