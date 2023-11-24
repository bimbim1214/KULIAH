from Point import *
p1=Point() #object p1
p1.x=2
p1.y=4
p2=Point() #object p2
p2.set_location(3,4)
print(p2.x)
#origin={0,0}
print(p2.distance_from_origin())
print(p2.distance(p1)) #other=p1
print(p2)