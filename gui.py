import tkinter as tk
import random

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.word = random.choice(['python', 'hangman', 'computer', 'programming', 'developer', 'debugging'])
        self.remaining_attempts = 6
        self.guessed_letters = []

        self.draw_word()
        self.draw_gallows()

        self.message_label = tk.Label(master, text="")
        self.message_label.pack()

        self.input_label = tk.Label(master, text="Guess a letter:")
        self.input_label.pack()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

    def draw_word(self):
        self.word_display = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.canvas.create_text(200, 50, text=self.word_display, font=("Arial", 24), tag="word")

    def draw_gallows(self):
        self.canvas.create_line(100, 300, 300, 300, width=5, tag="gallows_base")
        self.canvas.create_line(200, 300, 200, 100, width=5, tag="gallows_upright")
        self.canvas.create_line(200, 100, 300, 100, width=5, tag="gallows_crossbar")
        self.canvas.create_line(300, 100, 300, 150, width=5, tag="gallows_rope")

    def draw_head(self):
        self.canvas.create_oval(275, 150, 325, 200, width=5, tag="head")

    def draw_body(self):
        self.canvas.create_line(300, 200, 300, 250, width=5, tag="body")

    def draw_left_arm(self):
        self.canvas.create_line(300, 225, 275, 200, width=5, tag="left_arm")

    def draw_right_arm(self):
        self.canvas.create_line(300, 225, 325, 200, width=5, tag="right_arm")

    def draw_left_leg(self):
        self.canvas.create_line(300, 250, 275, 300, width=5, tag="left_leg")

    def draw_right_leg(self):
        self.canvas.create_line(300, 250, 325, 300, width=5, tag="right_leg")

    def make_guess(self):
        guess = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)

        if guess in self.guessed_letters:
            self.message_label.config(text="You already guessed that letter.")
            return

        self.guessed_letters.append(guess)

        if guess in self.word:
            self.message_label.config(text=f"Correct guess: '{guess}'")
            if self.check_win():
                self.message_label.config(text="Congratulations! You win!")
            else:
                self.draw_word()
        else:
            self.remaining_attempts -= 1
            self.message_label.config(text=f"Incorrect guess: '{guess}'")
            self.draw_hangman()

            if self.remaining_attempts == 0:
                self.message_label.config(text=f"You lost! The word was: {self.word}")

    def draw_hangman(self):
        if self.remaining_attempts == 5:
            self.draw_head()
        elif self.remaining_attempts == 4:
            self.draw_body()
        elif self.remaining_attempts == 3:
            self.draw_left_arm()
        elif self.remaining_attempts == 2:
            self.draw_right_arm()
        elif self.remaining_attempts == 1:
            self.draw_left_leg()
        elif self.remaining_attempts == 0:
            self.draw_right_leg()

    def check_win(self):
        return all(letter in self.guessed_letters for letter in self.word)


def main():
    root = tk.Tk()
    hangman_game = HangmanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
