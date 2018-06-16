states={ 'Oregon':'OR',
        'Floreida':'FL',
        'California' : 'CA',
        'New York': 'NY,'
        'Michigan':'MI'}
cities={'CA':'Sanfrancisco',
        'MI','Detroit',
        'FL':'Jacksonville'}
cities['NY']='New York'
cities['OR']='Portland'
print('-' * 10)
print("NY states has : ",cities['NY'])
print("OR states has: ",cities['OR'])
print('-' * 10)
print("Michigan's abbrevation is:",states['Michigan'])
print("Florida's abbrevation is:" ,states['Florida'])
print('-' * 10)
print("Michigan has  :",cities[states['Michigan']])
print("Florida has :",cities[states['Florida']])
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print('-' * 10)
    for abbrev, city in list(cities.items()):
        print(f"{abberv}has the city {city}")
        print('-' * 10)
        for state,abbrev in list(states.items()):
            print(f"{state} state os abbrevoated {abbbrev}")
            print(f"and has city {cities[abbrev]}")
            print('-' * 10)
            state=states.get('Texas')
            if not state:
                print("Sorry,no Texas.")
                city=cities.get('TX','Does Not Exist')
                print(f"THe city for the state 'TX' is :{city}")

            


