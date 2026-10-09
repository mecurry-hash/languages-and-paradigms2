# Q1
inventory = {
    "Laptop": {"price": 800, "quantity": 5},
    "Mouse": {"price": 20, "quantity": 2},
    "Keyboard": {"price": 50, "quantity": 10},
    "Monitor": {"price": 150, "quantity": 3}
}

def check_low_stock(threshold):
    print("Items Running Low on Stock:")
    
    for item, details in inventory.items():
        if details["quantity"] < threshold:
            print(item)

check_low_stock(4)  

# Q2

flight_route = [
    ("New Orleans", "Atlanta"),
    ("Atlanta", "Chicago"),
    ("Chicago", "New York")
]

def print_itinerary(route_list):
    print("\nFlight Itinerary:")

    for departure, arrival in route_list:
        print(departure, "->", arrival)

print_itinerary(flight_route)