import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(player1_guess, CPU_guess):
    if player1_guess == CPU_guess:
        return "It's a tie!", 0, 0
    elif (player1_guess == "R" and CPU_guess == "S") or \
         (player1_guess == "S" and CPU_guess == "P") or \
         (player1_guess == "P" and CPU_guess == "R"):
        return "You win!", 1, 0
    else:
        return "CPU wins!", 0, 1

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.player1 = ""
        self.player2 = "CPU"

        self.player1_score = 0
        self.player2_score = 0
        self.round_count = 0
        self.max_rounds = 5

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter your name:")
        self.label.pack(pady=10)

        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.round_label = tk.Label(self.root, text="Round: 0")
        self.round_label.pack()

        self.choice_label = tk.Label(self.root, text= f"This is a set of rounds. You can play upto 5 times in a set. \nChoose: R for Rock, S for Scissors, P for Paper")
        self.choice_label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_round, state=tk.DISABLED)
        self.play_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.score_label = tk.Label(self.root, text="")
        self.score_label.pack()

    def start_game(self):
        self.player1 = self.entry_name.get().upper()
        if not self.player1:
            tk.messagebox.showerror("Error", "Please enter your name.")
            return
        self.label.destroy()
        self.entry_name.destroy()
        self.start_button.destroy()
        self.round_label.config(text=f"Round: {self.round_count + 1}")
        self.label = tk.Label(self.root, text=f"Welcome, {self.player1}!")
        self.label.pack(pady=10)
        self.play_button.config(state=tk.NORMAL)

    def play_round(self):
        player1_guess = self.entry.get().upper()

        if player1_guess not in ["R", "S", "P"]:
            self.result_label.config(text="ERROR, WRONG OPTION. TRY AGAIN")
            return

        CPU_guess = random.choice(["R", "S", "P"])

        result, round_player1_score, round_player2_score = determine_winner(player1_guess, CPU_guess)
        self.player1_score += round_player1_score
        self.player2_score += round_player2_score
        self.round_count += 1
        self.round_label.config(text=f"Round: {self.round_count + 1}")

        self.display_choices(player1_guess, CPU_guess)
        self.display_result(result)
        self.display_scores(result)
        

        if self.round_count == self.max_rounds:
            self.round_count = 0
            self.play_button.config(state=tk.DISABLED)
            self.display_final_scores()
            play_again = tk.messagebox.askquestion("Play Again", "Do you want to play again?")
            if play_again == 'yes':
                self.reset_scores()
                self.round_label.config(text=f"Round: 1")
                self.play_button.config(state=tk.NORMAL)
            if play_again=="no":
                self.root.destroy()

    def display_choices(self, player1_guess, CPU_guess):
        choices_text = f"{self.player1}'s choice: {player1_guess}\n{self.player2}'s choice: {CPU_guess}"
        self.result_label.config(text=choices_text)

    def display_result(self, result):
        self.score_label.config(text=result)

    def display_scores(self, result):
        scores_text = f" {result} - {self.player1}: {self.player1_score}, {self.player2}: {self.player2_score}"
        self.score_label.config(text=scores_text)

    def display_final_scores(self):
        
        if self.player1_score > self.player2_score:
            result= "You win"
        elif self.player1_score < self.player2_score:
            result = "CPU wins"
        else:
            result = "It's a draw"
        final_scores_text = f"FINAL SCORES: {result} - {self.player1}: {self.player1_score}, {self.player2}: {self.player2_score}"
        self.result_label.config(text=final_scores_text)

    def reset_scores(self):
        self.player1_score = 0
        self.player2_score = 0


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
