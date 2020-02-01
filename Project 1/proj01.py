rods = float(input("Input rods: "))

print("You input {} rods.".format(rods))

meters = rods * 5.0292
feet = meters / 0.3048
miles = meters / 1609.34
furlongs = rods / 40
hours = miles / 3.1 
minutes = hours * 60

print("")
print("Conversions")
print("Meters: {}".format(round(meters, 3)))
print("Feet: {}".format(round(feet, 3)))
print("Miles: {}".format(round(miles, 3)))
print("Furlongs: {}".format(round(furlongs, 3)))
print("Minutes to walk {} rods: {}".format(rods, round(minutes, 3)))