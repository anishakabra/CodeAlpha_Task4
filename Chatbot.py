import tkinter as tk
from tkinter import scrolledtext

# Define bot responses
def get_bot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi there!"
    elif user_input == "how are you":
        return "I'm doing great, thanks for asking!"
    elif user_input == "what's your name":
        return "I'm ChatBot 1.0."
    elif user_input == "what can you do":
        return "I can chat with you and respond to some basic questions."
    elif user_input == "tell me a joke":
        return "Why don’t scientists trust atoms? Because they make up everything!"
    elif user_input == "bye":
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that."

# Handle send button click
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    bot_response = get_bot_response(user_input)
    chat_window.insert(tk.END, "Bot: " + bot_response + "\n\n")
    user_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Simple ChatBot")
root.geometry("400x500")
root.config(bg="lightblue")

# Chat display
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 10))
chat_window.pack(pady=10)
chat_window.config(state=tk.NORMAL)

# User input box
user_entry = tk.Entry(root, width=40, font=("Arial", 12))
user_entry.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, width=10, bg="lightgreen")
send_button.pack()

# Run the GUI loop
root.mainloop()
