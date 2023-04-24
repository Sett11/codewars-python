def get_first_python(l):
    for i in l:
        if(i['language']=='Python'):
            return '{}, {}'.format(i['first_name'],i['country'])
    return 'There will be no Python developers'

print(get_first_python([
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]))