# import modules
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, filedialog
import wolframalpha
import threading

# Create Main Window
class PyBot:
	def __init__(self, root):
		self.root = root
		self.font = ('arial', 12)
		self.background_color = "#7e7a79"
		self.text_color = "#ffffff"

if __name__ == "__main__":
	root = Tk()
	root.title("PyBot - from Decoder")
	root.geometry("500x520")
	root.config(bg="#403b3a")
	root.resizable(0, 0)
	PyBot(root)
	root.mainloop()

# Add Widget
menubar = Menu(self.root)
option_menu = Menu(menubar, tearoff=0)
option_menu.add_command(label="Clear Chat", command=self.clear_chat)
option_menu.add_command(label="Save Chat", command=self.save_chat)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=self.root.quit)
menubar.add_cascade(label="Options", menu=option_menu)
self.root.config(menu=menubar)

self.text_area = ScrolledText(self.root, font=self.font, bg=self.background_color, fg=self.text_color)
self.text_area.place(x=10, y=10, width=480, height=440)

frame = Frame(self.root, bg=self.background_color)
frame.place(x=10, y=460, width=480, height=50)

self.entry_box = Entry(frame, font=("arial", 14))
self.entry_box.grid(row=0, column=0, pady=9, padx=5)

self.send_button = Button(frame, text="Send", command=self.human_input)
self.send_button.grid(row=0, column=1, pady=9, padx=5)

# Define Methods
def human_input(self):
	input = self.entry_box.get()
	if input:
		self.text_area.insert(END, "Human : " + input)
		self.entry_box.delete(0, END)
		self.call_bot(input)

def bot_output(self, input):
	appid = "wolframalpha api "
	client = wolframalpha.Client(appid)
	res = client.query(input)
	answer = next(res.results).text
	if answer:
		self.text_area.insert(END, "\nPyBott : "+answer+"\n")

def call_bot(self, input):
	x = threading.Thread(target=self.bot_output, args=(input,))
	x.start()

def save_chat(self):
	filename = filedialog.asksaveasfile()
	if filename:
		with open(filename, "w") as f:
			f.write(self.text_area.get(0.0, END))

def clear_chat():
	if messagebox.askyesno("PyBot Says", "Are You Sure"):
		self.text_area.delete(0.0, END)

		