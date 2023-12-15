"""
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the string passed to the value function will not contain any leading spaces. Only main should call print.
"""

from bank import value


def main():
  test_hello()
  test_beginning_h()
  test_anything_else()


def test_hello():
  assert value('its good to see you, hello there') == 0
  assert value('HeLlo my friend') == 0
  assert value('Hello my dear') == 0

def test_beginning_h():
  assert value('how are you doing today, bitch?') == 20
  assert value('Hey bitch') == 20

def test_anything_else():
  assert value('good evening') == 100
  assert value('Its Nice to see you') == 100

if __name__ == '__main__' :
  main()  