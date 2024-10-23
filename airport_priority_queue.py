import heapq

class Airplane:
    def __init__(self, id, status, priority):
        self.id = id 
        self.status = status  
        self.priority = priority 

    def __lt__(self, other):
        return self.priority < other.priority  

    def __repr__(self):
        return f"Airplane {self.id} ({self.status}, Priority: {self.priority})"

class Airport:
    def __init__(self):
        self.queue = []

    def add_airplane(self, airplane):
        heapq.heappush(self.queue, airplane) 

    def land(self):
        if len(self.queue) > 0:
            next_airplane = heapq.heappop(self.queue)  
            print(f"Landing: {next_airplane}")
        else:
            print("No airplanes waiting to land")

    def display_queue(self):
        print("Current landing queue:")
        for airplane in self.queue:
            print(airplane)


if __name__ == "__main__":
    airport = Airport()
    airplane1 = Airplane(id="ABC123", status="emergency", priority=1)
    airplane2 = Airplane(id="XYZ456", status="low fuel", priority=2)
    airplane3 = Airplane(id="DEF789", status="standard", priority=3)
    airport.add_airplane(airplane1)
    airport.add_airplane(airplane2)
    airport.add_airplane(airplane3)
    airport.display_queue()
    airport.land()
    airport.display_queue()
