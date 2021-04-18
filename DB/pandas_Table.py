import requests
import pandas as pd
import tkinter as tk
from pandastable import Table



def show_data(data):
    class ShowApp(tk.Frame):
        def __init__(self, parent=None):
            self.parent = parent
            tk.Frame.__init__(self)
            self.main=self.master
            self.main.geometry('500x500')
            f=tk.Frame(self.main)
            f.pack(fill=tk.BOTH, expand=1)
            self.table = pt = Table(f, dataframe=data, showtoolbar=True, showstatusbar=True)
            pt.show()
    app=ShowApp()
    app.mainloop()


#download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
#target_csv_path = "nba_all_elo.csv"

#response = requests.get(download_url)
#response.raise_for_status()    # Check that the request was successful
#with open(target_csv_path, "wb") as f:
#    f.write(response.content)
#print("Download ready.")
nba = pd.read_csv("nba_all_elo.csv")
data=pd.DataFrame(nba)
print (data)
show_data(data)




