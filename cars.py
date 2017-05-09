
class Car(object):
  speed = 0
def __init__(self,type = "",name = "General",model ="GM"):
        self.type = type
        self.name = name
        self.model = model
        if self.model =="trailer":
            self.num_of_wheels = 8
        elif self.type =="Koenigsegg" or self.type == "Porshe":
            self.num_of_doors = 2
        if self.model == "trailer":
            self.type = "MAN"

def is_saloon(self):
        if self.type != "saloon":
            return  self.type == "trailer"
      

def drive(self, speed):
        assert isinstance(speed, int), "Drive argument must be integer"
        # trailer speed
        if self.type == 'trailer':
            self.speed = speed * 11
            return self
        # saloon speed
        elif self.type == 'saloon':
            self.speed = 10 ** speed
            return self
        else:
            pass
