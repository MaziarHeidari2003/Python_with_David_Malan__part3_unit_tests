import sys

def main():
  fraction = input('Enter the amount of fuel: ')
  percentage = convert(fraction)
  print(gauge(percentage))
  
  


def convert(fraction):
 while True: 
    try:
      x,y = fraction.split('/')
      a = int(x)
      b = int(y)
      percentage = (a/b)*100
      if percentage > 100 :
        fraction = input('Enter the amount of fuel: ')
      else:
        return percentage  
    except (ZeroDivisionError, ValueError):
      raise
      

def gauge(percentage):
  if percentage <= 1 :
    return 'E'
  if percentage >= 99 :
    return 'F'
  return f"{percentage}%"


if __name__ == "__main__":
  main()