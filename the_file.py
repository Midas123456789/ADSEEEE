class plane:
    def __init__(self):
        self.mass_list = []
        self.pos_list = []
    
    def add_mass(self, mass, pos):
        self.mass_list.append(mass)
        self.pos_list.append(pos)
    
    def getcg(self):
        return sum(self.mass_list[i] * self.pos_list[i] for i in range(len(self.mass_list)))/sum(self.mass_list)
    
