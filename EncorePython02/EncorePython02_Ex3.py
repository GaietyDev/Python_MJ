mass = int(input("Enter the mass(kg): "))
velocity = int(input("Enter the velocity(m/s): "))
print()

momentum = mass * velocity
kinetic_energy = (1/2 * mass) * (velocity * velocity)
print("Momentum (kg m/s):",momentum)
print("Kinetic energy (kg m^2/s^2):",kinetic_energy)
