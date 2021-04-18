import tkinter as tk
import tkinter.messagebox
import re

def value_check(column, value):
    if column=='dp_date':
        entry=re.search(r'\w\w\w\d\d', value)
        if entry: 
            year_2d=int(value[-2:])
            year=int(('%i%i' % (20, year_2d)))
            month_raw=value[:3]
            month=trans_date(month_raw)
            value_date=f'''"{('%i%s' % (year, month))}"'''
            print (value_date)
            return value_date
        elif entry==None: 
            tk.messagebox.showinfo(title="Auswahl", message="Ihre Eingabe muss in dem Format MMMYY \
                (bspw.: MAY20 für Mai 2020) erfolgen")
            value="EXIT"
            return value
    else:
        return value
# dienstplan.station <> 'FRA' and 
        # dienstplan.station <> 'MUC'
        #pk TEXT,
        #station TEXT,
        #flotte TEXT, 
        #dp_vpap TEXT,
        #dp_date NUMERIC,
        #fctn TEXT, 
        #lsw REAL,
        #bzw REAL, 
        #frei_t INTEGER, 
        #plus_t INTEGER,
        #0 off INTEGER,
        #1 OT INTEGER, 
        #2 REP INTEGER,
        #3 STBY INTEGER,
        #3 SIM INTEGER,
        #5 Urlaub INTEGER,
        #6 schulung INTEGER,
        #7 TK_day INTEGER,
        #8 Grndcrse INTEGER, 
        #9 tzlsw INTEGER,
        #10 tzbzw INTEGER, 
        #11  boden INTEGER, 
        #12 krank INTEGER, 
        #13 x1 integer,

def falsche_eingabe():
    #tk.messagebox.showinfo(title="Auswahl", message="Ihre Eingabe war fehlerhaft")
    pass

def trans_date(month_raw):
    if month_raw=='JAN':      
        month = "-01-01 00:00:00 UTC"
        return month
    elif month_raw== 'FEB':
        month = "-01-02 00:00:00 UTC"
        return month
    elif month_raw== 'MAR':
        month = "-01-03 00:00:00 UTC"
        return month
    elif month_raw== 'APR':
        month = "-01-04 00:00:00 UTC"
        return month
    elif month_raw== 'MAY':
        month = "-01-05 00:00:00 UTC"
        return month
    elif month_raw== 'JUN':
        month = "-01-06 00:00:00 UTC"
        return month
    elif month_raw== 'JUL':
        month = "-01-07 00:00:00 UTC"
        return month
    elif month_raw== 'AUG':
        month = "-01-08 00:00:00 UTC"
        return month
    elif month_raw== 'SEP':
        month = "-01-09 00:00:00 UTC"
        return month
    elif month_raw== 'OCT':
        month = "-01-10 00:00:00 UTC"
        return month
    elif month_raw== 'NOV':
        month = "-01-11 00:00:00 UTC"
        return month
    elif month_raw== 'DEC':
        month = "-01-12 00:00:00 UTC"
        return month

 

if (__name__=='__main__'):
    #value_check('dp_date', 'JUN20')
    pass