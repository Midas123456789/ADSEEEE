from wingcg import compute_cg

class plane:
    def __init__(self):
        self.mass_list = []
        self.pos_list = []
    
    def add_mass(self, mass, pos):
        self.mass_list.append(mass)
        self.pos_list.append(pos)
    
    def getcg(self):
        return sum(self.mass_list[i] * self.pos_list[i] for i in range(len(self.mass_list)))/sum(self.mass_list)
    

empty_plane = [(1000, 10)] #change
cargo = [(400, 4.45), (280, 22.5)] #(mass, pos)
passenger_weight = 80
rows = 18
start_passenger_comp = 5.94
length_passenger_comp = 12.29
seat_dist = length_passenger_comp / (rows)
seat = seat_dist / 2 + start_passenger_comp
passengers = []

for pos in range(18):
    passengers.append((4*passenger_weight, seat))
    seat += seat_dist

# change all these 
b = 10
cR = 2
cT = 1
LE_cR = 7
fuel_loc = LE_cR + compute_cg(b, cR, cT)
fuel_weight = 500

fuel = [(2*fuel_weight, fuel_loc)]
