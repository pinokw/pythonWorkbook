bad_guys = {
    'daredevil' : 'kingpin',
    'x-men': 'apocalypse',
    'batman':'joker'
}

bad_guys['asterix'] = 'cesar' # create new entry
print (bad_guys)
bad_guys['batman']='bane' #update 
print (bad_guys)
del bad_guys['x-men'] # delete
print (bad_guys)

# growing a dictonary
my_profile ={}
my_profile['fName']='Andreas'
my_profile['lName']='Pinheiro'
my_profile['city']='Cologne'
print (my_profile)
my_profile['children']=['Paul', 'Naomi', 'Claire'] #list within dictionary
print(my_profile)

#Nesting Dict within Dict
my_profile['jobs']={'First Officer': 'Condor', "Senior FO":'Lufthansa', 'Captain': 'Lufthansa'} 
print (my_profile)
print (my_profile['children'][1])# access index in List
print (my_profile['jobs']['First Officer']) #access entry within nested dict

# restriction: 
# KEY only usable once
# KEYs mus be immutable (no Lists, but Tuples)

# operators and functions
# check existing of keys
if 'city' in my_profile: 
    print ('Die Stadt kommt als key vor')
print (my_profile.get("Andreas"))
print (my_profile.get('Annabelle'))

# items in tuple-form into dict-view object 
print (my_profile.items()) # NO ACCESS to Dictionary! 
for i in my_profile.items():
    print (i[1]) # der erste Index des Tuples aus der Liste wird ausgedruckt (ALSO) Das ITEM des dictionarys

# keys, items, values 
print (bad_guys.keys()) #No Access do dictionary!
print (bad_guys.items())
print (bad_guys.values())

# remove key from dict: 
print(my_profile.pop('jobs')) # retuns value
print (my_profile)

# convert dict into list (uses a lot of memory)
a = list(my_profile.keys())
print(type(a))
print (a)


# Merge and update Dictionarys
d1= {
    'a':'Robin',
    'b':'Catwoman'
}
d2 = {
    'c':"Bugs Bunny",
    'b': 'Mickey Mouse', 
    'e': 'Pinoccio'
}
d2.update (c='Duffy Duck')
print (d2)
d1.update (d2) # DICS werden gemerged "b" wird durch Mickey-Mouse ersetzt
print (d1)

#switch keys and values
new_dict={}
for key, value in d1.items(): 
    new_dict[value] = key
print (new_dict)
# better: 
new_dict2={value: key for key, value in d1.items()}
print (new_dict2)

#Merge 2 lists into dict mit ZIP
e1 = ['Deutschland', 'Frankreich', 'Italien']
e2 = ['80 Millionen', '60 Million', '50 Million']
country_dict = {key: value for key, value in zip(e1, e2)}
print (country_dict)

#filter items in dictionary
f1 = {'eins':1, 'zwei':2, 'drei':3}
filter_dict = {key:value for key, value in f1.items() if value >2}
print (filter_dict)

#Summieren von values in Dictionarys
print (sum([value for value in f1.values()]))
print (sum(f1.values()))

#sort by keys
income={'Paul':75000, 'Andreas':10000, 'Annabelle':80000}
sorted_income={k: income[k] for k in sorted(income)}
print (sorted_income)

# popitem - pops items (randomly) and deletes it, 
# Am ende hat man ein dictionary, welches leer ist. Das spart speicherplatz
while True: 
    try: 
        item=country_dict.popitem()
        print (item)
    except:
        print ("The dictionary ist empty")
        break

#chainmap Collections Library
# Chainmap kann mehrere Dics zusammenfügen in eine große durchsuchbare Klasse
from collections import ChainMap
chained_map=ChainMap(income, f1)
print (chained_map)
for key, value in chained_map.items():
    print (key, value)

# Itertools
# cycle geht so oft durch ein dict, wie man das will
print ("Iter Beispiel 1 cycle")
print ("*" * 30)
from itertools import cycle
num_items = 10
for item in cycle(income.items()):
    if num_items == 0:
        break
    else: 
        num_items -=1 
        print (item)
# chain: 2 Dictionarys können verbunden werden, ohne dass man ein neues kreieren muss
print ("Iter Beispiel 2 chain ")
print ("*"* 30)
from itertools import chain
for item in chain(f1.items(), income.items()):
    print (item)

#unpacking dictionary: 
print ("Unpacking beispiele")
print ("*" * 30)
for key, value in {**f1, **income}.items():
    print (key, "-->", value)
