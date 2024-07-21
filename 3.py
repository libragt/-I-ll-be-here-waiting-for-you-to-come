import tkinter as tk
from tkinter import scrolledtext

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat With Me")
        self.root.configure(background="#fafafa")
        
        self.chat_history = scrolledtext.ScrolledText(self.root, width=50, height=20, wrap=tk.WORD, font=("Roboto", 12))
        self.chat_history.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew")
        self.chat_history.config(background="#ffffff", foreground="#333333", insertbackground="#3897f0")  # Background, text, and cursor colors
        
        self.user_label = tk.Label(self.root, text="You:", font=("Roboto", 12), background="#fafafa")
        self.user_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.user_entry = tk.Entry(self.root, width=40, font=("Roboto", 12))
        self.user_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, font=("Roboto", 12), background="#3897f0", foreground="#ffffff")
        self.send_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.user_entry.bind("<Return>", lambda event: self.send_message())
        
        self.bot_name = "Python"
        self.conversation = []
        
        self.responses = {
            "kok bisaa?": "I'll be here waiting for you to come"
        }
        
        self.additional_messages = [
            "And bring me right back home",
            "I'm caught up with these memories",
            "Just by sitting here alone",
            ":("
        ]
        
        self.start_chat()

    def send_message(self):
        user_message = self.user_entry.get()
        self.conversation.append(("You", user_message))
        self.display_message()
        self.user_entry.delete(0, tk.END)
        self.respond_with_delay(user_message.lower())
    
    def respond_with_delay(self, message):
        response = self.responses.get(message, "Maaf, saya tidak mengerti pertanyaan tersebut.")
        
        if message == "kok bisaa?":
            self.root.after(1000, self.display_response_and_schedule, response)
        else:
            self.conversation.append((self.bot_name, response))
            self.display_message()
    
    def display_response_and_schedule(self, response):
        self.conversation.append((self.bot_name, response))
        self.display_message()
        self.root.after(3500, self.display_message_lines, self.additional_messages)  # Delay changed to 5 seconds
    
    def display_message_lines(self, lines, index=0):
        if index < len(lines):
            self.conversation.append((self.bot_name, lines[index]))
            self.display_message()
            self.root.after(3500, self.display_message_lines, lines, index + 1)  # 5 seconds delay for each message
    
    def display_message(self):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.delete(1.0, tk.END)
        for sender, msg in self.conversation:
            if sender == "You":
                self.chat_history.insert(tk.END, f"You: {msg}\n", "user_message")
            else:
                self.chat_history.insert(tk.END, f"{self.bot_name}: {msg}\n", "bot_message")
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.see(tk.END)
    
    def start_chat(self):
        messages = ["pppppp","pppppp", "pppppp","pppppp", "aku gamon"]
        self.schedule_messages(messages)
    
    def schedule_messages(self, messages, index=0):
        if index < len(messages):
            self.conversation.append((self.bot_name, messages[index]))
            self.display_message()
            self.root.after(1000, self.schedule_messages, messages, index + 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApplication(root)
    root.mainloop()
