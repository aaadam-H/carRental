import pickle

class Car:
    def __init__(self, make, model, year, odometer_reading, status, price_per_hour):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
        self.status = status
        self.price_per_hour = price_per_hour

    def update_odometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("You can't roll back an odometer!")

    def update_car(self, make, model, year, odometer_reading, status, price_per_hour):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
        self.status = status
        self.price_per_hour = price_per_hour

    def get_full_info(self):
        return (f'Make: {self.make}, Model: {self.model}, Year: {self.year}, '
                f'Odometer: {self.odometer_reading} miles, Status: {self.status}, '
                f'Price per hour: RM{self.price_per_hour}')

def save_cars(cars, filename='cars.txt'):
    with open(filename, 'wb') as file:
        pickle.dump(cars, file)

def load_cars(filename='cars.txt'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def display_cars(cars):
    for index, car in enumerate(cars):
        print(f'{index + 1}. {car.make} {car.model} ({car.year}) - {car.status} - RM{car.price_per_hour}/hour')

def main():
    print("Welcome to the car rental system")
    renter = (input("Are you renter? (y/n): ").lower() == 'y')

    cars = load_cars()

    if renter:
        print("Available cars:")
        display_cars(cars)
        choice_index = int(input("Enter the number of the car you want to rent: ")) - 1
        rental_hours = int(input("Enter the number of hours you want to rent: "))

        if 0 <= choice_index < len(cars):
            cars[choice_index].status = 'Rented'
            total_cost = cars[choice_index].price_per_hour * rental_hours
            print(f'Total price: RM{total_cost}')
            save_cars(cars)
        else:
            print("Invalid choice")
    else:
        password = input("Enter the admin password: ") == 'admin123'

        if not password:
            print("Incorrect password")
            exit()

        print("Welcome to the admin panel")
        choice = int(input("Choose an option: 1. Add car 2. Update car 3. Remove car: "))
        if choice == 1:
            make = input("Enter the make of the car: ")
            model = input("Enter the model of the car: ")
            year = int(input("Enter the year of the car: "))
            odometer_reading = int(input("Enter the odometer reading of the car: "))
            status = 'Available'
            price_per_hour = int(input("Enter the price per hour of the car: "))
            new_car = Car(make, model, year, odometer_reading, status, price_per_hour)
            cars.append(new_car)
            print(f'{make} {model} added to the list of cars')
            save_cars(cars)
            display_cars(cars)
        elif choice == 2:
            display_cars(cars)
            choice_index = int(input("Enter the number of the car you want to update: ")) - 1
            if 0 <= choice_index < len(cars):
                update_choice = int(input("Choose what to update: 1. Odometer reading 2. Price per hour: "))
                if update_choice == 1:
                    new_odometer_reading = int(input("Enter the new odometer reading: "))
                    cars[choice_index].update_odometer(new_odometer_reading)
                    print(f'Odometer reading for {cars[choice_index].make} {cars[choice_index].model} updated to {new_odometer_reading}')
                elif update_choice == 2:
                    new_price_per_hour = int(input("Enter the new price per hour: "))
                    cars[choice_index].price_per_hour = new_price_per_hour
                    print(f'Price per hour for {cars[choice_index].make} {cars[choice_index].model} updated to RM{new_price_per_hour}')
                else:
                    print("Invalid choice")
                save_cars(cars)
            else:
                print("Invalid choice")
        elif choice == 3:
            display_cars(cars)
            choice_index = int(input("Enter the number of the car you want to remove: ")) - 1
            if 0 <= choice_index < len(cars):
                removed_car = cars.pop(choice_index)
                print(f'{removed_car.make} {removed_car.model} has been removed from the list of cars')
                save_cars(cars)
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")

if __name__ == '__main__':
    """cars = [
        Car('Perodua', 'Axia', 2010, randint(100,999999), 'Available', 5),
        Car('Perodua', 'Myvi', 2015, randint(100,999999), 'Available', 10),
        Car('Honda', 'City', 2018, randint(100,999999), 'Available', 15),
        Car('Toyota', 'Camry', 2019, randint(100,999999), 'Available', 20),
        Car('Toyota', 'Vellfire', 2020, randint(100,999999), 'Available', 25)
    ]
    save_cars(cars)
"""
    main()


