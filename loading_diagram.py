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
        
        

MAC = 2.305065311
LEMAC = 10.51244112
OEW = 13294
empty_plane_cg = 0.357498253 + LEMAC
cargo = [(400, 4.45), (280, 22.5)] #(mass, pos)
passenger_weight = 84
rows = 18
start_passenger_comp = 5.94
length_passenger_comp = 12.29
seat_dist = length_passenger_comp / (rows)
seat = seat_dist / 2 + start_passenger_comp
first_passengers = []

for pos in range(18):
    first_passengers.append((2*passenger_weight, seat))
    seat += seat_dist


b = 27.05
cR = 2.480525534
cT = 1.389874894
LE_cR = 8.865205242
fuel_loc = LE_cR + compute_cg(b, cR, cT)
fuel_weight = 1500
MAC = 2.305065311

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
add_points(first_front_loaded_passengers_plane, first_passengers, first_front_loaded_passengers_masses, first_front_loaded_passengers_positions)
add_points(first_rear_loaded_passengers_plane, first_passengers, first_rear_loaded_passengers_masses, first_rear_loaded_passengers_positions, reversed=True)

second_front_loaded_passengers_plane = copy.deepcopy(first_front_loaded_passengers_plane)
second_rear_loaded_passengers_plane = copy.deepcopy(first_front_loaded_passengers_plane)
second_rear_loaded_passengers_masses = []
second_front_loaded_passengers_masses = []
second_rear_loaded_passengers_positions = []
second_front_loaded_passengers_positions = []
add_points(second_front_loaded_passengers_plane, first_passengers, second_front_loaded_passengers_masses, second_front_loaded_passengers_positions)
add_points(second_rear_loaded_passengers_plane, first_passengers, second_rear_loaded_passengers_masses, second_rear_loaded_passengers_positions, reversed=True)

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

# Plotting
plt.plot(front_loaded_cargo_positions, front_loaded_cargo_masses, 
          marker='o')
plt.plot(rear_loaded_cargo_positions, rear_loaded_cargo_masses, 
          marker='o')

plt.plot(first_front_loaded_passengers_positions, first_front_loaded_passengers_masses, 
          marker='^')
plt.plot(first_rear_loaded_passengers_positions, first_rear_loaded_passengers_masses, 
          marker='^')

plt.plot(second_front_loaded_passengers_positions, second_front_loaded_passengers_masses, 
          marker='^')
plt.plot(second_rear_loaded_passengers_positions, second_rear_loaded_passengers_masses, 
          marker='^')

plt.plot(fuel_positions, fuel_masses, marker='^')

# Update axis label to reflect transformation

plt.ylabel("Mass [kg]")
plt.title("xcg [MAC]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
