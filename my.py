from math import floor

toCelcius = {
  'C': lambda t:t,
  'F': lambda t:(t - 32) * 5 / 9,
  'K': lambda t:t - 273.15,
  'R': lambda t:(t - 491.67) * 5 / 9,
  'De': lambda t:100 - t * 2 / 3,
  'N': lambda t:t * 100 / 33,
  'Re': lambda t:t * 5 / 4,
  'Ro': lambda t:(t - 7.5) * 40 / 21
}

fromCelcius = {
  'C': lambda t:t,
  'F': lambda t:t * 9 / 5 + 32,
  'K': lambda t:t + 273.15,
  'R': lambda t:(t + 273.15) * 9 / 5,
  'De': lambda t:(100 - t) * 3 / 2,
  'N': lambda t:t * 33 / 100,
  'Re': lambda t:t * 4 / 5,
  'Ro': lambda t:t * 21 / 40 + 7.5
}

def convert_temp(n,f,t):
    if f==t:
        return n
    n=fromCelcius[t](toCelcius[f](n))
    v=n<0
    n=abs(n)
    return -floor(n) if v else floor(n)

print(convert_temp(100, "C", "F"))