class Phone:
    def __init__(self, brand, model, storage, chipset, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.chipset = chipset
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")
        print(f"Chipset: {self.chipset}")
        print(f"Color: {self.color}")

    def modify_phone(self, brand=None, model=None, storage=None, chipset=None, color=None):
        if brand:
            self.brand = brand
        if model:
            self.model = model
        if storage:
            self.storage = storage
        if chipset:
            self.chipset = chipset
        if color:
            self.color = color

def delete_phone(phone_list, index):
    if 0 <= index < len(phone_list):
        del phone_list[index]
    else:
        print("Invalid index, cannot delete phone object. ʕ•́ᴥ•̀ʔっ")

def main_menu():
    phone_list = []

    while True:
        print("\nMain Menu:")
        print("1. Add Phone")
        print("2. View Phones")
        print("3. Modify Phone")
        print("4. Delete Phone")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            brand = input("Enter phone brand: ")
            model = input("Enter phone model: ")
            storage = input("Enter storage capacity (GB): ")
            chipset = input("Enter chipset type: ")
            color = input("Enter phone color: ")
            new_phone = Phone(brand, model, storage, chipset, color)
            phone_list.append(new_phone)

        elif choice == '2':
            if not phone_list:
                print("No phones available. ʕ•́ᴥ•̀ʔっ")
            else:
                for idx in range(len(phone_list)):
                    print(f"\nPhone {idx + 1}:")
                    phone_list[idx].display_info()

        elif choice == '3':
            if not phone_list:
                print("No phones available to modify. ʕ•́ᴥ•̀ʔっ")
            else:
                index = int(input("Enter the phone number to modify (1-5): ")) - 1
                if 0 <= index < len(phone_list):
                    print("Enter new details (leave blank to keep current values):")
                    brand = input("New Brand: ")
                    model = input("New Model: ")
                    storage = input("New Storage (GB): ")
                    chipset = input("New Chipset: ")
                    color = input("New Color: ")
                    phone_list[index].modify_phone(brand, model, storage, chipset, color)
                else:
                    print("Invalid phone number.")

        elif choice == '4':
            if not phone_list:
                print("No phones available to delete. ʕ•́ᴥ•̀ʔっ")
            else:
                index = int(input("Enter the phone number to delete (1-5): ")) - 1
                delete_phone(phone_list, index)

        elif choice == '5':
            print("Exiting program... ʕ•́ᴥ•̀ʔっ")
            break

        else:
            print("Invalid choice. Please try again. ʕ•́ᴥ•̀ʔっ")

main_menu()
