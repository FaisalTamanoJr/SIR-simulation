import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate


def compute_for_values(s0, i0, a, c, sigma, t):
    # Warn the user if they do not provide a number than their inputs
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
    if s0 <= 0:
        return "Error: The number of susceptible individuals must be greater than 0"

    if i0 <= 0:
        return "Error: The number of infected individuals must be greater than 0"

    # Define the differential equations for the SIR model
    def SIR_model(y, time, small_a, small_c, sigma_var):
        big_s, big_i, big_r = y
        dSdt = -small_a * small_c * big_s * big_i
        dIdt = small_a * small_c * big_s * big_i - sigma_var * big_i
        dRdt = sigma_var * big_i
        print(time)
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
    n = (s0 + i0)
    p = (sigma / (a * c))
    imax = n - p - (p * np.log(p / s0))

    # Return the maximum number of infected individuals
    return {"susceptible": S, "infected": I, "recovered": R, "max infected": imax}


def graph_values(t, big_s, big_i, big_r):
    # Plot the results
    t_span = np.linspace(0, float(t), 100)
    plt.plot(t_span, big_s, label='Susceptible')
    plt.plot(t_span, big_i, label='Infected')
    plt.plot(t_span, big_r, label='Recovered')
    plt.xlabel('Time (days)')
    plt.ylabel('Number of individuals')
    plt.title('SIR Model')
    plt.legend()
    plt.show()
