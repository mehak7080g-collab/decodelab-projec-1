import random
from datetime import datetime

print("=" * 55)
print("                    VEX")
print("          PERSONAL RULE-BASED AI")
print("=" * 55)
print("VEX: Online! 🤖")
print("VEX: 'help' likho commands ke liye.")
print("VEX: 'exit' likho band karne ke liye.")
print()


# -----------------------------
# VEX RESPONSE FUNCTION
# -----------------------------

def vex_response(message):

    message = message.lower().strip()

    # GREETINGS
    if message in ["hello", "hi", "hey", "salam", "assalam o alaikum"]:
        return random.choice([
            "Hello! 👋 Main VEX hoon.",
            "Hey! 🤖 VEX online hai.",
            "Assalam o Alaikum! 👋"
        ])

    # NAME
    elif "your name" in message or "tumhara naam" in message:
        return "Mera naam VEX hai. 🤖"

    # HOW ARE YOU
    elif "how are you" in message or "kaise ho" in message:
        return "Main bilkul theek hoon! 😎"

    # PYTHON
    elif "python" in message:
        return "Python ek beginner-friendly programming language hai. 🐍"

    # CODING
    elif "coding" in message or "programming" in message:
        return "Coding ka matlab computer ko instructions dena hai. 💻"

    # AI
    elif "what is ai" in message or "ai kya hai" in message:
        return "AI yani Artificial Intelligence machines ko intelligent tasks perform karne mein help karti hai. 🤖"

    # RULE BASED AI
    elif "rule based ai" in message:
        return "Rule-Based AI predefined IF/ELIF/ELSE rules ke according decision leti hai."

    # MACHINE LEARNING
    elif "machine learning" in message:
        return "Machine Learning mein computer data se patterns learn karta hai."

    # HTML
    elif "html" in message:
        return "HTML website ka basic structure banane ke liye use hoti hai."

    # CSS
    elif "css" in message:
        return "CSS website ka design aur appearance control karti hai."

    # JAVASCRIPT
    elif "javascript" in message:
        return "JavaScript website ko interactive banane ke liye use hoti hai."

    # PHP
    elif "php" in message:
        return "PHP ek server-side programming language hai."

    # API
    elif "api" in message:
        return "API different software applications ko aapas mein communicate karne deti hai."

    # SERVER
    elif "server" in message:
        return "Server requests receive karta hai aur data ya services provide karta hai."

    # DATABASE
    elif "database" in message:
        return "Database data ko store aur manage karne ke liye use hota hai."

    # VARIABLE
    elif "variable" in message:
        return "Variable ek naam hota hai jisme hum data store karte hain."

    # LOOP
    elif "loop" in message:
        return "Loop code ko repeatedly run karne ke liye use hota hai."

    # IF ELSE
    elif "if else" in message:
        return "IF/ELSE conditions ke according different code execute karta hai."

    # FUNCTION
    elif "function" in message:
        return "Function reusable code ka block hota hai."

    # LIST
    elif "list" in message:
        return "Python list multiple values ko ek jagah store kar sakti hai."

    # DEBUGGING
    elif "debugging" in message or "debug" in message:
        return "Debugging ka matlab program ke errors find aur fix karna hai. 🐛"

    # HELP
    elif message == "help":
        return """
VEX COMMANDS
-------------------------
help        → Commands show
time        → Current time
date        → Current date
joke        → Random joke
about       → VEX ke baare mein
exit        → Chatbot close

Try:
python
ai kya hai
coding
html
css
javascript
api
server
database
"""

    # TIME
    elif message == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"Current time: {current_time} ⏰"

    # DATE
    elif message == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Aaj ki date: {current_date} 📅"

    # JOKE
    elif message == "joke":
        return random.choice([
            "Programmer ka favourite place? Bug-zar 😂",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
            "Python developer ka favourite snake? Python obviously! 🐍"
        ])

    # ABOUT
    elif message == "about":
        return """
Main VEX hoon 🤖

Type:
Rule-Based AI Chatbot

Mera decision-making system
predefined rules aur conditions
use karta hai.
"""

    # THANKS
    elif "thank" in message or "thanks" in message or "shukriya" in message:
        return "You're welcome! 😎"

    # BYE
    elif message in ["bye", "goodbye", "khuda hafiz"]:
        return "Goodbye! 👋 Phir milte hain."

    # UNKNOWN
    else:
        return (
            "Hmm 🤔 mujhe is input ka rule nahi mila.\n"
            "Try 'help' likho."
        )


# -----------------------------
# MAIN CHAT LOOP
# -----------------------------

while True:

    user_input = input("You: ")

    # EXIT COMMAND
    if user_input.lower().strip() in ["exit", "quit", "stop"]:

        print("VEX: System shutting down... 🔴")
        print("VEX: Goodbye! 👋")

        break

    # GET RESPONSE
    response = vex_response(user_input)

    # SHOW RESPONSE
    print("VEX:", response)
    print()