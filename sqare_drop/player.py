INITIAL_STATE,UP,RIGHT,DOWN,LEFT,STAY,ERROR =0,1,2,3,4,5,6

class Player:
    def __init__(self,id,option) -> None:
        self.id = id
        self.pos_x ,self.pos_y = option.initial_pos[id]
        self.state = INITIAL_STATE

    def action(self):
        self.state = 0
        return self.state