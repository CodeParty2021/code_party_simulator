EMPTY = -1

class Field:
    def __init__(self,option):
        self.width = option.width
        self.height = option.height
        self.generate_field()

    def generate_field(self):
        self.field = [[i]*(self.width+2) for i in range (self.height+2)]

    def mask_field(self):
        return [x[1:self.width+1] for x in self.field[1:self.height+1]]

    def rotate_field(self):
        return list(map(list, zip(*self.field)))[::-1]
