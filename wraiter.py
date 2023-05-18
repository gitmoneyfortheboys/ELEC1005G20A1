import openai
import os
import webbrowser
import pyperclip as pc
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

openai.api_key = "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"
model_engine = "text-davinci-003"

class EmailDialog(tk.simpledialog.Dialog):

    def body(self, master):

        self.result = {}

        tk.Label(master, text="Who are you writing this email to? (e.x. Mother, Father, Friend, Teacher)").grid(row=0)
        tk.Label(master, text="Enter the email id of the recipient").grid(row=1)
        tk.Label(master, text="What is the subject of your email? (e.x. Request for absence)").grid(row=2)
        tk.Label(master, text="What is the tone of your email? (e.x. formal,informal)").grid(row=3)
        tk.Label(master, text="Enter any additional information to include and other requirements that you may have").grid(row=4)

        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)
        self.e3 = tk.Entry(master)
        self.e4 = tk.Entry(master)
        self.e5 = tk.Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)

    def apply(self):
        self.result["recipient"] = self.e1.get()
        self.result["emailid"] = self.e2.get()
        self.result["subject"] = self.e3.get()
        self.result["tone"] = self.e4.get()
        self.result["info"] = self.e5.get()

def email_parameters(name, tk_instance):
    dialog = EmailDialog(tk_instance)

    if dialog.result is not None:
        recipient = dialog.result["recipient"]
        emailid = dialog.result["emailid"]
        subject = dialog.result["subject"]
        tone = dialog.result["tone"]
        info = dialog.result["info"]

        prompt = (f'''Write an email to my {recipient} about {subject} in a {tone} tone in no less than 300 words.
        Exclude stating the subject. Be sure to include the email signature with my name which is {name}. {info}''')
        return prompt, recipient, emailid, subject, tone

# Similar for blog_parameters and caption_parameters with different fields

def api_request(user_prompt):
    completion = openai.Completion.create(
    engine = model_engine,
    prompt = user_prompt,
    max_tokens = 3700,
    n = 1,
    stop = None,
    temperature = 0.4,)

    response = completion.choices[0].text 
    return (response)

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('WRAITER : Next Generation AI Content Writer')
        self.geometry("800x600")

        tk.Label(self, text="What do you want to write today?").pack(pady=10)

        tk.Button(self, text="Email", command=self.write_email).pack(fill='x')
        tk.Button(self, text="Blog", command=self.write_blog).pack(fill='x')
        tk.Button(self, text="Social Media Caption", command=self.write_caption).pack(fill='x')

    def write_email(self):
        self.withdraw()
        name = simpledialog.askstring("Input", "What's your name?", parent=self)
        information = email_parameters(name, self)
        body = api_request(information[0])
        webbrowser.open('mailto:?to=' + information[2] + '&subject=' + information[3] + '&body=' + body)
        self.deiconify()

    def write_blog(self):
        self.withdraw()
        information = blog_parameters()
        blog = api_request(information)
        pc.copy(blog)
        messagebox.showinfo("Blog", "The blog has been copied to your clipboard!\n"+blog)
        self.deiconify()

    def write_caption(self):
        self.withdraw()
        information = caption_parameters()
        caption = api_request(information)
        pc.copy(caption)
        messagebox.showinfo("Caption", "The caption has been copied to your clipboard!\n"+caption)
        self.deiconify()

if __name__ == '__main__':
    app = MainPage()
    app.mainloop()

