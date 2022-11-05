import googlemaps
  
# Requires API key
gmaps = googlemaps.Client(key='AIzaSyDsYaL4XUdBro5FWjClEe_CUIyZr-RaII0')

print("1 - Mini Cooper      - 34 MPG - Max Speed: 165 MPH")
print("2 - Toyota Camry     - 33 MPG - Max Speed: 135 MPH")
print("3 - Honda Odyssey    - 24 MPG - Max Speed: 111 MPH")
print("4 - Cadillac DeVille - 22 MPG - Max Speed: 124 MPH")
print("5 - Ford F-150       - 25 MPG - Max Speed: 120 MPH")
car = input("Please type the number of the car you want: ")
s = input("What speed are you traveling in MPH?: ")

try:
    car = int(car)
    s = int(s)
except:
    print("Please enter the proper answers!")
    exit()

l = input("Location: ")
d = input("Destination: ")

# Requires cities name
my_dist = gmaps.distance_matrix(l,d)['rows'][0]['elements'][0]["distance"]["value"]
my_dist = float(my_dist)/1000
my_dist = my_dist/1.609

t = my_dist/s

h = int(t)
m = t - h
m = round(60 * m, 1)

# Printing the result
print("The time it will take to reach you desination is " + str(h) + " hours and " + str(m) + " minute when traveling at " + str(s) + " MPH.")