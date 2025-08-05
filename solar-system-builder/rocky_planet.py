import math

# constant earth values
e_mass = 5.972
e_radius = 6371
e_gravity = 9.807
e_density = 5.15
G = 6.6743E-11

mass    = float(input("enter the mass:             ") )
radius  = float(input("enter the radius:           ") )
gravity = mass/(radius**2)
density = (gravity/radius)
escape_velocity = math.sqrt(mass/radius)

a_mass    = (mass*e_mass)*(10**24)
a_radius  = (radius*e_radius*1000)
a_gravity = (gravity*e_gravity)
a_density = (density*e_density)
a_escape_velocity = (math.sqrt( (2*G)*(a_mass/a_radius) )/1000)

circumference     = ( (2*math.pi)*a_radius)
surface_area      = ( (4*math.pi)*(a_radius**2))
volume            = ( ( (4/3)*math.pi) * (a_radius**3))

print(f"gravity:                    {gravity}")
print(f"density:                    {density}")
print(f"relative escape_velocity:   {escape_velocity}")
print(f"absolute_mass:              {a_mass}kg")
print(f"absolute_radius:            {a_radius}m")
print(f"absolute_gravity:           {a_gravity}m/s^2")
print(f"absolute_density:           {a_density}g/cm^3")
print(f"escape_velocity:            {a_escape_velocity}km/s")
print(f"circumference:              {circumference}m")
print(f"surface_area:               {surface_area}m^2")
print(f"volume:                     {volume}m^3")