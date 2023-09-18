import re
import datetime
from collections import defaultdict

def hash_password(password):
    hashed_password = ""
    salt = 3
    for num in password:
        hashed_password += str(ord(num)+salt)
    return hashed_password

emailpass = {"jg@gmail.com":("abcD@1234","jg","1234")}
lastpasswords = defaultdict(list)
lastpasswords["jg@gmail.com"].append(hash_password("abcD@1234")) 

class FlightReservationSystem:
    def __init__(self):
        self.flights = {}
        self.bookings = []

    def add_flight(self, flight_number, flight_info):
        self.flights[flight_number] = flight_info

    def edit_flight(self, flight_number, flight_info):
        if flight_number in self.flights:
            self.flights[flight_number] = flight_info
            print("Flight information updated.")
        else:
            print("Flight not found.")

    def delete_flight(self, flight_number):
        if flight_number in self.flights:
            del self.flights[flight_number]
            print("Flight deleted.")
        else:
            print("Flight not found.")

    def view_all_flights(self):
        for flight_number, flight_info in self.flights.items():
            print(f"Flight Number: {flight_number}")
            for key, value in flight_info.items():
                print(f"{key}: {value}")
            print()

    def search_flights(self, departure_airport=None, arrival_airport=None, departure_time=None):
        found_flights = []
        for flight_number, flight_info in self.flights.items():
            if (not departure_airport or flight_info.get("Departure Airport") == departure_airport) \
                    and (not arrival_airport or flight_info.get("Arrival Airport") == arrival_airport) \
                    and (not departure_time or flight_info.get("Departure Time") == departure_time):
                found_flights.append((flight_number, flight_info))
        return found_flights

    def view_booking_history(self):
        for booking in self.bookings:
            print("Booking History:")
            for key, value in booking.items():
                print(f"{key}: {value}")
            print()

    def search_booking_history(self, flight_number=None, departure_time=None):
        found_bookings = []
        for booking in self.bookings:
            if (not flight_number or booking.get("Flight Number") == flight_number) \
                    and (not departure_time or booking.get("Departure Time") == departure_time):
                found_bookings.append(booking)
        return found_bookings

    def make_booking(self, booking_info):
        self.bookings.append(booking_info)
        print("Booking successfully made.")


def enter_admin():
    print("MODULE 4")
    system = FlightReservationSystem()
    while True:
        print("\nFlight Reservation System Menu:")
        print("1. Add Flight")
        print("2. Edit Flight")
        print("3. Delete Flight")
        print("4. View All Flights")
        print("5. Search Flights")
        print("6. View Booking History")
        print("7. Search Booking History")
        print("8. Make Booking")
        print("9. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            flight_number = input("Enter Flight Number: ")
            flight_info = {
                "Flight Name": input("Enter Flight Name: "),
                "Departure Airport": input("Enter Departure Airport: "),
                "Arrival Airport": input("Enter Arrival Airport: "),
                "Departure Date": input("Enter Departure Date: "),
                "Departure Time": input("Enter Departure Time: "),
                "Arrival Time": input("Enter Arrival Time: "),
                "Seats Available": input("Enter Seats Available: "),
                "Flight Status": input("Enter Flight Status: "),
            }
            system.add_flight(flight_number, flight_info)
        elif choice == "2":
            flight_number = input("Enter Flight Number to Edit: ")
            flight_info = {
                "Flight Name": input("Enter Flight Name: "),
                "Departure Airport": input("Enter Departure Airport: "),
                "Arrival Airport": input("Enter Arrival Airport: "),
                "Departure Date": input("Enter Departure Date: "),
                "Departure Time": input("Enter Departure Time: "),
                "Arrival Time": input("Enter Arrival Time: "),
                "Seats Available": input("Enter Seats Available: "),
                "Flight Status": input("Enter Flight Status: "),
            }
            system.edit_flight(flight_number, flight_info)
        elif choice == "3":
            flight_number = input("Enter Flight Number to Delete: ")
            system.delete_flight(flight_number)
        elif choice == "4":
            system.view_all_flights()
        elif choice == "5":
            departure_airport = input("Enter Departure Airport (or leave empty): ")
            arrival_airport = input("Enter Arrival Airport (or leave empty): ")
            departure_time = input("Enter Departure Time (or leave empty): ")
            found_flights = system.search_flights(departure_airport, arrival_airport, departure_time)
            for flight_number, flight_info in found_flights:
                print(f"Flight Number: {flight_number}")
                for key, value in flight_info.items():
                    print(f"{key}: {value}")
                print()
        elif choice == "6":
            system.view_booking_history()
        elif choice == "7":
            flight_number = input("Enter Flight Number (or leave empty): ")
            departure_time = input("Enter Departure Time (or leave empty): ")
            found_bookings = system.search_booking_history(flight_number, departure_time)
            for booking in found_bookings:
                print("Booking History:")
                for key, value in booking.items():
                    print(f"{key}: {value}")
                print()
        elif choice == "8":
            booking_info = {
                "Flight Number": input("Enter Flight Number: "),
                "Departure Time": input("Enter Departure Time: "),
                "Passenger Name": input("Enter Passenger Name: "),
                "Seat Number": input("Enter Seat Number: "),
            }
            system.make_booking(booking_info)
        elif choice == "9":
            print("Exiting Flight Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def enter_forget():
    print("MODULE 3")
    while True:
        email = input("Enter YOur Email:\n")        
        if email in emailpass:
            while True:
                    password = input("Enter the password:\n")
                    if is_valid_password(password):                         
                        if hash_password(password) in lastpasswords[email]:
                            while True:
                                password = input("password cannot the last three passwords\n Enter again:\n")
                                if hash_password(password)  not in lastpasswords[email]:
                                    # print("Password Updated Successfuly")
                                    if len(lastpasswords[email])>=3:
                                        lastpasswords[email].pop(0)
                                    break

                        a,b,c = emailpass.get(email)
                        emailpass[email] = (hash_password(password),b,c)             
                        print("Password Updated Successfully")
                        lastpasswords[email].append(hash_password(password))
                        enter_admin()
                        break
                    else:
                        print("Invalid password. Please try again.")
            break
        else: print("Email not in the database")
            
def enter_signUp():
    print("MODULE 1")
    while True:
        email = input("Enter your Email:\n")
        username = input("Enter the username:\n")
        if is_valid_email(email):
            while True:
                password = input("Enter the password:\n")
                if is_valid_password(password):
                    while True:
                        dob = input("Enter the date of birth (YYYY-MM-DD):\n")
                        if is_valid_dob(dob):
                            signup(email, password, username, dob)
                            print("MODULE 2")
                            break  # Exit the loop if signup is successful
                        else:
                            print("Invalid date of birth format. Please try again.")
                    break
                else:
                    print("Invalid password. Please try again.")
            break
        else:
            print("Invalid email. Please try again.")


def enter_signIn():
    email = input("Enter your Email:\n")
    password = input("Enter the Password:\n")
    signIn(email,password)

def signIn(email,password):
    if email in emailpass and hash_password(password) == emailpass[email][0]:
        print("Login successful")
        enter_forget()#Module 3
        choice = input("press 1 to signup\n press 2 to singIn\n press 3 to forget password\npress 4 to admin and view flights")
        if choice ==  "1":
            enter_signUp()
        elif choice == '2':
            enter_signIn()
        elif choice == '3':
            enter_forget()
        elif choice == '4':
            enter_admin()
    else:print("Email or Password Incorrect")

def is_valid_dob(dob):
    try:
        datetime.datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def is_valid_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!])[A-Za-z\d@#$%^&+=!]{8,15}$"
    return bool(re.match(pattern, password))

def signup(email,password,username,dob):
    if is_valid_password(password) and is_valid_email(email) and \
        email not in  emailpass and email != password and username != password:

        emailpass[email] = (hash_password(password),username,dob)
        lastpasswords[email].append(hash_password(password))

        print(emailpass)        
        choice = input("press 1 to signup press 2 to singIn\n")
        if choice ==  "1":
            enter_signUp()
        else:
            enter_signIn()
    else:
        print("email already exits or Password not valid or email matches password")
        enter_signUp()


enter_signUp()

# enter_forget()
