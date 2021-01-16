import random

names = []

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus"]

print(planets)

planets.append("Neptune")
planets.append("*Pluto")

print(planets)
print(planets[1])
print(planets[-1])

print("----------")

for planet in planets:
  print(planet)
  
print("----------")

for num in range(len(planets)):
  print(planets[num])

print("----------")
print(planets[random.randint(0, len(planets))])
