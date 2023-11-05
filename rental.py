class User():
    def __init__(self, name):
        self.name = name
        self.properties = []


class Properties():
    def __init__(self):
        self.expenses = 0
        self.income = 0
        self.investments = 0
        self.roi = 0
    
    def calculate_roi(self):
        investment = input("What is the total worth of the property? ")
        property_income = input("What the annual income of the property? ")
        property_expenses = input("What is the total expenses of the property? ")
        self.roi = ((int(property_income) - int(property_expenses))/int(investment)) * 100
        print(f"This is your return of investment: {self.roi}")
    
class ROI():
    def __init__(self):
        self.users = []
        self.current_user = None

    def run():
        
        while True:
            response = input("Do you want to add a user, change a user, add a property, get ROI or quit? ")
            if response.strip().lower() == "add a user":
                userName = input("What is the name of this new user? ")
                user = User(userName)
                roiUser = ROI()
                roiUser.users.append(user)
                roiUser.current_user = user
            elif response.strip().lower() == "change a user":
                check_name = input("What is the name of the user you want to change to? ")
                if check_name in roiUser.users and check_name != roiUser.curren_user:
                    roiUser.current_user = check_name
                else:
                    print("This user is not in the list, or it is type incorrectly.")
            elif response.strip().lower() == "add a property":
                new_property = input("What kind of property would you like to add? ")
                user.properties.append(new_property)
            elif response == "get ROI":
                user_property = Properties()
                user_property.calculate_roi()
            elif response.strip().lower() == "quit":
                print("Enjoy your vacation user!")
                break
            else:
                print("Typed incorrectly, choose an option please.")

ROI.run()