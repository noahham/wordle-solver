# IMPORTS
from cgitb import text
from tkinter import *
from tkinter import ttk

# Setting up 'words' list
wordsTemp1 = open("words.txt", "r")
wordsTemp2 = wordsTemp1.readlines()
words = []
for line in wordsTemp2:
    words.append(line.strip())
words.sort()

filterWords = words

concFilterWords = []

# DISPLAY
root = Tk()

# Variables
letter = StringVar()
letter.set("A")

confirm = StringVar()
confirm.set("is on column")

position = StringVar()
position.set("1")

posOptions = [1, 2, 3, 4, 5]

# Functions

def addFilter():
# Letter 1
    if position.get() == "1":
    # UI
        posOptions.remove(1)
        posInput.config(values=posOptions)
        letter_1.config(text=letter.get())
        if confirm.get() == "is in column":
            letterBG_1.config(bg="#558d4e")
            letter_1.config(bg="#558d4e")
        else:
            letterBG_1.config(bg="#b59f3b")
            letter_1.config(bg="#b59f3b")
    # List
        if confirm.get() == "is in column":
            i = 0
            while i < len(filterWords):
                if (filterWords[i])[0:1] != (letter.get()).lower():
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
        else:
            posIndex = int(position.get()) -1
            i = 0
            while i < len(filterWords):
                if filterWords[i].find((letter.get()).lower()) == -1 or filterWords[i].find((letter.get()).lower()) == posIndex:
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
# Letter 2
    elif position.get() == "2":
    # UI
        posOptions.remove(2)
        posInput.config(values=posOptions)
        letter_2.config(text=letter.get())
        if confirm.get() == "is in column":
            letterBG_2.config(bg="#558d4e")
            letter_2.config(bg="#558d4e")
        else:
            letterBG_2.config(bg="#b59f3b")
            letter_2.config(bg="#b59f3b")
    # List
        if confirm.get() == "is in column":
            i = 0
            while i < len(filterWords):
                if (filterWords[i])[1:2] != (letter.get()).lower():
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
        else:
            posIndex = int(position.get()) -1
            i = 0
            while i < len(filterWords):
                if filterWords[i].find((letter.get()).lower()) == -1 or filterWords[i].find((letter.get()).lower()) == posIndex:
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
# Letter 3
    elif position.get() == "3":
    # UI
        posOptions.remove(3)
        posInput.config(values=posOptions)
        letter_3.config(text=letter.get())
        if confirm.get() == "is in column":
            letterBG_3.config(bg="#558d4e")
            letter_3.config(bg="#558d4e")
            
            
        else:
            letterBG_3.config(bg="#b59f3b")
            letter_3.config(bg="#b59f3b")
    # List
        if confirm.get() == "is in column":
            i = 0
            while i < len(filterWords):
                if (filterWords[i])[2:3] != (letter.get()).lower():
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
        else:
            posIndex = int(position.get()) -1
            i = 0
            while i < len(filterWords):
                if filterWords[i].find((letter.get()).lower()) == -1 or filterWords[i].find((letter.get()).lower()) == posIndex:
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
# Letter 4
    elif position.get() == "4":
    # UI
        posOptions.remove(4)
        posInput.config(values=posOptions)
        letter_4.config(text=letter.get())
        if confirm.get() == "is in column":
            letterBG_4.config(bg="#558d4e")
            letter_4.config(bg="#558d4e")
        else:
            letterBG_4.config(bg="#b59f3b")
            letter_4.config(bg="#b59f3b")
    # List
        if confirm.get() == "is in column":
            i = 0
            while i < len(filterWords):
                if (filterWords[i])[3:4] != (letter.get()).lower():
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
        else:
            posIndex = int(position.get()) -1
            i = 0
            while i < len(filterWords):
                if filterWords[i].find((letter.get()).lower()) == -1 or filterWords[i].find((letter.get()).lower()) == posIndex:
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
# Letter 5
    else:
    # UI
        posOptions.remove(5)
        posInput.config(values=posOptions)
        letter_5.config(text=letter.get())
        if confirm.get() == "is in column":
            letterBG_5.config(bg="#558d4e")
            letter_5.config(bg="#558d4e")
        else:
            letterBG_5.config(bg="#b59f3b")
            letter_5.config(bg="#b59f3b")
    # List
        if confirm.get() == "is in column":
            i = 0
            while i < len(filterWords):
                if (filterWords[i])[4:5] != (letter.get()).lower():
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
        else:
            posIndex = int(position.get()) -1
            i = 0
            while i < len(filterWords):
                if filterWords[i].find((letter.get()).lower()) == -1 or filterWords[i].find((letter.get()).lower()) == posIndex:
                    filterWords.remove(filterWords[i])
                    i -= 1
                i += 1
    concFilterWords = (", ".join(filterWords))
    output.config(state="normal")
    output.delete("1.0","end")
    output.insert(INSERT, (concFilterWords))
    output.config(state="disabled")
    print("Filter added.")


def resetFilter():
    letter_1.config(text="?", bg="#272b32")
    letter_2.config(text="?", bg="#272b32")
    letter_3.config(text="?", bg="#272b32")
    letter_4.config(text="?", bg="#272b32")
    letter_5.config(text="?", bg="#272b32")
    
    letterBG_1.config(bg="#272b32")
    letterBG_2.config(bg="#272b32")
    letterBG_3.config(bg="#272b32")
    letterBG_4.config(bg="#272b32")
    letterBG_5.config(bg="#272b32")
    
    filterWords = words
    posOptions = [1, 2, 3, 4, 5]
    posInput.config(values=posOptions)
    
    output.config(state="normal")
    output.delete("1.0","end")
    output.config(state="disabled")
    print("Filters cleared.")
    

# Screen
root.geometry("350x400")
root.configure(bg="#21252b")
root.title("Wordle Solver")

style = ttk.Style()
style.theme_use("classic")
style.configure("TCombobox", fieldbackground="#272b32", background="#21252b", foreground="white", borderwidth=0, justify="center")
style.configure("TFrame", fieldbackground="#272b32", background="#21252b", foreground="white", borderwidth=0, justify="center")


# Elements
letterInput = ttk.Combobox(root, textvariable=letter, width=2, font=("Arial Black", 14), justify="center",
                           values=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
letterInput.current(0)
letterInput.place(relx=.175, rely=.075, anchor="center")

conInput = ttk.Combobox(root, textvariable=confirm, width=13, font=("Arial Bold", 14), justify="center", 
                        values=["is in column", "isn't in column"])
conInput.current(0)
conInput.place(relx=.5, rely=.075, anchor="center")

posInput = ttk.Combobox(root, textvariable=position, state="", width=2, font=("Arial Black", 14), justify="center", 
                        values=posOptions)
posInput.current(0)
posInput.place(relx=.825, rely=.075, anchor="center")

addButton = Button(root, text="Add", width=9, font=("Arial Bold", 12), 
                    bd=0, fg="white", bg="#272b32", activeforeground="white", activebackground="#2a3037", command=addFilter)
addButton.place(relx=.35, rely=.175, anchor="center")

resetButton = Button(root, text="Reset", width=9, font=("Arial Bold", 12), 
                    bd=0, fg="white", bg="#272b32", activeforeground="white", activebackground="#2a3037", command=resetFilter)
resetButton.place(relx=.65, rely=.175, anchor="center")


letterBG_1 = Canvas(root, width=45, height=45, bg="#272b32", highlightthickness=0)
letterBG_1.place(relx=.18, rely=.31, anchor="center")

letterBG_2 = Canvas(root, width=45, height=45, bg="#272b32", highlightthickness=0)
letterBG_2.place(relx=.34, rely=.31, anchor="center")

letterBG_3 = Canvas(root, width=45, height=45, bg="#272b32", highlightthickness=0)
letterBG_3.place(relx=.5, rely=.31, anchor="center")

letterBG_4 = Canvas(root, width=45, height=45, bg="#272b32", highlightthickness=0)
letterBG_4.place(relx=.66, rely=.31, anchor="center")

letterBG_5 = Canvas(root, width=45, height=45, bg="#272b32", highlightthickness=0)
letterBG_5.place(relx=.82, rely=.31, anchor="center")


letter_1 = Label(root, text="?",fg="white", bg="#272b32", font=("Arial Black", 20))
letter_1.place(relx=.18, rely=.31, anchor="center")

letter_2 = Label(root, text="?",fg="white", bg="#272b32", font=("Arial Black", 20))
letter_2.place(relx=.34, rely=.31, anchor="center")

letter_3 = Label(root, text="?",fg="white", bg="#272b32", font=("Arial Black", 20))
letter_3.place(relx=.5, rely=.31, anchor="center")

letter_4 = Label(root, text="?",fg="white", bg="#272b32", font=("Arial Black", 20))
letter_4.place(relx=.66, rely=.31, anchor="center")

letter_5 = Label(root, text="?",fg="white", bg="#272b32", font=("Arial Black", 20))
letter_5.place(relx=.82, rely=.31, anchor="center")

output = Text(root, state="disabled", wrap="word", height=11, width=35, fg = "white", bg="#272b32", font=("Arial Bold", 12))
output.place(relx=.5, rely=.68, anchor="center")

root.mainloop()
