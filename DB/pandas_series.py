from pandas import DataFrame, Series
import random
from pandas import date_range

s=Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print (s)
print (s.mean())

# Create some random data
data = [random.randint(0,10000) for x in range (10000)]
# Create datetime Index, providing start and freq
index = date_range(start='01-01-2013', periods=len(data), freq='T')
s = Series(data, index=index)
print (s.tail())