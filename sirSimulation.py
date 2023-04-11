import math

def compute_for_values(s0, i0, a, c, sigma, t):
    output = {
              "susceptible": 0,
              "infected": 0,
              "recovered": 0,
              "max infected": 0
    }

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


    # Calculate population at time t
    """
    I'll still need to modify some of the equations here
    - Faisal
    """
    n = s0 + i0
    r = a * c
    p = sigma / r

    # these constants are just temp, will edit them next time
    s_o = 1
    i_o = 2
    r_o = 3
    imax = 4
    #s_o = s0 * math.exp(-r * i0 * t)
    #i_o = (n / (1 + p * s0)) * math.exp((r * s0 - sigma) * t) - p * s_o
    #r_o = n - s_o - i_o

    # Calculate maximum number of infected individuals
    #imax = n - p - math.log(s0)

    # add the results to the dictionary
    output["susceptible"] = s_o
    output["infected"] = i_o
    output["recovered"] = r_o
    output["max infected"] = imax

    return output
