import openai
import os
import webbrowser
import pyperclip as pc
import tkinter as tk
from tkinter import ttk, messagebox

openai.api_key = ""
model_engine = "text-davinci-003"

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title=None):
        super().__init__(parent)

        if title:
            self.title(title)

        # Set the size of the window to the same size as the parent
        self.geometry(parent.winfo_geometry())

        # Set the background color
        self.configure(background='black')

class EmailDialog(CustomDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Email Parameters')
        self.geometry("800x600")  # The same size as MainPage
        self.configure(background='black')  # Set dialog window background to black
        self.result = None
        self.body(self)
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.grab_set()

    def body(self, master):
        master.configure(background='black')
        self.result = {}

        tk.Label(master, text="What's your name?", bg="black", fg="white").grid(row=0)
        tk.Label(master, text="Who are you writing this email to? (e.x. Mother, Father, Friend, Teacher)", bg="black", fg="white").grid(row=1)
        tk.Label(master, text="Enter the email id of the recipient", bg="black", fg="white").grid(row=2)
        tk.Label(master, text="What is the subject of your email? (e.x. Request for absence)", bg="black", fg="white").grid(row=3)
        tk.Label(master, text="What is the tone of your email? (e.x. formal,informal)", bg="black", fg="white").grid(row=4)
        tk.Label(master, text="Enter any additional information to include and other requirements that you may have", bg="black", fg="white").grid(row=5)

        self.e0 = tk.Entry(master, bg="white", fg="black")
        self.e1 = tk.Entry(master, bg="white", fg="black")
        self.e2 = tk.Entry(master, bg="white", fg="black")
        self.e3 = tk.Entry(master, bg="white", fg="black")
        self.e4 = tk.Entry(master, bg="white", fg="black")
        self.e5 = tk.Entry(master, bg="white", fg="black")

        self.e0.grid(row=0, column=1)
        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        self.e3.grid(row=3, column=1)
        self.e4.grid(row=4, column=1)
        self.e5.grid(row=5, column=1)

        self.ok_button = tk.Button(master, text="OK", command=self.ok, bg="white", fg="black")
        self.ok_button.grid(row=6, column=0, columnspan=2)


    def apply(self):
        result = {}
        result["name"] = self.e0.get()
        result["recipient"] = self.e1.get()
        result["emailid"] = self.e2.get()
        result["subject"] = self.e3.get()
        result["tone"] = self.e4.get()
        result["info"] = self.e5.get()
        return result

    def ok(self, event=None):
        self.result = self.apply()
        self.destroy()

    def cancel(self, event=None):
        self.destroy()

class BlogDialog(CustomDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Blog Parameters')
        self.geometry("800x600")
        self.configure(background='black') 
        self.result = None
        self.body(self)
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.grab_set()

    def body(self, master):
        master.configure(background='black')
        self.result = {}

        tk.Label(master, text="What's your name?", bg="black", fg="white").grid(row=0)
        tk.Label(master, text="What is the topic of your blog?", bg="black", fg="white").grid(row=1)
        tk.Label(master, text="What is the tone of your blog? (e.x. formal, informal)", bg="black", fg="white").grid(row=2)
        tk.Label(master, text="Enter any additional information to include and other requirements that you may have", bg="black", fg="white").grid(row=3)

        self.e0 = tk.Entry(master, bg="white", fg="black")
        self.e1 = tk.Entry(master, bg="white", fg="black")
        self.e2 = tk.Entry(master, bg="white", fg="black")
        self.e3 = tk.Entry(master, bg="white", fg="black")

        self.e0.grid(row=0, column=1)
        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        self.e3.grid(row=3, column=1)

        self.ok_button = tk.Button(master, text="OK", command=self.ok, bg="white", fg="black")
        self.ok_button.grid(row=4, column=0)

    def apply(self):
        result = {}
        result["name"] = self.e0.get()
        result["topic"] = self.e1.get()
        result["tone"] = self.e2.get()
        result["info"] = self.e3.get()
        return result

    def ok(self, event=None):
        self.result = self.apply()
        self.destroy()
    
    def cancel(self, event=None):
        self.destroy()


class CaptionDialog(CustomDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Caption Parameters')
        self.geometry("800x600")
        self.configure(background='black') 
        self.result = None
        self.body(self)
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.grab_set()

    def body(self, master):
        master.configure(background='black')
        self.result = {}

        tk.Label(master, text="What's the image about? (e.x. sunset, kids playing)", bg="black", fg="white").grid(row=0)
        tk.Label(master, text="What is the tone of your caption? (e.x. inspirational, humorous)", bg="black", fg="white").grid(row=1)
        tk.Label(master, text="Enter any additional information to include and other requirements that you may have", bg="black", fg="white").grid(row=2)

        self.e0 = tk.Entry(master, bg="white", fg="black")
        self.e1 = tk.Entry(master, bg="white", fg="black")
        self.e2 = tk.Entry(master, bg="white", fg="black")

        self.e0.grid(row=0, column=1)
        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)

        self.ok_button = tk.Button(master, text="OK", command=self.ok, bg="white", fg="black")
        self.ok_button.grid(row=3, column=0)

    def apply(self):
        result = {}
        result["image"] = self.e0.get()
        result["tone"] = self.e1.get()
        result["info"] = self.e2.get()
        return result

    def ok(self, event=None):
        self.result = self.apply()
        self.destroy()

    def cancel(self, event=None):
        self.destroy()


class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")
        self.title("NextGen Writer")
        self.configure(background='black')  # Set MainPage background to black

        # Load your images
        self.img_email = tk.PhotoImage(file='email.png')  # Replace with your file names
        self.img_blog = tk.PhotoImage(file='Blog.png')  # Replace with your file names
        self.img_caption = tk.PhotoImage(file='Caption.png')  # Replace with your file names

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        for i in range(5):  # Increase the range to 5
            self.grid_rowconfigure(i+2, weight=1) # Reduce the weight to 1
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)

        # Set greeting label with increased font size and place it in the grid
        self.lbl_greeting = tk.Label(self, text="What would you like to write today?", bg="black", fg="white", font=("Helvetica", 30))
        self.lbl_greeting.grid(row=0, column=0, columnspan=2)

        # Place the buttons with images in the grid under the greeting label
        self.btn_email = tk.Button(self, image=self.img_email, command=self.email_prompt, bg="white", fg="black")
        self.btn_email.grid(row=1, column=0, columnspan=2)

        # Add empty row
        self.grid_rowconfigure(2, weight=1)  # Reduce the weight to 1

        self.btn_blog = tk.Button(self, image=self.img_blog, command=self.blog_prompt, bg="white", fg="black")
        self.btn_blog.grid(row=3, column=0, columnspan=2)

        # Add empty row
        self.grid_rowconfigure(4, weight=1)  # Reduce the weight to 1

        self.btn_caption = tk.Button(self, image=self.img_caption, command=self.caption_prompt, bg="white", fg="black")
        self.btn_caption.grid(row=5, column=0, columnspan=2)

        # Add empty rows at the bottom
        self.grid_rowconfigure(6, weight=2)  # Empty space with more weight
        self.grid_rowconfigure(7, weight=1)  # Empty space with less weight

    def email_prompt(self):
        dialog = EmailDialog(self)
        dialog.wait_window()
        if dialog.result is not None:
            name = dialog.result["name"]
            recipient = dialog.result["recipient"]
            emailid = dialog.result["emailid"]
            subject = dialog.result["subject"]
            tone = dialog.result["tone"]
            info = dialog.result["info"]

            prompt = (f'''Write an email to my {recipient} about {subject} in a {tone} tone in no more than 300 words.
            Exclude stating the subject. Be sure to include the email signature with my name which is {name}. {info}''')

            response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=200)
            email_body = response.choices[0].text.strip()

            # Open the default email client with the composed email
            webbrowser.open('mailto:?to=' + emailid + '&subject=' + subject + '&body=' + email_body)

    def blog_prompt(self):
        dialog = BlogDialog(self)
        dialog.wait_window()
        if dialog.result is not None:
            name = dialog.result["name"]
            topic = dialog.result["topic"]
            tone = dialog.result["tone"]
            info = dialog.result["info"]

            prompt = (f'''Write a blog post on the topic of "{topic}" in a {tone} tone.
            The post should be at least 500 words. Please include the author's bio with my name which is {name}. {info}''')

            response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=500)
            blog_text = response.choices[0].text.strip()
            pc.copy(blog_text) # Copy blog content to clipboard
            messagebox.showinfo("Blog Content", "The blog content has been copied to your clipboard!")


    def caption_prompt(self):
        dialog = CaptionDialog(self)
        dialog.wait_window()
        if dialog.result is not None:
            image = dialog.result["image"]
            tone = dialog.result["tone"]
            info = dialog.result["info"]

            prompt = (f'''Write a {tone} caption for an image about "{image}". {info}''')

            response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=50)
            caption_text = response.choices[0].text.strip()
            pc.copy(caption_text)  # Copy caption content to clipboard
            messagebox.showinfo("Caption Content", "The caption has been copied to your clipboard!")


if __name__ == "__main__":
    app = MainPage()
    app.mainloop()