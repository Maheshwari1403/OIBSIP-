import tkinter as tk
from tkinter import scrolledtext
import datetime
import random

# ================= BOT LOGIC =================
def chatbot_reply(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return random.choice(["Hello 👋", "Hi there!", "Hey! How can I help?"])

    elif "how are you" in user_input:
        return "I'm working perfectly!"

    elif "your name" in user_input:
        return "I am your Smart Chatbot 🤖"

    elif "time" in user_input:
        return datetime.datetime.now().strftime("Time: %H:%M")

    elif "date" in user_input:
        return datetime.datetime.now().strftime("Date: %d-%m-%Y")

    elif "python" in user_input:
        return "Python is great for AI, automation, and apps like this."

    elif "study" in user_input:
        return "Stay consistent. Focus on concepts."

    elif "motivate" in user_input:
        return random.choice([
            "Keep going 💪",
            "Consistency beats talent",
            "You can do it!"
        ])

    elif "bye" in user_input:
        return "Goodbye 👋"

    else:
        return random.choice([
            "I didn't understand that.",
            "Try asking differently.",
            "I'm still learning 🤖"
        ])

# ================= SEND FUNCTION =================
def send_message():
    user_msg = entry.get()

    if user_msg.strip() == "":
        return

    time = datetime.datetime.now().strftime("%H:%M")

    chat_box.config(state=tk.NORMAL)

    # USER MESSAGE
    chat_box.insert(tk.END, f"[{time}] You:\n{user_msg}\n", "user")

    # BOT REPLY
    reply = chatbot_reply(user_msg)
    chat_box.insert(tk.END, f"[{time}] Bot:\n{reply}\n\n", "bot")

    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

    entry.delete(0, tk.END)

# ================= UI =================
root = tk.Tk()
root.title("Smart Chatbot")
root.geometry("500x600")
root.config(bg="#0F172A")  # dark blue background

# Header
header = tk.Label(root, text="🤖 Smart Chatbot", bg="#1E293B", fg="white",
                  font=("Helvetica", 16, "bold"), pady=10)
header.pack(fill="x")

# Chat area
chat_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 12),
    bg="#020617",
    fg="white",
    bd=0
)
chat_box.pack(padx=10, pady=10, fill="both", expand=True)
chat_box.config(state=tk.DISABLED)

# Styling messages
chat_box.tag_config("user",
                    background="#2563EB",
                    foreground="white",
                    spacing1=5,
                    spacing3=5,
                    lmargin1=50)

chat_box.tag_config("bot",
                    background="#16A34A",
                    foreground="white",
                    spacing1=5,
                    spacing3=10,
                    rmargin=50)

# Input area
bottom_frame = tk.Frame(root, bg="#0F172A")
bottom_frame.pack(fill="x", pady=5)

entry = tk.Entry(bottom_frame, font=("Helvetica", 12), bg="#1E293B", fg="white", insertbackground="white")
entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

send_btn = tk.Button(bottom_frame, text="Send", command=send_message,
                     bg="#22C55E", fg="black", font=("Helvetica", 10, "bold"))
send_btn.pack(side="right", padx=10)

root.mainloop()