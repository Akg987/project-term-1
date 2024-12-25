from tkinter import *

import buget
from pl import mainscrean
from be.database import dbContext
from buget import MoneyTankAnimation
if __name__=="__main__":
    db=dbContext()
    screen=Tk()
    screen.geometry("1090x520")
    screen.title("مدیریت هزینه ها")
    screen.resizable(False,False)
    screen.iconbitmap("icon.ico")
    PageMe=mainscrean.App(screen)
    PageMe1=buget.main(screen)
    screen.mainloop()