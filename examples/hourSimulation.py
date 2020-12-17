import sys
import os

from rc_buildingsimulator.building_physics import Zone  # Importing Zone Class

# Example Inputs
t_air = 10
t_m_prev = 22
internal_gains = 10  # Internal heat gains, in Watts
# Solar heat gains after transmitting through the winow [Watts]
solar_gains = 2000
ill = 44000  # Illuminance after transmitting through the window [Lumens]
occupancy = 0.1  # Occupancy for the timestep [people/hour/square_meter]


# Initialise an instance of the Zone. Empty brackets take on the
# default parameters. See ZonePhysics.py to see the default values
Office = Zone()

# Solve for Zone energy
Office.solve_energy(internal_gains, solar_gains, t_air, t_m_prev)

# Solve for Zone lighting
Office.solve_lighting(ill, occupancy)

print(Office.t_m)  # Printing Room Temperature of the medium

print(Office.lighting_demand)  # Print Lighting Demand
print(Office.energy_demand)  # Print heating/cooling loads

# Example of how to change the set point temperature after running a simulation
Office.theta_int_h_set = 20.0

# Solve again for the new set point temperature
Office.solve_energy(internal_gains, solar_gains, t_air, t_m_prev)

print(Office.floor_area)
print(Office.room_vol)
print(Office.total_internal_area)

print(Office.t_m)  # Print the new internal temperature

# Print a boolean of whether there is a heating demand
print(Office.has_heating_demand)
