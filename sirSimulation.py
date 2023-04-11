import math

def compute_for_values(s0, i0, a, c, sigma, t):

    # Warn the user if they do not provide a number as their inputs
    try:
        s0 = int(s0)
        i0 = int(i0)
        a = float(s0)
        c = float(c0)
        sigma = float(sigma)
        t = float(t)
    except ValueError:
        return "Error: input must all be numbers"

    # Make sure that S(0) and I(0) is greater than 0
    if (s0 <= 0):
        return "Error: The number of susceptible individuals must be greater than 0"

    if (i0 <= 0):
        return "Error: The number of infected individuals must be greater than 0"

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


if __name__ == "__main__":
    main()
