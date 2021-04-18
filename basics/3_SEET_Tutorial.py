# SET: unordered, unique (no duplicates), elements in sets hashable
# Grundlagen: Sets sind Megenlehre! 
x=set({'Name':'Andreas', 'Nachname':'Pinheiro'})
print (x) #only keys in sets
y= {'foo', 'bar'} # creation of a set
z=set() #empty set
print (f''' {y} is a new set
    {type(z)} is a empty set. ''')

# iterate tru set
for element in y:
    print (element)

# union, difference, intersection
print("*"*30, "UNION", "*"*30) 
x1={'Andreas', 'Klaus', 'Rainer', 'Peter'}
x2={'Andreas', 'Annabelle', 'Naomi', 'Paul'}
print (x1 | x2) # union von x1 und x2
print(x1.union(x2))# same same
print("*"*30, "Intersection", "*"*30) 
print (x1 & x2) #intersection (gemeinsame Menge) von x1 und x2
print(x1.intersection(x2)) # Gemeinsame Menge der SETS
print("*"*30, "Difference", "*"*30) 
print(x1 - x2) # Die elemente, die nur in x1 existieren und in keinem anderen SET
print(x1.difference(x2))
print("*"*30, "Symetric Difference", "*"*30) 
print (x1 ^x2) # Gegenteil von Intersection
print (x1.symmetric_difference(x2))

#Teilmengen überschiessende Teilmengen
print("*"*30, "Subset", "*"*30) 
x1={1, 2, 3, 4, 5 }
x2={1, 2, 3, 4, 5, 6}
print(x1<=x1) # ist x1 eine Teimenge von x2? subsetz
print("*"*30, "Superset", "*"*30) 
print(x2.issuperset(x1))

#modify an set
x1={'Andreas', 'Klaus', 'Rainer', 'Peter'}
x2={'Andreas', 'Annabelle', 'Naomi', 'Paul'}
print("*"*30, "adding, removing", "*"*30) 
x1.add('Added_Person')
print (x1)
x1.remove('Added_Person')
print (x1)
x1.discard('Added_Person') #removes Added_Person if in set, otherwise does nothing
print(x1.pop()) #pop selects random set value and deletes it
print("*"*30, "Update-Method", "*"*30) 
x1.update(x2)
print (x1)
x1.intersection_update(x2) # only elements that are in list x2 and x1 
print (x1)
x1.difference_update(x2) # only elemts in x1 not in x2
print (x1)
print("*"*30, "Frozen Set", "*"*30) 
x3=frozenset({'foo', 'bar', 'baz'}) # no adding etc. possible
x4={2, 5, x3} #frozenset can be part of a set
print(x4)
