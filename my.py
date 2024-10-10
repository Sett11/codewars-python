class SiegeState:
    def __init__(self):
        self.damage=20
        self.canMove=False

class TankState:
    def __init__(self):
        self.damage=5
        self.canMove=True

class Tank:
    def __init__(self):
        self.state=TankState()

    def can_move(self):
        return self.state.canMove
    
    def damage(self):
        return self.state.damage