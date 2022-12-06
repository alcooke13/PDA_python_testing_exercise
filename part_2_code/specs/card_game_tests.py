import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
   def setUp(self):
      self.card_1 = Card("Hearts", 8)
      self.card_2 = Card("Spades", 10)
      self.card_3 = Card("Hearts", 10)
      self.card_4 = Card("Spades", 1)
      self.card_game_1 = CardGame()

   def test_check_for_ace_true(self):
      results = self.card_game_1.check_for_ace(self.card_4)
      self.assertEqual(True, results)

   def test_check_for_ace_false(self):
      results = self.card_game_1.check_for_ace(self.card_2)
      self.assertEqual(False, results)

   # def test_card_returns_highest_value(self):
   #    results = self.card_game_1.highest_card(self.card_1, self.card_2)
   #    self.assertEqual(self.card_2, results)

   # def test_totalling_of_cards(self):
   #    card_list = [self.card_1, self.card_2, self.card_3]
   #    results = self.card_game_1.cards_total(card_list)
   #    self.assertEqual("You have a total of 28", results)
