import math

# constant sun values
s_mass = 1.988
s_luminosity = 3.823

mass    = float(input("enter the mass:         ") )
luminosity = mass**4
diameter = mass**0.74
surface_temperature = mass**0.505
life_time = mass**-2.5
habitable_zone = math.sqrt(luminosity)
inner_radius = habitable_zone* 0.95
outter_radius = habitable_zone * 1.37

a_mass = (mass*s_mass)*(10**30)
a_luminosity = (luminosity*s_luminosity)*(10**26)

inner_limit = 0.1 * mass
outter_limit = 40 * mass
frost_line = 4.85*(math.sqrt(luminosity))

print(f"luminosity:             {luminosity}W")
print(f"diameter:               {diameter}")
print(f"surface temperature:    {surface_temperature}")
print(f"lifetime:               {life_time}")
print(f"habitable zone:         {habitable_zone}AU")
print(f"inner radius:           {inner_radius}AU")
print(f"outter radius:          {outter_radius}AU")
print(f"absolute mass:          {a_mass}")
print(f"absolute luminosity:    {a_luminosity}W")
print(f"inner limit:            {inner_limit}AU")
print(f"outter limit:           {outter_limit}AU")
print(f"frost line:             {frost_line}AU")