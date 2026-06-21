# -----------------------------------------
# Build a simple rule based chatbot
# -----------------------------------------
import random
from datetime import datetime
def chatbot(value):

    
    # 👉 Date & Time Portion
    current=datetime.now()
    if value=="date":
        return current.strftime("%d/%m/%Y")
    
    if value=="time":
        return current.strftime("%I:%M:%S %p")
    

    responses = {
        "hi": ["Hello!","Hi bro","Hi there","Hey!"],
        "hello": ["Hello!","Hi bro","Hi there","Hey!"],
        "how are you": ["I am fine, thanks!"],
        "good morning": ["Good morning!"],
        "good night": ["Good night!"],
        "good afternoon":["Good Afternoon!"],
        "what is your name": ["My name is Sam AI."],
        "what can you do": ["I can tell date, time and answer simple questions."],
        "help": ["You can ask me about date, time, greetings and more."],
        "who made you": ["I was created by a Python developer."],
        "thanks": ["You're welcome!", "Glad to help!"],
        "bye": ["Bye! Have a nice day."],
        }
    if value in responses:
        reply=random.choice(responses[value])
        return reply
    else:
        return random.choice(["Can you rephrase that?","I don't know about that.","Try asking something else."])

print("Hello! I am Sam Ai")
print("Sam : Hello , Enter bye for exit.")
print("Start your conversation : ")

while True:
    value = input("You :  ").lower().strip()
    result = chatbot(value)
    if value == "bye":
        print(f"Sam : {result}")
        break
    else:
        print(f"Sam : {result}")
        found=False
