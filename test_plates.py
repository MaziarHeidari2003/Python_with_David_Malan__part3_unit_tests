"""
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":
"""

from plates import plate_check

def main():
  test_length()
  test_num_place()
  test_starting_two_letters()
  test_punctuation()
  test_number_zero()


def test_length():
  assert plate_check('AA') == True
  assert plate_check('abcdef') == True
  assert plate_check('BBBBBBB') == False
  assert plate_check('B') == False

def test_num_place():
  assert plate_check('aaa22') == True
  assert plate_check('a4as') == False  

def test_starting_two_letters():
  assert plate_check('aa') == True
  assert plate_check('a2') == False
  assert plate_check('2a') == False
  assert plate_check('22') == False

def test_number_zero():
  assert plate_check('cs50') == True
  assert plate_check('aa05') == False

def test_punctuation():
  assert plate_check('pi,12') == False
  assert plate_check('pi?s') == False
  assert plate_check('pi 12') == False







if __name__ == '__main__':
  main()