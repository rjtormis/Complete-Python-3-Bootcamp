#Problem 1
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
import math
class Line():

    def __init__(self,coord1,coord2):

        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):

        return math.sqrt((self.coord2[0] - self.coord1[0]) ** 2 + (self.coord2[1] - self.coord1[1])**2)
    
    def slope(self):
        return (self.coord2[1] - self.coord1[1]) / (self.coord2[0] - self.coord1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())