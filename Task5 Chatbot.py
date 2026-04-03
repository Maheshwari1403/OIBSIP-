import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog

# ================= SERVER =================
HOST = '127.0.0.1'
PORT = 1489
LIMIT = 10
active_clients = []

def send_message_to_all(message):
    for user in active_clients:
        try:
            user[1].sendall(message.encode())
        except:
            pass

def listen_from_client(client, username):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                final_msg = username + '~' + message
                send_message_to_all(final_msg)
        except:
            break

def client_handler(client):
    while True:
        try:
            username = client.recv(2048).decode('utf-8')
            if username:
                active_clients.append((username, client))
                send_message_to_all(f"SERVER~{username} joined chat")
                break
        except:
            break

    threading.Thread(target=listen_from_client, args=(client, username), daemon=True).start()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(LIMIT)
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        threading.Thread(target=client_handler, args=(client,), daemon=True).start()

# ================= CLIENT UI =================

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Colors (New Theme)
BG_COLOR = "#1E1E2E"
CARD_COLOR = "#2A2A3C"
ACCENT = "#00C853"
TEXT = "#FFFFFF"

def add_message(msg, tag=None):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, msg + "\n", tag)
    message_box.config(state=tk.DISABLED)
    message_box.see(tk.END)

def connect():
    try:
        client.connect((HOST, PORT))
        username = username_entry.get()

        if username == "":
            messagebox.showerror("Error", "Enter username")
            return

        client.sendall(username.encode())
        add_message("[SYSTEM] Connected to server")

        threading.Thread(target=listen_messages, daemon=True).start()

        username_entry.config(state=tk.DISABLED)
        join_btn.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def send_message():
    msg = message_entry.get()

    if msg == "":
        return

    client.sendall(msg.encode())
    add_message(f"You: {msg}", "me")
    message_entry.delete(0, tk.END)

def upload_file():
    file = filedialog.askopenfilename()
    if file:
        add_message(f"You uploaded: {file}", "me")

def listen_messages():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                username, content = message.split('~')
                add_message(f"{username}: {content}", "other")
        except:
            break

# ================= UI =================

root = tk.Tk()
root.title("Chat Application")
root.geometry("700x500")
root.config(bg=BG_COLOR)

# Top
top_frame = tk.Frame(root, bg=BG_COLOR)
top_frame.pack(fill="x")

tk.Label(top_frame, text="Username:", bg=BG_COLOR, fg=TEXT).pack(side="left", padx=5)

username_entry = tk.Entry(top_frame)
username_entry.pack(side="left", padx=5)

join_btn = tk.Button(top_frame, text="Join", bg=ACCENT, fg="black", command=connect)
join_btn.pack(side="left", padx=5)

# Chat box
message_box = scrolledtext.ScrolledText(root, bg=CARD_COLOR, fg=TEXT)
message_box.pack(fill="both", expand=True, padx=10, pady=10)
message_box.config(state=tk.DISABLED)

message_box.tag_config("me", foreground="#00E5FF")
message_box.tag_config("other", foreground="#FFFFFF")

# Bottom
bottom_frame = tk.Frame(root, bg=BG_COLOR)
bottom_frame.pack(fill="x")

message_entry = tk.Entry(bottom_frame)
message_entry.pack(side="left", fill="x", expand=True, padx=5)

send_btn = tk.Button(bottom_frame, text="Send", bg=ACCENT, command=send_message)
send_btn.pack(side="left", padx=5)

upload_btn = tk.Button(bottom_frame, text="Upload", bg=ACCENT, command=upload_file)
upload_btn.pack(side="left", padx=5)

# ================= MAIN =================

# Start server in background
threading.Thread(target=start_server, daemon=True).start()

root.mainloop()