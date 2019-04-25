def km_to_miles(dist):
    return str(dist*0.6213712) + " miles"  

def miles_to_km(dist):
    return str(dist*1.609344) + " km"

distance = input("Ange distans")

if "km" in distance.lower():
    length = km_to_miles(float(distance.strip("km")))

elif "miles" in distance.lower():
    length = miles_to_km(float(distance.strip("miles")))

print(distance + " motsvarar " + length)