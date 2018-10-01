# -*- coding: utf-8 -*-


class Game:
    """
    Juego clásico de Piedra, Papel, Tijera, Lagarto, Spock.
    """

    def __init__(self):
        self.cards = []
        self.game_play = {}
        self.__initialize_game()

    def __initialize_game(self):
        """
        Inicializa las variables y reglas del juego.
        """
        pi, pa, ti, la, sp = "piedra", "papel", "tijera", "lagarto", "spock"
        self.cards = [pi, pa, ti, la, sp]
        self.game_play = {
            pi: [ti, la], pa: [pi, sp], ti: [pa, la], la: [pa, sp], sp: [pi, ti]
        }

    def play(self, str1, str2):
        """
        Método principal para evaluar que jugador gana.
        :param str1: string, Palabra usada por jugador 1.
        :param str2: string, Palabra usada por jugador 2.
        :return: string, el resultado final del juego.
        """
        if str1 not in self.cards or str2 not in self.cards:
            return "Opciones incorrectas."
        return "Empate." if str1 == str2 else "Gana jugador 1." \
            if str2 in self.game_play[str1] else "Gana jugador 2."


if __name__ == "__main__":
    game = Game()
    # Ejemplo de juego
    print game.play("lagarto", "papel")
