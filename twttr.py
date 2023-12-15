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