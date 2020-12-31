import pytest
from game_of_greed.game_logic import GameLogic

# Test sequence of correct length is returned
def test_sequence_length_six():
  roll = GameLogic.roll_dice(6)
  actual = len(roll)
  expected = 6
  assert actual == expected

def test_sequence_length_three():
  roll = GameLogic.roll_dice(3)
  actual = len(roll)
  expected = 3
  assert actual == expected

# Test each item in sequence is an integer with value between 1 and 6
def test_sequence_values():
  roll = GameLogic.roll_dice(6)
  assert max(roll) < 7 and min(roll) > 0

  



