import matplotlib.pyplot as plt
import numpy as np
from bll.addplan import addplan

# Initialize addplan instance
plan = addplan()

# Get the total budget
budge = plan.GetTotalHazine()

# Get the monthly hazine data
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
