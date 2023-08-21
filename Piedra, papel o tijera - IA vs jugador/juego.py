import random

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

def main():
    computer = LearningComputer()
    player_score = 0
    computer_score = 0

    while True:
        player_move = input("Elige piedra, papel o tijera: ").lower()
        if player_move not in computer.moves:
            print("Movimiento inválido. Intenta nuevamente.")
            continue

        computer_move = computer.make_move()
        print(f"Computadora eligió {computer_move}")

        if player_move == computer_move:
            print("Empate")
        elif computer.beat(player_move) == computer_move:
            print("Gana la computadora")
            computer_score += 1
            computer.learn(player_move)
        else:
            print("Ganas tú")
            player_score += 1
            computer.learn(player_move)

        print(f"Marcador: Jugador {player_score} - Computadora {computer_score}")
        play_again = input("¿Quieres jugar de nuevo? (s/n): ")
        if play_again.lower() != 's':
            break

if __name__ == "__main__":
    main()