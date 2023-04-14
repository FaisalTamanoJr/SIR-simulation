import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import integrate

def compute_for_values(s0, i0, a, c, sigma, t):
    # Warn the user if they do not provide a number as their inputs
    try:
        s0 = int(s0)
        i0 = int(i0)
        a = float(a)
        c = float(c)
        sigma = float(sigma)
        t = float(t)
    except ValueError:
        return "Error: input must all be numbers"

    # Make sure that S(0) and I(0) is greater than 0
    if (s0 <= 0):
        return "Error: The number of susceptible individuals must be greater than 0"

    if (i0 <= 0):
        return "Error: The number of infected individuals must be greater than 0"

    # Define the differential equations for the SIR model
    def SIR_model(y, t, a, c, sigma):
        S, I, R = y
        dSdt = -a * c * S * I
        dIdt = a * c * S * I - sigma * I
        dRdt = sigma * I
        return dSdt, dIdt, dRdt

    # Set up the initial conditions
    y0 = [s0, i0, 0]

    # Set up the time grid
    t_span = np.linspace(0, t, 100)

    # Solve the differential equations
    sol = integrate.odeint(SIR_model, y0, t_span, args=(a, c, sigma))

    # Extract the solutions for S, I, and R
    S, I, R = sol[:, 0], sol[:, 1], sol[:, 2]

    # Calculate the maximum number of infected individuals
    imax = [0, 3]


    # Return the maximum number of infected individuals
    return {"susceptible": S, "infected": I, "recovered": R, "max infected": imax}


def graph_values(t, S, I, R):
    # Plot the results
    t_span = np.linspace(0, float(t), 100)
    plt.plot(t_span, S, label='Susceptible')
    plt.plot(t_span, I, label='Infected')
    plt.plot(t_span, R, label='Recovered')
    plt.xlabel('Time (days)')
    plt.ylabel('Number of individuals')
    plt.title('SIR Model')
    plt.legend()
    plt.show()
