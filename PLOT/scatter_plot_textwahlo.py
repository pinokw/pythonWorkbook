import matplotlib.pyplot as plt
import numpy as np

class Post():
    
    def __init__(self, thema, attack_rate, pro, con, cmpy):
        self.thema=thema
        self.attack_rte=attack_rate
        self.pro=pro
        self.con=con
        self.cmpy=cmpy

    def zust_rte(self):
        self.zust_rte=self.pro-self.con

    def size(self):
        if self.pro==0 and self.con==0:
            self.size=1
        else:
            self.size=(self.con+self.pro)*30

    def color(self):
        if self.cmpy=="GWI":
            self.color=20
        elif self.cmpy=="DLH":
            self.color=50
        elif self.cmpy=="LCAG":
            self.color=80


if (__name__=='__main__'):
    post_lst=(['Wahlomat', 20, 9, 0, 'LCAG'],\
        ['Wahlomat', 80, 3, 0, 'GWI'], \
        ['Wahlomat', 90, 8, 19, 'GWI'],
        ['Wahlomat', 90, 8, 3, 'GWI'], 
        ['Wahlomat', 30, 21, 0, 'DLH'])
    analy_lst=[]
    x_lst=[]
    y_lst=[]
    clr_lst=[]
    size_lst=[]
    for entry in post_lst:
        post=Post(entry[0], entry[1], entry[2], entry[3], entry[4])
        post.zust_rte()
        post.color()
        post.size()
        analy_lst.append(post)
    for pst in analy_lst:
        x_lst.append(pst.attack_rte)
        y_lst.append(pst.zust_rte)
        clr_lst.append(pst.color)
        size_lst.append(pst.size)

    x = np.array(x_lst)
    y = np.array(y_lst)
    sizes = np.array(size_lst)
    colors = np.array(clr_lst)

    plt.scatter(x, y, s=sizes, c=colors, cmap='RdYlBu') #,
    plt.text(10, 80, "Test", color = 'green', fontsize = 15)

    plt.show()