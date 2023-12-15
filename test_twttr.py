from twttr import shorten

def main():
  test_upper_lower_case()
  test_numbers()


def test_upper_lower_case():
  assert shorten('twitter') == 'twttr'
  assert shorten('TWITTER') == 'TWTTR'
  assert shorten('TwiItTR') == 'TwtTR'

def test_numbers():
  assert shorten('1234') == '1234'  

def test_panctuation():
  assert shorten('?/;,') == '?/;,'  

if __name__ == '__main__' :
  main()    