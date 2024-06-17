class Equipment:
    def __init__(self, eid, name, condition, status):
        self.eid = eid
        self.name = name
        self.condition = condition
        self.status = status

    def to_dict(self):
        return {"Eid": self.eid, "Name": self.name, "Condition": self.condition, "Status": self.status}

class User:
    def __init__(self, usn):
        self.usn = usn
        self.borrowed_equipment = []

    def to_dict(self):
        return {"USN": self.usn, "Borrowed Equipment": self.borrowed_equipment}

class Inventory:
    def __init__(self):
        self.items = {
            1: Equipment(1, "Bat", "Good", "A"),
            2: Equipment(2, "Football", "Average", "A")
        }
        self.students = {}

    def add_equipment(self, eid, name, condition, status):
        if eid in self.items:
            print("Equipment with this EID already exists!")
            return
        self.items[eid] = Equipment(eid, name, condition, status)
        print(f"Equipment {name} added successfully!")

    def delete_equipment(self, eid):
        if eid not in self.items:
            print("Equipment not found!")
            return
        if self.items[eid].status != "A":
            print("Equipment cannot be deleted as its status is not 'Available'.")
            return
        del self.items[eid]
        print(f"Equipment with EID {eid} deleted successfully!")

    def update_equipment(self, eid):
        if eid not in self.items:
            print("Equipment not found!")
            return
        print("What do you want to update?")
        print("1. Name\n2. Condition\n3. Status")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter new name: ")
            self.items[eid].name = name
        elif choice == '2':
            condition = input("Enter new condition: ")
            self.items[eid].condition = condition
        elif choice == '3':
            status = input("Enter new status (A - Available, U - Unavailable): ")
            self.items[eid].status = status
        else:
            print("Invalid choice!")
            return
        print(f"Equipment with EID {eid} updated successfully!")

    def display_inventory(self):
        print("\nInventory:")
        for item in self.items.values():
            print(f"EID: {item.eid}, Name: {item.name}, Condition: {item.condition}, Status: {item.status}")

    def record_of_students(self):
        print("\nRecord of Students:")
        for usn, student in self.students.items():
            print(f"USN: {usn}, Borrowed Equipment: {student['Borrowed Equipment']}")
    
    

class SportsClub:
    def __init__(self):
        self.credentials = {
            "admin": {"username": "admin", "password": "admin@123"},
            "user": {"username": "user", "password": "user@123"}
        }
        self.inventory = Inventory()

    def login(self, user_type):
        username = input("Enter username: ")
        password = input("Enter password: ")

        credentials = self.credentials[user_type]
        if username == credentials["username"] and password == credentials["password"]:
            print(f"{user_type.title()} login successful!")
            if user_type == "admin":
                self.admin_menu()
            else:
                self.user_menu()
        else:
            print("Invalid credentials!")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu")
            print("1. Add Equipment\n2. Delete Equipment\n3. Update Equipment\n4. Display Inventory\n5. Record of Students\n6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                eid = int(input("Enter EID: "))
                if eid in self.inventory.items:
                    print("Equipment with this EID already exists!")
                    continue
                name = input("Enter name: ")
                condition = input("Enter condition: ")
                status = input("Enter status (A - Available, U - Unavailable): ")
                self.inventory.add_equipment(eid, name, condition, status)
            elif choice == '2':
                eid = int(input("Enter EID to delete: "))
                self.inventory.delete_equipment(eid)
            elif choice == '3':
                eid = int(input("Enter EID to update: "))
                self.inventory.update_equipment(eid)
            elif choice == '4':
                self.inventory.display_inventory()
            elif choice == '5':
                self.inventory.record_of_students()
            elif choice == '6':
                print("Exiting Admin Menu!")
                break
            else:
                print("Invalid choice!")

    def user_menu(self):
        while True:
            print("\nUser Menu")
            print("1. Borrow Equipment\n2. Return Equipment\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.borrow_equipment()
            elif choice == '2':
                usn = input("Enter your USN: ")
                eid = int(input("Enter EID of equipment to return: "))
                self.return_equipment(usn, eid)
            elif choice == '3':
                print("Exiting User Menu!")
                break
            else:
                print("Invalid choice!")

    def borrow_equipment(self):
        self.inventory.display_inventory()
        eid = int(input("Enter EID of equipment to borrow (or 0 to exit): "))
        if eid == 0:
            return
        if eid not in self.inventory.items or self.inventory.items[eid].status == "U":
            print("Equipment unavailable!")
            return
        usn = input("Enter your USN: ")
        if usn not in self.inventory.students:
            self.inventory.students[usn] = {"Borrowed Equipment": []}
        self.inventory.students[usn]["Borrowed Equipment"].append(eid)
        self.inventory.items[eid].status = "U"
        print(f"Equipment with EID {eid} borrowed successfully!")

    def return_equipment(self, usn, eid):
        if usn in self.inventory.students and eid in self.inventory.students[usn]["Borrowed Equipment"]:
            self.inventory.students[usn]["Borrowed Equipment"].remove(eid)
            self.inventory.items[eid].status = "A"
            print(f"Equipment with EID {eid} returned successfully!")
        else:
            print("Invalid USN or EID. Equipment not found in borrowed list.")


if __name__ == "__main__":
    club = SportsClub()
    while True:
        print("\nSports Club")
        print("1. Login as Admin\n2. Login as User\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            club.login("admin")
        elif choice == '2':
            club.login("user")
        elif choice == '3':
            print("Exiting program!")
            break
        else:
            print("Invalid choice!")