
import unittest
from juego import Game


class GameTests(unittest.TestCase):

    def piedra_tests(self):
        game = Game()
        self.assertEquals(game.play("piedra", "piedra"), "Empate.")
        self.assertEquals(game.play("piedra", "tijera"), "Gana jugador 1.")
        self.assertEquals(game.play("piedra", "lagarto"), "Gana jugador 1.")
        self.assertEquals(game.play("piedra", "papel"), "Gana jugador 2.")
        self.assertEquals(game.play("piedra", "spock"), "Gana jugador 2.")

    def papel_tests(self):
        game = Game()
        self.assertEquals(game.play("papel", "papel"), "Empate.")
        self.assertEquals(game.play("papel", "piedra"), "Gana jugador 1.")
        self.assertEquals(game.play("papel", "spock"), "Gana jugador 1.")
        self.assertEquals(game.play("papel", "lagarto"), "Gana jugador 2.")
        self.assertEquals(game.play("papel", "tijera"), "Gana jugador 2.")

    def tijera_tests(self):
        game = Game()
        self.assertEquals(game.play("tijera", "tijera"), "Empate.")
        self.assertEquals(game.play("tijera", "papel"), "Gana jugador 1.")
        self.assertEquals(game.play("tijera", "lagarto"), "Gana jugador 1.")
        self.assertEquals(game.play("tijera", "spock"), "Gana jugador 2.")
        self.assertEquals(game.play("tijera", "piedra"), "Gana jugador 2.")

    def lagarto_tests(self):
        game = Game()
        self.assertEquals(game.play("lagarto", "lagarto"), "Empate.")
        self.assertEquals(game.play("lagarto", "papel"), "Gana jugador 1.")
        self.assertEquals(game.play("lagarto", "spock"), "Gana jugador 1.")
        self.assertEquals(game.play("lagarto", "tijera"), "Gana jugador 2.")
        self.assertEquals(game.play("lagarto", "piedra"), "Gana jugador 2.")

    def spock_tests(self):
        game = Game()
        self.assertEquals(game.play("spock", "spock"), "Empate.")
        self.assertEquals(game.play("spock", "tijera"), "Gana jugador 1.")
        self.assertEquals(game.play("spock", "piedra"), "Gana jugador 1.")
        self.assertEquals(game.play("spock", "papel"), "Gana jugador 2.")
        self.assertEquals(game.play("spock", "lagarto"), "Gana jugador 2.")

    def wrong_options_tests(self):
        game = Game()
        self.assertEquals(game.play("some", "option"), "Opciones incorrectas.")
        self.assertEquals(game.play("piedra", "some"), "Opciones incorrectas.")
        self.assertEquals(game.play("option", "papel"), "Opciones incorrectas.")
