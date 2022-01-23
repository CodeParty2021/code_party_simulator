class Player:
    UP,RIGHT,DOWN,LEFT,STAY,ERROR,FALL =0,1,2,3,4,5,6
    SAFE,FALL1,FALL2,FALL3,REVIVED = 0,1,2,3,4
    def __init__(self,id,option) -> None:
        self.id = id
        self.pos_x ,self.pos_y = option.initial_pos[id]
        self.state = self.SAFE
    
    def action(self,state):
        if(self.state == self.SAFE):
            return self.UP
        return self.FALL
    
    def get_pos(self):
        return (self.pos_x,self.pos_y)

    def set_pos(self,pos):
        self.pos_x,self.pos_y = pos
    
    def step(self,action):
        if(self.state == self.SAFE):
            if(action==self.UP):
                self.pos_y+=1
            elif(action==self.DOWN):
                self.pos_y-=1
            elif(action==self.RIGHT):
                self.pos_x+=1
            elif(action==self.LEFT):
                self.pos_x-=1
            elif(action==self.STAY or action==self.ERROR):
                pass
        elif(self.state==self.FALL3):
            self.state==self.FALL2
        elif(self.state==self.FALL2):
            self.state==self.FALL1
        elif(self.state==self.FALL1):
            self.state==self.SAFE
    
    def fall(self):
        self.state = self.FALL3