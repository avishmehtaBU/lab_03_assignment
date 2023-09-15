flights = {
    "AI161E90": ("BLR", "BOM", 5600),
    "BR161F91": ("BOM", "BBI", 6750),
    "AI161F99": ("BBI", "BLR", 8210),
    "VS171E20": ("JLR", "BBI", 5500),
    "AS171G30": ("HYD", "JLR", 4400),
    "AI131F49": ("HYD", "BOM", 3499)
}

cities = {
    "BLR": "Bengaluru",
    "BOM": "Mumbai",
    "BBI": "Bhubaneswar",
    "HYD": "Hyderabad",
    "JLR": "Jabalpur"
}


#I AM MAKING SOME CHANGES

def flight_info(f_ID=None, source_city=None, dest_city=None):
    if f_ID:
        if f_ID in flights:
            source, dest, price = flights[f_ID]
            print(f"Flight ID: {f_ID}")
            print(f"Source: {cities[source]}")
            print(f"Destination: {cities[dest]}")
            print(f"Price: {price}")
        else:
            print("Flight not found.")
    elif source_city:
        matches = [(fid, source, dest, price) for fid, (source, dest, price) in flights.items() if source == source_city]
        if matches:
            print("Flights from", cities[source_city])
            for fid, source, dest, price in matches:
                print(f"Flight ID: {fid}")
                print(f"Destination: {cities[dest]}")
                print(f"Price: {price}")
        else:
            print("No flights found from", cities[source_city])
    elif dest_city:
        matches = [(fid, source, dest, price) for fid, (source, dest, price) in flights.items() if dest == dest_city]
        if matches:
            print("Flights to", cities[dest_city])
            for fid, source, dest, price in matches:
                print(f"Flight ID: {fid}")
                print(f"Source: {cities[source]}")
                print(f"Price: {price}")
        else:
            print("No flights found to", cities[dest_city])
    else:
        print("Please provide valid input.")

user_input_type = int(input("Enter 1 for Flight ID, 2 for source city, or 3 for destination city: "))
if user_input_type == 1:
    f_ID = input("Enter Flight ID: ")
    flight_info(f_ID=f_ID)
elif user_input_type == 2:
    source_city = input("Enter source city: ")
    flight_info(source_city=source_city)
elif user_input_type == 3:
    dest_city = input("Enter destination city: ")
    flight_info(dest_city=dest_city)
else:
    print("Invalid input type.")
