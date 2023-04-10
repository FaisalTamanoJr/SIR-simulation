import math

def main():
    # Get user input for initial values
    S0 = int(input("Enter the initial number of susceptible individuals: "))
    I0 = int(input("Enter the initial number of infected individuals: "))

    
    # STILL WORKING ON THIS PART
    a = float(input("Enter the value of a: "))
    c = float(input("Enter the value of c: "))
    sigma = float(input("Enter the value of σ: "))

    # Get user input for time t
    t = int(input("Enter the time in days: "))

    # Calculate population at time t
    N = S0 + I0
    r = a * c
    p = sigma / r

    S = S0 * math.exp(-r * I0 * t)
    I = (N / (1 + p * S0)) * math.exp((r * S0 - sigma) * t) - p * S
    R = N - S - I

    # Calculate maximum number of infected individuals
    Imax = N - p - math.log(S0)

    # Print results
    print("Population at time t:")
    print("Susceptible individuals: ", S)
    print("Infected individuals: ", I)
    print("Recovered individuals: ", R)
    print("Maximum number of infected individuals: ", Imax)