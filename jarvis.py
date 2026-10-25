"""
Jarvis - a simple text-based assistant made for Karol.
Needs only Python 3. No extra installs required.
Run it with:  python jarvis.py
"""

import datetime
import random
import webbrowser

NAME = "Jarvis"
YOUR_NAME = "Karol"

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I told my computer I needed a break. It said: no problem, I'll go to sleep.",
    "Why was the computer cold? It left its Windows open.",
]


def respond(command):
    command = command.lower().strip()

    if any(word in command for word in ["hello", "hi", "hey"]):
        return "Hello, " + YOUR_NAME + "! How can I help you?"

    if "time" in command:
        return "The time is " + datetime.datetime.now().strftime("%H:%M") + ", " + YOUR_NAME + "."

    if "date" in command or "day" in command:
        return "Today is " + datetime.datetime.now().strftime("%A, %B %d, %Y") + ", " + YOUR_NAME + "."

    if "joke" in command:
        return random.choice(JOKES)

    if "your name" in command:
        return "I am " + NAME + ", your personal assistant, " + YOUR_NAME + "."

    if "my name" in command or "who am i" in command:
        return "You are " + YOUR_NAME + "!"

    if command.startswith("search "):
        query = command[len("search "):]
        webbrowser.open("https://www.google.com/search?q=" + query.replace(" ", "+"))
        return "Searching Google for: " + query

    if command.startswith("open "):
        site = command[len("open "):].replace(" ", "")
        webbrowser.open("https://www." + site + ".com")
        return "Opening " + site + ".com"

    if "help" in command:
        return (
            "Try: hello, what time is it, what is the date, tell me a joke, "
            "what is my name, search cats, open youtube, or bye"
        )

    return "Sorry " + YOUR_NAME + ", I don't understand that yet. Type 'help' to see what I can do."


def main():
    print(NAME + " is ready, " + YOUR_NAME + ". Type 'help' for ideas or 'bye' to quit.")
    while True:
        command = input(YOUR_NAME + ": ")
        if command.lower().strip() in ["bye", "exit", "quit"]:
            print(NAME + ": Goodbye, " + YOUR_NAME + "!")
            break
        print(NAME + ": " + respond(command))


if __name__ == "__main__":
    main()
