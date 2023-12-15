"""
In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

"""


def main():
  greeting = input('Greeting: ')
  value_to_print = value(greeting)
  print(f'${value_to_print}')


def value(greeting): 
  value = 0
  greeting = greeting.lower().strip()
  if 'hello' in greeting  :
    return value
  elif greeting[0] == 'h' :
    value = 20
    return value
  else:
    value = 100
    return value


if __name__ == '__main__' :
  main()