from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from be.server import M_Hazine
from dal.Repository import Repository
from customtkinter import *
from Time import getTime, get_month_dates, year, getMinute, getGregorian,getDay
from jdatetime import datetime
from Time import getJalali
from bll.addplan import addplan
from be.database import dbContext
from buget import *
from datetime import datetime as dt, timedelta
from jdatetime import datetime as jdatetime
import matplotlib.pyplot as plt
import numpy as np
class App(ttk.Frame):

    def __init__(self, screen):
        super().__init__(screen)
        self.master = screen
        self.createplane()
        self.LoadDataInTable()

    def createplane(self):
        style = ttk.Style()
        style.theme_use("vista")

        # string ha
        self.WhatIsFor = StringVar()
        self.Makan = StringVar()
        self.Hazine = StringVar()
        self.Id = StringVar()
        self.title=StringVar()
        self.tarikh=IntVar()
        # Frame ha
        self.addFrame = Frame(self.master, width=390, height=520, bg="#6f8f8c").place(x=710, y=0)
        self.backFrame = Frame(self.master, width=710, height=540, bg="#1491c7").place(x=0, y=0)

        self.resultFrame = ttk.Treeview(self.backFrame, columns=("c1", "c2","c3","c4"), show="headings", height=20)
        self.resultFrame.place(x=26, y=30)
        #lbl ha

        self.resultFrame.bind("<Button-1>", self.SelectRowIntbl)

        # tbl result
        self.resultFrame.heading("# 3", text="هزینه")
        self.resultFrame.column("# 3", width=191, anchor=E)

        self.resultFrame.heading("# 2", text="تاریخ")
        self.resultFrame.column("# 2", width=222, anchor=E)

        self.resultFrame.heading("# 1", text="عنوان")
        self.resultFrame.column("# 1", width=200, anchor=E)

        self.resultFrame.heading("# 4", text="ردیف")
        self.resultFrame.column("# 4", width=52, anchor=E)

        # Entry ha
        self.entrytitle = ttk.Entry(self.addFrame, justify="center",textvariable=self.title)
        self.entrytitle.place(x=750, y=15, width=300, height=28)

        self.entryhazine = ttk.Entry(self.addFrame, justify="center",textvariable=self.Hazine)
        self.entryhazine.place(x=750, y=50, width=300, height=28)

        self.entrymakan = ttk.Entry(self.addFrame, justify="center",textvariable=self.Makan)
        self.entrymakan.place(x=750, y=85, width=300, height=28)

        self.entrywhatisfor = ttk.Entry(self.addFrame, justify="center",textvariable=self.WhatIsFor)
        self.entrywhatisfor.place(x=750, y=120, width=300, height=28)

        # Labels
        self.txttitle = ttk.Label(self.addFrame, text="عنوان")
        self.txttitle.place(x=750, y=15, width=35, height=28)
        self.entrytitle.bind("<Button-1>", self.on_click_destroytitle)
        self.entrytitle.bind("<FocusOut>", self.focusouttitle)

        self.txthazine = ttk.Label(self.addFrame, text="هزینه")
        self.txthazine.place(x=750, y=50, width=35, height=28)
        self.entryhazine.bind("<Button-1>", self.oncklickdestroyhazine)
        self.entryhazine.bind("<FocusOut>", self.Checknumber and self.focusouthazine)

        self.txtmakan = ttk.Label(self.addFrame, text="مکان")
        self.txtmakan.place(x=750, y=85, width=32, height=28)
        self.entrymakan.bind("<Button-1>", self.oncklickdestroymakan)
        self.entrymakan.bind("<FocusOut>", self.focusoutmakan)

        self.txtwhatisfor = ttk.Label(self.addFrame, text="هزینه برای چه چیزی")
        self.txtwhatisfor.place(x=750, y=120, width=96, height=28)
        self.entrywhatisfor.bind("<Button-1>", self.oncklickdestroywhatisfor)
        self.entrywhatisfor.bind("<FocusOut>", self.focusoutwhatisfor)

        # Buttons
        self.btnadd = ttk.Button(self.addFrame, text="اضافه کردن به لیست", command=self.onclicksave)
        self.btnadd.place(x=750, y=480)
        self.btnshowchart = ttk.Button(self.backFrame, text="نمایش نمودار",command=self.plot_chart)
        self.btnshowchart.place(x=26, y=457, width=668, height=60)
        self.BtnDelet = Button (self.addFrame,text="حذف" , bg = "red",fg = "black",command=self.OnClickDelet)
        self.BtnDelet.place_forget()

        self.btnupdate = Button(self.addFrame,text="آپدیت" ,bg = "green",fg = "white",command=self.onclickupdate)
        self.btnupdate.place_forget()

        self.btnshowbudget = ttk.Button(self.addFrame,text="نمایش بودجه",command=self.showbudge)
        self.btnshowbudget.place(x=767,y=450)
        self.day = CTkComboBox(
            self.addFrame,
            width=130,
            height=60,
            bg_color="#fcf003",
            values=getDay()
            ,
        )
        self.day.place(x=830, y=200)

        self.hour = CTkComboBox(
            self.addFrame,
            width=130,
            height=60,
            bg_color="#fcf003",
            values=getTime(),
        )
        self.hour.place(x=760, y=300)

        self.minute = CTkComboBox(
            self.addFrame,
            width=130,
            height=60,
            bg_color="#fcf003",
            values=getMinute(),
        )
        self.minute.place(x=910, y=300)


    # Bind ha
    def on_click_destroytitle(self, event):
        self.txttitle.place_forget()

    def focusouttitle(self, event):
        self.txttitle.place(x=750, y=15, width=35, height=28)

    def oncklickdestroyhazine(self, event):
        self.txthazine.place_forget()

    def focusouthazine(self, event):
        self.txthazine.place(x=750, y=50, width=35, height=28)

    def oncklickdestroymakan(self, event):
        self.txtmakan.place_forget()

    def focusoutmakan(self, event):
        self.txtmakan.place(x=750, y=85, width=32, height=28)

    def oncklickdestroywhatisfor(self, event):
        self.txtwhatisfor.place_forget()

    def focusoutwhatisfor(self, event):
        self.txtwhatisfor.place(x=750, y=120, width=96, height=28)

    def Checknumber(self, e):
        if not self.entryhazine.get().isnumeric():
            self.entryhazine.focus_set()
            messagebox.showerror("اخطار", "عدد فقط")
    def SelectRowIntbl(self,e):
        objrepos = Repository()
        objbl = addplan()
        selecttionRow=self.resultFrame.selection()
        if selecttionRow!=():
            IdRow=self.resultFrame.item(selecttionRow)["values"][3]
            result=objrepos.ReadById(IdRow)
            self.Id.set(IdRow)
            self.title.set(result.title)
            self.Hazine.set(result.hazine)
            self.tarikh.set(result.time)
            self.Makan.set(result.place)
            self.WhatIsFor.set(result.hazinebarayechechizi)
            self.BtnDelet.place(x=865,y=480,width=90)
            self.btnupdate.place(x=960,y=479,width=100)
            self.resultFrame.bind('<Button-3>', self.showinfo)

    def showinfo(self,event):
        selected_item = self.resultFrame.selection()[0]
        item_details = self.resultFrame.item(selected_item, 'values')

        objrepos = Repository()
        result = objrepos.ReadById(item_details[3])

        details_window = Toplevel(self.master)
        details_window.title("اطلاعات")
        details_window.geometry("400x200")

        ttk.Label(details_window, text=f"عنوان: {result.title}").pack(pady=10)
        ttk.Label(details_window, text=f"هزینه: {result.hazine}").pack(pady=10)
        ttk.Label(details_window, text=f"مکان: {result.place}").pack(pady=10)
        ttk.Label(details_window, text=f"هزینه برای چه چیزی: {result.hazinebarayechechizi}").pack(pady=10)
        ttk.Label(details_window, text=f" {result.time}").pack(pady=10)
    def LoadDataInTable(self):
        objbl = addplan()
        listHistory = objbl.GetDataHistory()
        for item in listHistory:
            self.resultFrame.insert('', "end", text=item.id, values=[item.title, item.time, item.hazine,item.id])


    def showbudge(self):
        PageMe2 = main(self.master)



    def plot_chart(self,objec):
        
        plan = addplan()
       
        budge = objec
        y = plan.GetMonthlyHazine()

        # Ensure y has 31 values (one for each day of the month)
        if len(y) < 31:
            y += [0] * (31 - len(y))  # Pad with zeros if less than 31 values
        elif len(y) > 31:
            y = y[:31]  # Trim to 31 values if more than 31 values

        # Make data for x-axis
        x = 0.5 + np.arange(31)

        # Plot
        fig, ax = plt.subplots()
        ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
        ax.set(xlim=(0, 32), xticks=np.arange(1, 32, 2),
               ylim=(0, budge), yticks=np.arange(1, budge, budge / 10))

        plt.show()

    def onclickupdate(self):
        # Get the current Jalali date
        current_jalali_date = jdatetime.now()

        # Parse the user input
        day = int(self.day.get())
        hour = int(self.hour.get())
        minute = int(self.minute.get())
        month = current_jalali_date.month
        year = current_jalali_date.year

        # Create a Jalali date from user input
        jalali_date = jdatetime(year, month, day, hour, minute)

        # Add 10 days
        jalali_date_plus_10 = jalali_date + timedelta(days=10)

        # Convert to Gregorian
        gregorian_date_plus_10 = jalali_date_plus_10.togregorian()

        # Format the Gregorian date
        formatted_date = gregorian_date_plus_10.strftime("%Y-%m-%d %H:%M:%S")

        Id = self.Id.get()
        if Id:
            updated_obj = M_Hazine(
                title=self.entrytitle.get(),
                hazine=self.entryhazine.get(),
                place=self.entrymakan.get(),
                hazinebarayechechizi=self.entrywhatisfor.get(),
                time=formatted_date
            )
            objbl = Repository()
            result = objbl.Update(updated_obj, Id)
            if result:
                messagebox.showinfo("انجام شد", "با موفقیت به روز شد")
                self.Reload()
            else:
                messagebox.showerror("خطا", "به روز رسانی ناموفق بود")
    def OnClickDelet(self):
        Id=self.Id.get()
        objbl = Repository()
        result=objbl.Delete(Id)
        if result:
            self.BtnDelet.place_forget()
            messagebox.showinfo("انجام شد","با موفقیت از لیست نتایج حذف شد")
            self.Reload()
        else:
            messagebox.showerror("انجام نشد","  حذف نشد")

    def onclicksave(self):
        if self.entrytitle.get() == "":
            self.entrytitle.focus_set()
            messagebox.showwarning("خطار", "لطفا جای خالی را پر کنید")
        elif self.entryhazine.get() == "":
            messagebox.showwarning("خطار", "لطفا جای خالی را پر کنید")
            self.entryhazine.focus_set()
        elif self.entrymakan.get() == "":
            self.entrymakan.focus_set()
            messagebox.showwarning("اخطار", "لطفا جای خالی را پر کنید")
        elif self.entrywhatisfor.get() == "":
            self.entrywhatisfor.focus_set()
            messagebox.showwarning("اخطار", "لطفا جای خالی را پر کنید")
        else:
            # Get the current Jalali date
            current_jalali_date = jdatetime.now()

            # Parse the user input
            day = int(self.day.get())
            hour = int(self.hour.get())
            minute = int(self.minute.get())
            month = current_jalali_date.month
            year = current_jalali_date.year

            # Create a Jalali date from user input
            jalali_date = jdatetime(year, month, day, hour, minute)

            # Add 10 days
            jalali_date_plus_10 = jalali_date + timedelta(days=10)

            # Convert to Gregorian
            gregorian_date_plus_10 = jalali_date_plus_10.togregorian()

            # Format the Gregorian date
            formatted_date = gregorian_date_plus_10.strftime("%Y-%m-%d %H:%M:%S")


            obj0 = M_Hazine(self.entrytitle.get(), self.entryhazine.get(), self.entrymakan.get(),
                            self.entrywhatisfor.get(), formatted_date)

            objprs0 = Repository()
            objprs0.insert(obj0)
            self.Reload()

    def Reload(self):
        self.ClearTbl()
        self.LoadDataInTable()

    def ClearTbl(self):
        for item in self.resultFrame.get_children():
            sel = (str(item))
            self.resultFrame.delete(sel)