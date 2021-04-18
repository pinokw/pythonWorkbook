#####################################################
#   TEMPLATE - XLS import und Berechnung
#
#   Jedes Sheet eines XLS wird als KEY in ein DICT importiert
#
#   Jede Zeile in einem Sheet ist ein DICT mit dem Spaltennamen als KEY
#
########################################################

import os, sys
from pkg import *
fileDir = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(fileDir)

xlslist=[]
xls_folder = os.path.join(fileDir, 'read_xls_tmpl', 'xls')
for file in os.listdir(xls_folder):
    if file.endswith(".xlsx"):
        xlslist.append(os.path.join(xls_folder, file))

class Person():

    def __init__(self, data):
        pk=[value for key, value in data.items() if key=='pk'] # jede Zeile ist ein DICT mit den entsprechenden Spaltennamen als ky
        self.pk= pk[0]
        station=[value for key, value in data.items() if key=='station'] # jede Zeile ist ein DICT mit den entsprechenden Spaltennamen als ky
        self.station= station[0]
        flotte=[value for key, value in data.items() if key=='flotte'] # jede Zeile ist ein DICT mit den entsprechenden Spaltennamen als ky
        self.flotte= flotte[0]
    
def attributes(data):
    attributes=[k for k, v in data.items()]
    return attributes

xls_input = xlslist[0] # nur das oberste XLS wird genommen
xls_data=read_xls.readxls_main(xls_input)
person_input=[]
for key, value in xls_data.items(): # KEYs sind die Namen der Sheets
    if key == "BZW": # Nur ein Sheet wird betraachtet (optional)
        for entry in value:
            person=Person(entry)
            person_input.append(person)
            header=attributes(entry)

# Hier passiert irgendetwas mit den input-Werten....

# Ausgabe des XLS exemplarisch mit den input werten
write_xls.print_xls(person_input, header)






