# negativ indexing
list=['Andreas','Paul', 'Annabelle', 'Claire', 'Naomi']
print (list[-1]) # Naomi!
# länge der Liste
print(len(list))

#slicing slice Paul-CLaire 
print(list[1:4])

#slicing by 2 steps
print(list[0:5:2])
list[2:3]=['Klaus', 'Peter', 'Hans'] # index 2und 3 werden durch die neuen items ersetzt
print (list)
list[1]=['Manuel', 'Andreas', 'Guerra', 'Pinheiro'] # nummer 1 wird durch eine subliste ersetzt
print(list)
list[1:1]=['Manuel', 'Andreas', 'guerra', 'Pinheiro'] # 4 einsträge VOR Eintrag Nummer 1

# addition and multiplication
print(list * 22)
print (list+['Klaus', 'Hans']) #nur temporär!
print (list)
# print (min(list)) # lowest value first letter

#nesting (list within list)
listb=['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print (listb [1] [1]) # sublist 1 in Index 1
print('*'*30)
print (f'''listb[0]='Almanach''')
listb[0]='Almanach'
print (listb)
print ('*'*30)
print (f'''listb[1][1]=['xxx', 'yyyy', 'zzzz']''')
listb[1][1]=['xxx', 'yyyy', 'zzzz']
print (listb)
print('*'*30)

# LIST Methods
listb.append('appended Object') 
print (listb)
listb.extend('Hallo') # iterable wird hinzugefügt - ähnlich listb + "Hello"
print (listb)
listb.insert(2, 'hello') # "hello" wird am index 2 hinzugefügt
print (listb)
listb.remove('appended Object')
print (listb)
listb.clear()
print (listb)

# sort
list.sort
print (list)

#List Methods with return values
print (list.pop()) # last item in list is taken and deleted! Default is -1
print  (list)
print (list.index("Andreas", 0, 5)) #return of index of a value betwenn 0, 5
print (list.count("Andreas")) # Zählt einen Eintrag in der liste

b= list.copy() # First Layer will be copied der Rest wird nur referenziert (Sublist) s. bspw.
print (b)
b [5][1] = 'Nur Referenz'
print (b)
print (list) # ---> ' Nur Referenz ist in einer Sublist und wird in b nur "referenziert"
