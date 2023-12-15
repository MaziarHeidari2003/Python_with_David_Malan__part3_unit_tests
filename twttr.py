"""
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

"""

def main():
  msg = input('Enter the phrase: ')
  msg_shorten = shorten(msg)
  print(msg_shorten)


def shorten(msg):
  new_msg = ''
  for char in msg:
    if not char.lower() in ['a','e','i','o','u','y']: 
      new_msg = new_msg + char
    
  return new_msg     

if __name__ == '__main__' :
  main()