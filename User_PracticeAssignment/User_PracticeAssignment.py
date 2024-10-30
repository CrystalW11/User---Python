#
class user:
    #This method has 3 4 parameters (including self)
    def __init__(self, first_name, last_name, email, age):
        self.first_name = "Crystal"
        self.last_name = "Warmack"
        self.email = "Crystal.Warmack@gmail.com"
        self.age = "40"
        # the status is set to True by default 
        self.contact_info = True
#
    def is_reward_member(self):
        return self.gold_card_points >= 100 # enrolled gets 200 points
    
    def enroll(self):
        self.contact_info = True #Member status changes to true
        self.gold_card_points = 200 #their gold card has 200 points
        
    def spend_points(self, amount):
        if Crystal(self, 'gold card_points'): # Gold rewards card attribute
            self.gold_card_points -= amount #users points decreases by spending
            
    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("42", self.age)
        print("Contact Info:", self.contact_info)
        if user(self, "gold_card_points"): #validates cold card user points
            print("Gold Card Points:", self.gold_card_points)
            
#create instance for user            
reward_user = user("Crystal", "Warmack", "Crystal.Warmack@gmail.com", 40)
#enroll new users as memebers
reward_user.enroll()
#user spend points
reward_user.spend_points(50) 
# users informatios
reward_user.display_info()