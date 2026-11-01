'''Design a socket and spigot type of a quarter joint to connect two round rods subjected to a force of 120kN. 
The material of joint is made of C40 steel having yield stress 325MPa, 
Takes FoS 4 for tension, 6 for shear, and 3 for crushing load'''

import json
import math

#Given values
print("==================== SPIGOT COTTER DESIGN ====================")
force = 120000 #in kN.
yeild_stress = 325 #in MPa.
FOSt = 4 #Factor of saftey for tensile/axial load
FOSs = 6 #Factor of saftey for shear load
FOSc = 3 #Factor of saftey for crushing load

tensile_load = (yeild_stress/FOSt)
shear_load = (yeild_stress/FOSs)
crushing_load = (yeild_stress/FOSc)

def shaft_diameter(): #Finding Shaft Diameter
    d = math.sqrt((4*force)/(math.pi*tensile_load))
    diameter = math.ceil(d)
    return diameter

def spigot_diameter():#Finds the thickness and spigot diameter
    sdiameter_thickness = force/crushing_load
    sdiameter = math.sqrt(((4 * force / tensile_load) + 4 * sdiameter_thickness) / math.pi)
    d1 = math.ceil(sdiameter)
    thickness = sdiameter_thickness/d1
    t = math.ceil(thickness)
    return d1, t

def spigot_collor_diameter(d1):
    sdiameter = math.sqrt(((4*force)/(math.pi*crushing_load))+(d1**2))
    d2 = math.ceil(sdiameter)
    return d2

def spigot_collor_thickness(d1):
    collor_thickness = (force/(math.pi*d1*shear_load))
    e = math.ceil(collor_thickness)
    return e

def socket_diameter(d1,t):
    a = math.pi
    b = -4*t
    c = (((-4*force)/tensile_load)+(math.pi*(d1**2))+(-4*t*d1))
    D = b**2 - 4*a*c
    if D < 0:
        return None
    d3 = (-b + math.sqrt(D)) / (2*a)
    return math.ceil(d3) if d3 > 0 else None

def socket_collor_diameter(d1, t):
    socdiameter = (((force)/(crushing_load*t))+d1)
    d4 = math.ceil(socdiameter)
    return d4

def clearance(d1):
    clear = (force/(2*shear_load*d1))
    a = math.ceil(clear)
    return a

def socket_collor_thickness(d1, d4):
    socthickness = (force/(2*shear_load*(d4-d1)))
    c = math.ceil(socthickness)
    return c

def values(d,d1,d2,t,d3,d4,a,c,e,force,tensile_load,shear_load,crushing_load):
    print("\n"+"="*20 +"RESULTS" + "="*20)
    print(f"Applied Force: {force}kN.")
    print(f'Tensile Load: {tensile_load}MPa.')
    print(f'Shear Load: {shear_load}MPa.')
    print(f'Crushing Load: {crushing_load}MPa.')

    print("-"*60)

    print(f"Shaft diameter: {d}mm.")
    print(f"Spigot diameter: {d1}")
    print(f"Spigot thickness: {t}mm.")
    print(f"Spigot collor diameter: {d2}mm.")
    print(f"Spigot collor thickness: {e}mm.")
    print(f"Socket diameter: {d3}mm.")
    print(f"Socket collor diameter: {d4}mm.")
    print(f"Socket collor thickness: {c}mm.")
    print(f"Clearance: {a}mm.")


d = shaft_diameter()
d1, t = spigot_diameter()
d2 = spigot_collor_diameter(d1)
e = spigot_collor_thickness(d1)
d3 = socket_diameter(d1, t)
d4 = socket_collor_diameter(d1, t)
a = clearance(d1)
c = socket_collor_thickness(d1, d4)

values(
    d, d1, d2, t, d3, d4, a, c, e, force,
    tensile_load, shear_load, crushing_load
)

