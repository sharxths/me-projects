import numpy as np
import matplotlib.pyplot as plt

print("\n DUAL CYCLE ANALYSIS \n")

# Section 1 : User Inputs

P1 = float(input("Enter the initial pressure  (in bar) : "))
V1 = float(input("Enter the initial volume (m^3) : "))
T1 = float(input("Enter the intial temprature (in K) : "))
r = float(input("Enter the compression ratio (r) : "))
alpha = float(input("Enter pressure ratio (alpha = P3/P2) : "))
Rc = float(input("Enter the cutoff ratio(Rc = V4/V3) : "))

#Sectio 2 : Constants

gamma = 1.4
R = 0.287 #kJ/kgK
Cv = 0.718 #kJ/kgK
Cp = 1.005 #kJ/kgK
#Isentropic compression from 1 to 2
V2 =V1/r
P2 = P1*(V1/V2)**gamma
T2 = T1*(V1/V2)**(gamma-1)
#Constant Volume heat addition process from 2 to 3
V3 = V2
P3 = alpha*P2
T3 = T2*alpha
#Isobaric Heat Addition process from 3 to 4
P4 = P3
V4 = Rc*V3
T4 = T3*Rc
#Isentropic expansion process from 4 to 1
V5 = V1 
P5 = P4*(V4/V5)**gamma
T5 = T4*(V4/V5)**(gamma-1)

# Section 3 : Outputs

Q23 = Cv*(T3 - T2) #Heat added during constant volume process
Q34 = Cp*(T4 - T3) #Heat added during constant pressure process
Qin = Q23 + Q34 #Total Heat added
Qout = Cv*(T5 - T1) #Heat rejected during constant volume process
Wnet = Qin - Qout #Net work done
efficiency = (Wnet/Qin)*100 #Thermal efficiency in percentage

#Sectiom 4 : Displaying the results

print("\n Results : \n")
print("STATE 1")
print("Pressure P1 =", round (P1, 3), "bar")
print("Volume V1 =", round (V1, 3), "m^3")
print("Temperature T1 =", round (T1, 3), "K")

print("\nSTATE 2")
print("Pressure P2 =", round (P2, 3), "bar")
print("Volume V2 =", round (V2, 3), "m^3")
print("Temperature T2 =", round (T2, 3), "K")       

print("\nSTATE 3")
print("Pressure P3 =", round (P3, 3), "bar")
print("Volume V3 =", round (V3, 3), "m^3")
print("Temperature T3 =", round (T3, 3), "K")   

print("\nSTATE 4")
print("Pressure P4 =", round (P4, 3), "bar")
print("Volume V4 =", round (V4, 3), "m^3")
print("Temperature T4 =", round (T4, 3), "K")   

print("\nSTATE 5")
print("Pressure P5 =", round (P5, 3), "bar")
print("Volume V5 =", round (V5, 3), "m^3")
print("Temperature T5 =", round (T5, 3), "K")

print("\n Heat and Work Analysis : \n")

print("Heat added at Constant Volume process(Q23) =", round (Q23, 3), "kJ/kg")
print("Heat added at Constant Pressure process(Q34) =", round (Q34, 3), "kJ/kg")
print("Total Heat added(Qin) =", round (Qin, 3), "kJ/kg")
print("Heat rejected at Constant Volume process(Qout) =", round (Qout, 3), "kJ/kg")
print("Net Work done(Wnet) =", round (Wnet, 3), "kJ/kg")
print("Thermal efficiency =", round (efficiency, 3), "%")


#Generating P-V Diagram

#Process 1-2 : Isentropic compression

V_comp = np.linspace(V1, V2, 200)
P_comp = P1*(V1**gamma)/(V_comp**gamma)

#Process 2-3 : Constant Volume heat addition

P_cv = np.linspace(P2,P3, 100)
V_cv = np.full_like(P_cv, V2)

#Process 3-4 : Isobaric heat addition

V_cp = np.linspace(V3, V4, 100)
P_cp = np.full_like(V_cp, P3)

#Process 4-5 : Isentropic expansion

V_exp = np.linspace(V4, V5, 200)
P_exp = P4*(V4**gamma)/(V_exp**gamma)

#Process 5-1 : Isobaric heat rejection

P_rej = np.linspace(P5, P1, 100)
V_rej = np.full_like(P_rej, V5)

#Section 5 : Plotting the P-V diagram

plt.figure(figsize = (12, 8))

plt.plot(V_comp, P_comp,
         linewidth=3, label = '1-2 Isentropic Compression')
plt.plot(V_cv, P_cv,
         linewidth=3, label = '2-3 Constant Volume Heat Addition')
plt.plot(V_cp, P_cp,
         linewidth=3, label = '3-4 Isobaric Heat Addition')
plt.plot(V_exp, P_exp,
         linewidth=3, label = '4-5 Isentropic Expansion')
plt.plot(V_rej, P_rej,
         linewidth=3, label = '5-1 Constant volume Heat Rejection')

plt.scatter([V1, V2, V3, V4, V5],
            [P1, P2, P3, P4, P5],
            s =100,
            color = 'red',
            )
plt.text(V1, P1, ' 1', fontsize=12)
plt.text(V2, P2, ' 2', fontsize=12)
plt.text(V3, P3, ' 3', fontsize=12)
plt.text(V4, P4, ' 4', fontsize=12)
plt.text(V5, P5, ' 5', fontsize=12)

plt.title('P-V Diagram of Dual Cycle', fontsize=18)
plt.xlabel('Volume (m^3)', fontsize=14)
plt.ylabel('Pressure (bar)', fontsize=14)
plt.grid(True)
plt.legend()
plt.tight_layout()
output_file = 'dualcycle_pv.png'
plt.savefig(output_file)
print(f"Graph saved to {output_file}")
plt.show()
