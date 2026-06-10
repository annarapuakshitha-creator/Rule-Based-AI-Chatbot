from datetime import datetime 
print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")
    elif user == "good morning":
        print("Bot: Good morning! Have a great day!")
    elif user == "good night":
        print("Bot: Good night! Sweet dreams!")
    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "who created you":
         print("Bot: I was created by an AI intern at DecodeLabs.")

    elif user == "help":
         print("Bot: You can say hi, ask my name, ask how I am, or type bye.")
    elif user == "time":
         current_time = datetime.now().strftime("%I:%M %p")
         print("Bot: Current time is", current_time)

    elif user == "date":
         current_date = datetime.now().strftime("%d-%m-%Y")
         print("Bot: Today's date is", current_date)

    elif user == "thank you":
         print("Bot: You're welcome!")

    elif user == "help":
         print("Bot: Available commands:")
         print("- hi")
         print("- hello")
         print("- how are you")
         print("- what is your name")
         print("- time")
         print("- date")
         print("- thank you")
         print("- who created you")
         print("- bye")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")