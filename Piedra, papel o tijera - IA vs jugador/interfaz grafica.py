import random
import tkinter as tk
from tkinter import messagebox

class LearningComputer:
    def __init__(self):
        self.moves = ['piedra', 'papel', 'tijera']
        self.history = {'piedra': {'piedra': 0, 'papel': 0, 'tijera': 0},
                        'papel': {'piedra': 0, 'papel': 0, 'tijera': 0},
                        'tijera': {'piedra': 0, 'papel': 0, 'tijera': 0}}
        self.prev_player_move = None

    def make_move(self):
        if self.prev_player_move is None or sum(self.history[self.prev_player_move].values()) == 0:
            return random.choice(self.moves)
        
        last_move = max(self.history[self.prev_player_move], key=lambda key: self.history[self.prev_player_move][key])
        return self.beat(last_move)

    def beat(self, move):
        return {'piedra': 'papel', 'papel': 'tijera', 'tijera': 'piedra'}[move]

    def learn(self, player_move):
        if self.prev_player_move is not None:
            self.history[self.prev_player_move][player_move] += 1
        self.prev_player_move = player_move

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")

        self.computer = LearningComputer()
        self.player_score = 0
        self.computer_score = 0

        self.label = tk.Label(root, text="Elige piedra, papel o tijera:")
        self.label.pack()

        self.buttons = []
        for move in self.computer.moves:
            button = tk.Button(root, text=move, command=lambda m=move: self.play(m))
            button.pack()
            self.buttons.append(button)

        self.score_label = tk.Label(root, text="Marcador: Jugador 0 - Computadora 0")
        self.score_label.pack()

    def play(self, player_move):
        computer_move = self.computer.make_move()

        if player_move == computer_move:
            result = "Empate"
        elif self.computer.beat(player_move) == computer_move:
            result = "Gana la computadora"
            self.computer_score += 1
            self.computer.learn(player_move)
        else:
            result = "Ganas tú"
            self.player_score += 1
            self.computer.learn(player_move)

        self.score_label.config(text=f"Marcador: Jugador {self.player_score} - Computadora {self.computer_score}")
        messagebox.showinfo("Resultado", f"Computadora eligió {computer_move}\n{result}")

if __name__ == "__main__":
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()
