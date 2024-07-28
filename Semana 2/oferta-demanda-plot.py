import numpy as np
import matplotlib.pyplot as plt

# Define the supply and demand equations
def supply(P):
    return 2 * P - 10

def demand(P):
    return 50 - 3 * P

# Find the equilibrium point
# At equilibrium, supply equals demand: Q_s = Q_d
# So, 2P - 10 = 50 - 3P
# Solving for P gives: 5P = 60 -> P = 12
# Substitute P back into either equation to find Q
P_eq = 60 / 5
Q_eq = supply(P_eq)

# Generate a range of prices
P = np.linspace(0, 25, 100)
Q_s = supply(P)
Q_d = demand(P)

# Plot the supply and demand curves
plt.figure(figsize=(10, 6))
plt.plot(P, Q_s, label='Supply', color='b')
plt.plot(P, Q_d, label='Demand', color='r')
plt.axvline(x=P_eq, linestyle='--', color='gray')
plt.axhline(y=Q_eq, linestyle='--', color='gray')
plt.scatter(P_eq, Q_eq, color='black', zorder=5)
plt.text(P_eq, Q_eq, f'  Equilibrium\n  P = {P_eq:.2f}\n  Q = {Q_eq:.2f}', horizontalalignment='left')

# Labels and title
plt.xlabel('Price (P)')
plt.ylabel('Quantity (Q)')
plt.title('Supply and Demand Curves')
plt.legend()
plt.grid(True)
plt.show()
