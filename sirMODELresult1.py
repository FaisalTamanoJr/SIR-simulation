import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the SIR model using differential equations
def SIR_model(y, t, N, r, sigma):
    S, I, R = y
    dSdt = -r * S * I / N  # Equation (3) - Rate of change of Susceptible individuals
    dIdt = r * S * I / N - sigma * I  # Equation (4) - Rate of change of Infected individuals
    dRdt = sigma * I  # Equation (5) - Rate of change of Recovered individuals
    return dSdt, dIdt, dRdt

# Initial conditions
N = 1000  # Total population size
I0, R0 = 1, 0  # Initial number of infected and recovered individuals
S0 = N - I0 - R0  # Initial number of susceptible individuals
r = 0.2  # Disease transmission rate
sigma = 0.1  # Recovery rate

# Set up time steps
t = np.linspace(0, 200, 200)

# Integrate the SIR equations over the time grid, t
y0 = S0, I0, R0  # Initial conditions vector
sol = odeint(SIR_model, y0, t, args=(N, r, sigma))  # Solving the differential equations

# Plot the results
S, I, R = sol.T
plt.plot(t, S, 'b', label='Susceptible')  # Plotting the susceptible population
plt.plot(t, I, 'r', label='Infected')  # Plotting the infected population
plt.plot(t, R, 'g', label='Recovered')  # Plotting the recovered population
plt.legend()
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.title('SIR Model for the Spread of Disease')
plt.show()
