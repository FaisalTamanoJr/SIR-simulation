import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the SIR model
def sir_model(y, t, N, r, sigma):
    S, I, R = y
    dSdt = -r * S * I / N # Equation (3)
    dIdt = r * S * I / N - sigma * I # Equation (4)
    dRdt = sigma * I # Equation (5)
    return dSdt, dIdt, dRdt

# Define initial conditions
N = 1000
S0, I0, R0 = N-1, 1, 0 # Equation (2)
y0 = S0, I0, R0

# Define model parameters
r = 0.5 # Transmission rate (a*c)
sigma = 0.1 # Recovery rate

# Define time points
t = np.linspace(0, 100, 1000)

# Solve the SIR model using ODE solver
sol = odeint(sir_model, y0, t, args=(N, r, sigma))

# Plot results
plt.plot(t, sol[:, 0], label='S(t)') # Susceptible population
plt.plot(t, sol[:, 1], label='I(t)') # Infected population
plt.plot(t, sol[:, 2], label='R(t)') # Recovered population
plt.legend()
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.title('SIR Model for Spread of Disease')
plt.show()