from tkinter import *
import sympy as sp

import sirSimulation
import sirSimulation as sirSim

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

window = Tk()
window.title = 'SIR Model Simulator'

inputsFrame = Frame(padx=20, pady=30)
eqFrame = Frame(padx=20, pady=30)

lbl_inputs = Label(inputsFrame, text="INPUTS")
lbl_S0 = Label(inputsFrame, text="Initial number of susceptible individuals: ")
lbl_I0 = Label(inputsFrame, text="Initial number of infected individuals: ")
lbl_constantA = Label(inputsFrame, text=" Rate of infected people infecting susceptible individuals: ")
lbl_constantC = Label(inputsFrame, text="Rate of people coming into contact with an infected person: ")
lbl_constantSigma = Label(inputsFrame, text="Rate of people recovering: ")
lbl_varTime = Label(inputsFrame, text="Time (in days): ")

lbl_inputs.grid(row=0, column=0, sticky="W")
lbl_S0.grid(row=1, column=0, sticky="E")
lbl_I0.grid(row=2, column=0, sticky="E")
lbl_constantA.grid(row=3, column=0, sticky="E")
lbl_constantC.grid(row=4, column=0, sticky="E")
lbl_constantSigma.grid(row=5, column=0, sticky="E")
lbl_varTime.grid(row=6, column=0, sticky="E", pady=10)

ent_S0 = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_I0 = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_constantA = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_constantC = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_constantSigma = Entry(inputsFrame, width=10, bg="white", fg="black")
ent_varTime = Entry(inputsFrame, width=10, bg="white", fg="black")

ent_S0.grid(row=1, column=1, sticky="W")
ent_I0.grid(row=2, column=1, sticky="W")
ent_constantA.grid(row=3, column=1, sticky="W")
ent_constantC.grid(row=4, column=1, sticky="W")
ent_constantSigma.grid(row=5, column=1, sticky="W")
ent_varTime.grid(row=6, column=1, sticky="E", pady=10)

s0 = 0
i0 = 0
constantA = 0
constantC = 0
constantSigma = 0
varTime = 0

already_simulated = False


def simulate_on_click():
    global already_simulated
    if already_simulated:
        for widget in eqFrame.winfo_children():
            widget.destroy()

    s0 = ent_S0.get()
    i0 = ent_I0.get()
    constantA = ent_constantA.get()
    constantC = ent_constantC.get()
    constantSigma = ent_constantSigma.get()
    varTime = ent_varTime.get()

    s = sp.Symbol('S')
    i = sp.Symbol('I')
    r = sp.Symbol('R')
    a = sp.Symbol('a')
    c = sp.Symbol('c')
    sigma = sp.Symbol('σ')

    simulated = sirSimulation.compute_for_values(s0=s0, i0=i0, a=constantA, c=constantC, sigma=constantSigma, t=varTime)
    if type(simulated) == dict:
        rateOfSus = simulated["susceptible"]
        rateOfInf = simulated["infected"]
        rateOfRec = simulated["recovered"]
        maxInf = simulated["max infected"]

        lbl_susRate = Label(eqFrame, text="S(0)=" + str(rateOfSus))
        lbl_infRate = Label(eqFrame, text="I(0)=" + str(rateOfInf))
        lbl_recRate = Label(eqFrame, text="R(0)=" + str(rateOfRec))
        lbl_infMax = Label(eqFrame, text="Imax=" + str(maxInf))

        lbl_susRate.pack()
        lbl_infRate.pack()
        lbl_recRate.pack()
        lbl_infMax.pack()

    else:
        lbl_error = Label(text=simulated)
        lbl_error.pack()

    already_simulated = True


btn_compute = Button(inputsFrame, text="Simulate SIR Model", command=simulate_on_click)
btn_compute.grid(row=7, column=0, columnspan=2)

inputsFrame.pack(side=LEFT)
eqFrame.pack(side=TOP)

window.mainloop()
