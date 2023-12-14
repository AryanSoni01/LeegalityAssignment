class ParkingSpace:
    def __init__(self, vehicle_number=None):
        self.vehicle_number = vehicle_number

    def park(self, vehicle_number):
        if self.vehicle_number is None:
            self.vehicle_number = vehicle_number
            return True
        return False

    def unpark(self):
        if self.vehicle_number is not None:
            vehicle_number = self.vehicle_number
            self.vehicle_number = None
            return vehicle_number
        return None

class ParkingLevel:
    def __init__(self, level_name, capacity):
        self.level_name = level_name
        self.capacity = capacity
        self.spaces = [ParkingSpace() for _ in range(capacity)]

    def find_empty_spot(self):
        for i, space in enumerate(self.spaces):
            if space.vehicle_number is None:
                return i + 1 # since parking space numbers starts from 1 
        return None

class ParkingLot:
    def __init__(self):
        self.levels = [ParkingLevel('A', 20), ParkingLevel('B', 20)]

    def park_vehicle(self, vehicle_number):
        for level in self.levels:
            spot = level.find_empty_spot()
            if spot is not None:
                level.spaces[spot - 1].park(vehicle_number)
                return {"level": level.level_name, "spot": spot}
        return None

    def retrieve_parking_spot(self, vehicle_number):
        for level in self.levels:
            for i, space in enumerate(level.spaces):
                if space.vehicle_number == vehicle_number:
                    return {"level": level.level_name, "spot": i + 1}
        return None

    def unpark_vehicle(self, vehicle_number):
        for level in self.levels:
            for space in level.spaces:
                if space.vehicle_number == vehicle_number:
                    return space.unpark()
        return None

    def retrieve_nearest_parking_spot(self):
        for level in self.levels:
            spot = level.find_empty_spot()
            if spot is not None:
                return {"level": level.level_name, "spot": spot}
        return None

if __name__ == "__main__":
    parking_lot = ParkingLot()

    while True:
        print("\nWelcome to Leegality Parking Lot, Please Select one of the following options")
        print("Options:")
        print("1. Park a vehicle")
        print("2. Retrieve parking spot")
        print("3. Unpark a vehicle")
        print("4. Retrieve nearest parking spot")
        print("5. Exit")

        choice = input("Please enter your choice: ")

        if choice == '1':
            vehicle_number = input("Please enter your vehicle number: ")
            result = parking_lot.park_vehicle(vehicle_number)
            if result:
                print(f"-->Your vehicle can be parked at Level {result['level']}, Spot {result['spot']}")
            else:
                print("-->Sorry, Parking is currently full.")

        elif choice == '2':
            vehicle_number = input("Please enter your vehicle number: ")
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            if result:
                print(f"-->Your vehicle is parked at Level {result['level']}, Spot {result['spot']}")
            else:
                print("-->Sorry, vehicle is not parked in here.")

        elif choice == '3':
            vehicle_number = input("Please enter your vehicle number: ")
            result = parking_lot.unpark_vehicle(vehicle_number)
            if result:
                print(f"-->Unparked vehicle with number {result}")
            else:
                print("-->Sorry, vehicle is not parked here.")

        elif choice == '4':
            result = parking_lot.retrieve_nearest_parking_spot()
            if result:
                print(f"-->Nearest empty spot is available at Level {result['level']}, Spot {result['spot']}")
            else:
                print("-->Sorry, No empty parking spots are available.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter the valid choice from the above options.")
