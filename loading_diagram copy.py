from wingcg import compute_cg
import copy
import matplotlib.pyplot as plt

class Plane:
    def __init__(self):
        self.mass_list = []
        self.pos_list = []
    
    def add_mass(self, mass, pos):
        self.mass_list.append(mass)
        self.pos_list.append(pos)
    
    def get_cg(self):
        return sum(self.mass_list[i] * self.pos_list[i] for i in range(len(self.mass_list)))/sum(self.mass_list)
    
    def get_mass(self):
        return sum(self.mass_list)
    
def add_points(plane, objects, masses, xcgs, reversed=False):
    _objects = objects[:]
    if reversed:
        _objects.reverse()
    cg = plane.get_cg()
    mass = plane.get_mass()
    xcgs.append(cg)
    masses.append(mass)
    for object in _objects:
        new_mass = object[0]
        new_pos = object[1]
        plane.add_mass(new_mass, new_pos)
        cg = plane.get_cg()
        mass = plane.get_mass()
        xcgs.append(cg)
        masses.append(mass)
        
        

MAC = 2.463771418
LEMAC = 11.69586907
OEW = 14219.1
#empty_plane_cg = 0.357498253 + LEMAC
#empty_plane_cg = 0.2290540063 + LEMAC
#empty_plane_cg = 0.4859424998 + LEMAC
#empty_plane_cg = 0.1797668398*MAC + LEMAC
empty_plane_cg = 0.4854016701*MAC + LEMAC #aftmost cg

passenger_weight = 84
rows = 14
start_passenger_comp = 5.94
length_passenger_comp = 12.29*(rows/18)
seat_dist = length_passenger_comp / (rows)
print(seat_dist)
seat = seat_dist / 2 + start_passenger_comp
passengers = []

for pos in range(rows):
    passengers.append((2*passenger_weight, seat))
    seat += seat_dist
    
cargo_total = 7400 - rows*4*passenger_weight
front_cargo = 0.5714285714*cargo_total #proportional to front max cargo
aft_cargo = 0.4285714286*cargo_total #proportional to aft max cargo
cargo = [(front_cargo, 6.697), (aft_cargo, 23.92)] #(mass, pos)
# front_cargo = 500
# aft_cargo = 0
# cargo = [(front_cargo, 6.697), (aft_cargo, 23.92)] #(mass, pos)

b = 27.05
cR = 2.834799723
cT = 1.675366636
LE_cR = 11.3248
fuel_loc = LE_cR + compute_cg(b, cR, cT)
fuel_weight = 1500
#MAC = 2.305065311

fuel = [(2*fuel_weight, fuel_loc)]
front_loaded_cargo_positions = []
front_loaded_cargo_masses = []
rear_loaded_cargo_positions = []
rear_loaded_cargo_masses = []
front_loaded_cargo_plane = Plane()
front_loaded_cargo_plane.add_mass(OEW, empty_plane_cg)
rear_loaded_cargo_plane = copy.deepcopy(front_loaded_cargo_plane)
add_points(front_loaded_cargo_plane, cargo, front_loaded_cargo_masses, front_loaded_cargo_positions)
add_points(rear_loaded_cargo_plane, cargo, rear_loaded_cargo_masses, rear_loaded_cargo_positions, reversed=True)

first_front_loaded_passengers_plane = copy.deepcopy(front_loaded_cargo_plane)
first_rear_loaded_passengers_plane = copy.deepcopy(front_loaded_cargo_plane)
first_rear_loaded_passengers_masses = []
first_front_loaded_passengers_masses = []
first_rear_loaded_passengers_positions = []
first_front_loaded_passengers_positions = []
add_points(first_front_loaded_passengers_plane, passengers, first_front_loaded_passengers_masses, first_front_loaded_passengers_positions)
add_points(first_rear_loaded_passengers_plane, passengers, first_rear_loaded_passengers_masses, first_rear_loaded_passengers_positions, reversed=True)

second_front_loaded_passengers_plane = copy.deepcopy(first_front_loaded_passengers_plane)
second_rear_loaded_passengers_plane = copy.deepcopy(first_front_loaded_passengers_plane)
second_rear_loaded_passengers_masses = []
second_front_loaded_passengers_masses = []
second_rear_loaded_passengers_positions = []
second_front_loaded_passengers_positions = []
add_points(second_front_loaded_passengers_plane, passengers, second_front_loaded_passengers_masses, second_front_loaded_passengers_positions)
add_points(second_rear_loaded_passengers_plane, passengers, second_rear_loaded_passengers_masses, second_rear_loaded_passengers_positions, reversed=True)

fuel_masses = []
fuel_positions = []
fueled_plane = copy.deepcopy(second_front_loaded_passengers_plane)
add_points(fueled_plane, fuel, fuel_masses, fuel_positions)

def transform_positions(positions, MAC):
    return [(pos - LEMAC) / MAC for pos in positions]

# Transform all position lists before plotting
front_loaded_cargo_positions = transform_positions(front_loaded_cargo_positions, MAC)
rear_loaded_cargo_positions = transform_positions(rear_loaded_cargo_positions, MAC)

first_front_loaded_passengers_positions = transform_positions(first_front_loaded_passengers_positions, MAC)
first_rear_loaded_passengers_positions = transform_positions(first_rear_loaded_passengers_positions, MAC)

second_front_loaded_passengers_positions = transform_positions(second_front_loaded_passengers_positions, MAC)
second_rear_loaded_passengers_positions = transform_positions(second_rear_loaded_passengers_positions, MAC)

fuel_positions = transform_positions(fuel_positions, MAC)


cgs = front_loaded_cargo_positions + rear_loaded_cargo_positions + first_front_loaded_passengers_positions + first_rear_loaded_passengers_positions + second_front_loaded_passengers_positions + second_rear_loaded_passengers_positions + fuel_positions
maxcg = max(cgs)
mincg = min(cgs)
print(mincg, maxcg)
# Plotting
import matplotlib.pyplot as plt

plt.plot(front_loaded_cargo_positions, front_loaded_cargo_masses, 
          marker='o', label="Front loaded Cargo")
plt.plot(rear_loaded_cargo_positions, rear_loaded_cargo_masses, 
          marker='o', label="Rear loaded Cargo")

plt.plot(first_front_loaded_passengers_positions, first_front_loaded_passengers_masses, 
          marker='o', label="First Front loaded Passengers")
plt.plot(first_rear_loaded_passengers_positions, first_rear_loaded_passengers_masses, 
          marker='o', label="First Rear loaded Passengers")

plt.plot(second_front_loaded_passengers_positions, second_front_loaded_passengers_masses, 
          marker='o', label="Second Front loaded Passengers")
plt.plot(second_rear_loaded_passengers_positions, second_rear_loaded_passengers_masses, 
          marker='o', label="Second Rear loaded Passengers")

plt.plot(fuel_positions, fuel_masses, marker='o', label="Fuel")

plt.axvline(x=maxcg, color='r', linestyle='--', linewidth=2, label="Max CG Limit")
plt.axvline(x=mincg, color='b', linestyle='--', linewidth=2, label="Min CG Limit")

plt.ylabel("Mass [kg]")
plt.xlabel("xcg [MAC]")
plt.grid(True)
plt.legend()  # Ensures labels appear in the legend
plt.tight_layout()
plt.show()
