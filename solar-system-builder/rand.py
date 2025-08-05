import random

# rocky
r_mass = round(random.uniform(1, 3.5),1)
r_radius = round(random.uniform(0.5, 1.5),1)

# dwarf_planet
d_mass = round(random.uniform(0.0001, 0.1),1)
d_radius = round(random.uniform(0.04,1.5),1)

# gas giants
g_mass = round(random.uniform(0.3, 13),1)
g_radius = round(random.uniform(0.7, 2),1)

# puff ball
p_mass = round(random.uniform(0.1,2),1)
p_radius = round(random.uniform(1.5,3),1)

# gass dwarf
gd_mass = round(random.uniform(0.1, 1),1)
gd_radius = round(random.uniform(0.3,0.7),1)

print(r_mass, r_radius, d_mass, d_radius, g_mass, g_radius, p_mass, p_radius, gd_mass, gd_radius)