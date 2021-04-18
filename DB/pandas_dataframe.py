from pandas import DataFrame, Series
import random
#create data
data1 = [random.randint(0,10) for x in range (10)]
data2 = [random.randint(11,1000) for x in range (10)]
print (data1)

df=DataFrame({'data1':data1, 'data2':data2}) # key=coloumn
print (df)
