class Pupil:
    
    def __init__(self, roll_number, name, english, math, physic, chemistry, cs):
        self.roll_number = roll_number
        self.name = name
        self.english = english
        self.math = math
        self.physic = physic
        self.chemistry = chemistry
        self.cs = cs
    
    def __str__(self):
        return f"Roll_number: {self.roll_number}, Name: {self.name}, Math: {self.math}, Physic: {self.physic}, Chemistry: {self.chemistry}, Cs: {self.cs}"


class pupil_sys:
    
    def __init__(self):
        self.pupils = []
    
    def main_menu(self):
        while True:
            print("1, REPORT MENU")
            print("2. ADMIN MENU")
            print("3. EXIT")
            choice = input("Enter choice(1-3): ")
            if choice == "1":
                self.report_menu()
            elif choice == "2":
                self.admin_menu()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def report_menu(self):
        print("\nREPORT MENU:")
        print("1. CLASS RESULT")
        print("2. PUPIL REPORT CARD")
        print("3. BACK TO MAIN MENU")

    def admin_menu(self):
        while True:
            print("\nADMIN MENU")
            print("1. CREATE PUPIL RECORD")
            print("2. DISPLAY ALL PUPIL RECORD")
            print("3. SEARCH PUPIL RECORD")
            print("4. MODIFY PUPIL RECORD")
            print("5. DELETE PUPIL RECORD")
            print("6. BACK TO MAIN MENU")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_pupil_record()
            elif choice == "2":
                self.display_all_pupil_records()
            elif choice == "3":
                self.search_pupil_record()
            elif choice == "4":
                self.modify_pupil_record()
            elif choice == "5":
                self.delete_pupil_record()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
    
    
    def create_pupil_record(self):
        roll_number = input("Enter roll number: ")
        name = input("Enter name: ")
        english = input("Enter Marks in English: ")
        math = input("Enter Marks in Maths: ")
        physic = input("Enter Marks in Physics: ")
        chemistry = input("Enter Marks in Chemistry: ")
        cs = input("Enter Marks in CS: ")
        pupil = Pupil(roll_number, name, english, math, physic, chemistry, cs)
        self.pupils.append(pupil)
        while True:
            choice = input("Wants to enter more record (y/n)?: ")
            if choice.lower() == 'y':
                create_pupil_record(self)
                continue
            elif choice.lower() == 'n':
                break
            else:
                print("Invalid choice")
                continue
    
    
    def display_all_pupil_records(self):
        if not self.pupils:
            print("No pupil records found")
        else:
            print("\nPUPIL DETAILS.. :")
            for pupil in self.pupils:
                print(f"Name: {pupil.name}, \nRoll Number:{pupil.roll_number}, \nEng:{pupil.english}, \nMath:{pupil}, \nPhy: {pupil.physic}, \nChe, {pupil.chemistry},\nCs: {pupil.cs}")
     
    def search_pupil_record(self):
        roll_number = input("Enter thr rollno you want to search: ")
        for pupil in self.pupils:
            if pupil.roll_number == roll_number:
                print(f"PUPIL DETAILS - Name: {pupil.name}, \nRoll Number:{pupil.roll_number}, \nEng:{pupil.english}, \nMath:{pupil}, \nPhy: {pupil.physic}, \nChe, {pupil.chemistry},\nCs: {pupil.cs}")
                return
        print("Pupil not found")
    
    
    
    def modify_pupil_record(self):
        roll_number = input("Enter roll number to modify: ")
        for pupil in pupils:
           if pupil.roll_number == roll_number:
             print("Name:", pupil.name)
             while True:
                choice = input("Wants to edit (y/n)?:")
                if choice.lower() == 'y':
                    pupil.name = input("Enter the name ")
                    continue
                elif choice.lower() == 'n':
                    break
                else:
                    print("Invalid choice")
                    continue
                
        print("English marks :",pupil.english)
        while True:
            choice = input("Want to edit (y/n)?:")
            if choice.lower() == 'y':
                pupil.english = input("English marks")
                continue
            elif choice.lower() == 'n':
                break
            else:
                print("Invallid choice")
                continue
    
        print("Math marks :",pupil.math)
        while True:
            choice = input("Want to edit (y/n)?:")
            if choice.lower() == 'y':
                pupil.math = input("Math marks")
                continue
            elif choice.lower() == 'n':
                break
            else:
                print("Invallid choice")
                continue
                
        print("Physics marks :",pupil.physic)
        while True:
            choice = input("Want to edit (y/n)?:")
            if choice.lower() == 'y':
                pupil.physic = input("Physics marks")
                continue
            elif choice.lower() == 'n':
                break
            else:
                print("Invallid choice")
                continue
            
        print("Chemistry marks :",pupil.chemistry)
        while True:
            choice = input("Want to edit (y/n)?:")
            if choice.lower() == 'y':
                pupil.chemistry = input("Chemistry marks")
                continue
            elif choice.lower() == 'n':
                break
            else:
                print("Invallid choice")
                continue
            
        print("CS marks :",pupil.cs)
        while True:
            choice = input("Want to edit (y/n)?:")
            if choice.lower() == 'y':
                pupil.cs = input("CS marks")
                continue
            elif choice.lower() == 'n':
                break
            else:
                print("Invallid choice")
                continue
        print("Record updated")
        
    
    def delete_pupil_record(self):
         roll_number = input("Enter roll number to delete: ")
         for pupil in self.pupils:
            if pupil.roll_number == roll_number:
                self.pupils.remove(pupil)
                print("record found and deleted")
                return
    
        
    def class_result(self):
        if not self.pupils:
            print("No record found")
        else:
            for pupil in pupils:
                print(f"Name: {pupil.name}, \nRoll Number:{pupil.roll_number}, \nEng:{pupil.english}, \nMath:{pupil}, \nPhy: {pupil.physic}, \nChe, {pupil.chemistry},\nCs: {pupil.cs}")
    
    def pupil_report_card(self):
        roll_number = input("Enter thr rollno you want to search: ")
        for pupil in self.pupils:
            if pupil.roll_number == roll_number:
                print(f"PUPIL DETAILS - Name: {pupil.name}, \nRoll Number:{pupil.roll_number}, \nEng:{pupil.english}, \nMath:{pupil}, \nPhy: {pupil.physic}, \nChe, {pupil.chemistry},\nCs: {pupil.cs}")
                return
        print("Pupil not found")
    
    def run_system(self):
        while True:
            self.main_menu()
            choice = input("Enter choice(1-3): ")

            if choice == "1":
                self.report_menu()
                report_choice = input("Enter choice(1-3): ")
                if report_choice == "1":
                    self.class_result()
                elif report_choice == "2":
                    self.pupil_report_card()
                elif report_choice == "3":
                    continue
            
            elif choice == "2":
                while True:
                    self.admin_menu()
                    admin_choice = input("Enter choice(1-6): ")
                    if admin_choice == "1":
                        self.create_pupil_record()
                    elif admin_choice == "2":
                        self.display_all_pupil_records()
                    elif admin_choice == "3":
                        self.search_pupil_record()
                    elif admin_choice == "4":
                        self.modify_pupil_record()
                    elif admin_choice == "5":
                        self.delete_pupil_record()
                    elif admin_choice == "6":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            
            elif choice == "3":
                print("Existing the Pupil Management System")
                break
            else:
                print("Invalid choice. Please try again")
if __name__ == "__main__":
    system = pupil_sys()
    system.run_system()


    
    
                
     
    
    
    
        
         
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    
                
     
            
             