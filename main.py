'''
Noah Ham
11/19/24
Wordle Solver 1.3
'''

from tkinter import *
from tkinter import ttk

class Solver:
    def __init__(self):
        """ Initializes the app and necessary variables """
        self.root = Tk()
        self.setupTk()
        
        self.setupWordsList('words.txt')

        # Instantiates dropdown variables
        self.letter = StringVar()
        self.confirm = StringVar()
        self.position = StringVar()
        self.letter.set("A")
        self.confirm.set("is on column")
        self.position.set("1")

        self.posOptions = ['1', '2', '3', '4', '5']

        self.createElements()
        self.reset()

    def setupTk(self):
        """ Initializes Tk object """
        self.root.geometry("350x400")
        self.root.configure(bg="#21252b")
        self.root.title("Wordle Solver")

        style = ttk.Style()
        style.theme_use("classic")
        style.configure("TCombobox", fieldbackground="#272b32", background="#21252b", foreground="white", borderwidth=0,
                        justify="center")
        style.configure("TFrame", fieldbackground="#272b32", background="#21252b", foreground="white", borderwidth=0,
                        justify="center")

    def setupWordsList(self, filename):
        """
        Takes the file and puts the words from it in a sorted list

        Parameters:
            filename (string): the name of the file

        """
        self.words = []

        wordsTemp1 = open(filename, "r")
        wordsTemp2 = wordsTemp1.readlines()

        for line in wordsTemp2:
            self.words.append(line.strip())
        self.words.sort()

    def createElements(self):
        """ Creates all tkinter elements for the app """

        # Dropdowns

        self.letterInput = ttk.Combobox(self.root, textvariable=self.letter, width=2, font=("Arial Black", 14), justify="center",
                                        values=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                                        "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])

        self.letterInput.place(relx=.175, rely=.075, anchor="center")

        self.colInput = ttk.Combobox(self.root, textvariable=self.confirm, width=13, font=("Arial Bold", 14), justify="center",
                                values=["is in column", "isn't in column"])

        self.colInput.place(relx=.5, rely=.075, anchor="center")

        self.posInput = ttk.Combobox(self.root, textvariable=self.position, state="", width=2, font=("Arial Black", 14), justify="center",
                                values=self.posOptions)
        self.posInput.place(relx=.825, rely=.075, anchor="center")

        # Buttons

        addButton = Button(self.root, text="Add", width=9, font=("Arial Bold", 12),
                            bd=0, fg="white", bg="#272b32", activeforeground="green", activebackground="green",
                            command=lambda: self.addFilter(int(self.position.get()) - 1, (self.letter.get()).lower()))
        addButton.place(relx=.35, rely=.175, anchor="center")

        resetButton = Button(self.root, text="Reset", width=9, font=("Arial Bold", 12),
                            bd=0, fg="white", bg="#272b32", activeforeground="#272b32", activebackground="#2a3037",
                            command=self.reset)
        resetButton.place(relx=.65, rely=.175, anchor="center")

        # Letters

        self.letters = []
        self.lettersBG = []
        xPos = .18

        for i in range(5):
            self.lettersBG.append(Canvas(self.root, width=45, height=45, bg="#272b32", highlightthickness=0))
            self.letters.append(Label(self.root, text="?", fg="white", bg="#272b32", font=("Arial Black", 20)))

            self.lettersBG[i].place(relx=xPos, rely=.31, anchor="center")
            self.letters[i].place(relx=xPos, rely=.31, anchor="center")
            xPos += .16

        # Possible Answers

        self.output = Text(self.root, state="disabled", wrap="word", height=11, width=35, fg="white", bg="#272b32",
                            font=("Arial Bold", 12))
        self.output.place(relx=.5, rely=.68, anchor="center")

    def addFilter(self, posIndex, letterToFind):
        """
        Adds a hint that filters the possible words that the answer could be

        Parameters
            (int) posIndex: The index (0-4) of the new filter
            (char) letterToFind: The letter to find in the new filter

        """

        self.letters[posIndex].config(text=self.letter.get())

        if self.confirm.get() == "is in column":
            # Updates position dropdown
            self.posOptions.remove(str(posIndex + 1))
            self.posInput.config(values=self.posOptions)

            # Changes letter and BG to green
            self.lettersBG[posIndex].config(bg="#558d4e")
            self.letters[posIndex].config(bg="#558d4e")

            # Removes all words that don't have the letter in right spot
            i = 0
            while i < len(self.words):
                if self.words[i][posIndex] != letterToFind:
                    self.words.remove(self.words[i])
                    i -= 1 # Goes back after removing it
                i += 1
        else:
            # Changes letter and BG to yellow
            self.lettersBG[posIndex].config(bg="#b59f3b")
            self.letters[posIndex].config(bg="#b59f3b")

            # Removes all words that have the letter in the right spot or don't have the letter at all
            i = 0
            while i < len(self.words):
                if self.words[i].find(letterToFind) == -1 or self.words[i][posIndex] == letterToFind:
                    self.words.remove(self.words[i])
                    i -= 1  # Goes back after removing it
                i += 1

        # Refreshes dropdowns
        self.letterInput.current(0)
        self.posInput.current(0)

        # Refreshes output box
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert(INSERT, (", ".join(self.words)))
        self.output.config(state="disabled") # User can't type in it

    def reset(self):
        """ Resets the entire program to start from scratch """

        for char in self.letters:
            char.config(text="?", bg="#272b32")

        for char in self.lettersBG:
            char.config(bg="#272b32")

        self.setupWordsList("words.txt")
        self.posOptions = ['1', '2', '3', '4', '5']
        self.posInput.config(values=self.posOptions)

        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.config(state="disabled")

        self.letterInput.current(0)
        self.posInput.current(0)
        self.colInput.current(0)

def main():
    s = Solver()
    s.root.mainloop()

if __name__ == '__main__':
    main()
