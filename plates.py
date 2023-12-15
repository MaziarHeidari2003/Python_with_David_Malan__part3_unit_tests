"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""


def main():
  plate = input('Enter the plate t obe checked: ')
  if  plate_check(plate) :
    print('Valid')
  else:
    print('Invalid')  


def plate_check(plate):
  if len(plate) > 6 or len(plate) < 2 :
    return False
  

  for i in range(len(plate)):
    #if plate[i] in ['0','1','2','3','4','5','6','7','8','9'] :
     # if i == len(plate)-1 :
        #break
      #elif not plate[i+1] in ['0','1','2','3','4','5','6','7','8','9'] :
         #return False
    
    if plate[i].isdigit():
      if not plate[i:].isdigit():
        return False
      

  if plate[0].isalpha() == False or plate[1].isalpha() == False :
    return False    

  for char in plate:
    if char.isalpha() == False:
      if char == '0':
        return False
      else:
        break
    
  for char in plate :
    if char in [',','?',' ','.'] :
      return False
    
  return True  
 
if __name__ == '__main__' :
  main()
