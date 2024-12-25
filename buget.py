import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from dal.Repository import Repository
from be.server import M_Hazine
from pl.mainscrean import App,plot_chart
class addplan:
    def GetDataHistory(self):
        repso = Repository()
        return repso.Read(M_Hazine)

    def GetTotalHazine(self):
        repso = Repository()
        hazine_list = repso.Read(M_Hazine)
        total_hazine = sum(hazine.hazine for hazine in hazine_list)
        return total_hazine


class MoneyTankAnimation:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=200, height=300)
        self.canvas.pack()
        
        self.tank_width = 100
        self.tank_height = 200
        self.tank_color = "gray"
        self.money_color = "green"
        self.money_height = self.tank_height

        # Draw tank
        self.tank = self.canvas.create_rectangle(50, 50, 50 + self.tank_width, 50 + self.tank_height, outline="black",
                                                 fill=self.tank_color)
        # Draw money
        self.money = self.canvas.create_rectangle(50, 50 + self.tank_height - self.money_height, 50 + self.tank_width,
                                                  50 + self.tank_height, outline="black", fill=self.money_color)
        # Text for amount
        self.amount_text = self.canvas.create_text(100, 40, text="0 %", font=("Arial", 12))

    def update_tank(self, amount):
        # Ensure amount is within valid range (0 to 100)
        amount = max(0, min(100, amount))
        # Calculate new money height
        new_money_height = (self.tank_height * amount) / 100
        # Update money level
        self.canvas.coords(self.money, 50, 50 + self.tank_height - new_money_height, 50 + self.tank_width,
                           50 + self.tank_height)
        # Update text
        self.canvas.itemconfig(self.amount_text, text=f"  %{amount}")
        self.canvas.update()


def main(e):
    
    root = tk.Tk()
    root.title("Money Tank Animation")

    animation = MoneyTankAnimation(root)
    plan = addplan()

    def start_animation():
        try:
            total_budget = float(budget_entry.get())
            total_hazine = plan.GetTotalHazine()
            if total_budget < total_hazine:
                tk.messagebox.showerror("Error", "هزینه بیشتر از بودجه است")
                return
            remaining_budget = total_budget - total_hazine
            percentage = (remaining_budget / total_budget) * 100
            animation.update_tank(percentage)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numbers")

    # Budget input field
    tk.Label(root, text="Enter Budget:").pack()
    budget_entry = ttk.Entry(root)
    budget_entry.pack()

    # Label to show entered budget
    budget_label = tk.Label(root, text=" تومان")
    budget_label.pack()

    def update_budget_label(*args):
        budget = budget_entry.get()
        budget_label.config(text=f"{budget} تومان")

    budget_entry.bind("<KeyRelease>", update_budget_label)

    # Start button
    start_button = ttk.Button(root, text="Start Animation", command=start_animation)
    start_button.pack()

    def bugetentryget():
        budgetfornemodaz = budget_entry.get()
        return budgetfornemodaz
    
    root.mainloop()
    
    return App.plot_chart(bugetentryget)

if __name__ == "__main__":
    main()

