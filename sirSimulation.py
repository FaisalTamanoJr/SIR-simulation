import math

def compute_for_values(s0, i0, a, c, sigma, t):

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
