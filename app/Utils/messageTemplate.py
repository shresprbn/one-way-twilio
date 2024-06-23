import random

class MessageTemplate:
    def __init__(self):
        self.restaurantName = ''
        self.totalAmount = 0
        self.restaurantLocation = {
            'Total Vegan' : '9563 S University Blvd A, Highlands Ranch, CO 80126',
            'Taj Mahal' : '5350 S Santa Fe Dr C, Littleton, CO 80120',
            'Tikka Masala' : '16255 W 64th Ave unit 6, Arvada, CO 80007'
        }
    

    def thankYouMessage(self):
        return f"Thank you for ordering from {self.restaurantName}."
    
    def totalOrderAmount(self):
        return f"You have ordered food of worth {self.totalAmount} from {self.restaurantName}"
    
    def readyForPickup(self):
        return f"Your order is ready for pickup at {self.restaurantLocation[self.restaurantName]} ,{self.restaurantName}"
    
    def recoveryCode(self):
        randomCode = random.randint(100000, 999999)
        return f"The recovery code for reseting your password is {randomCode}", randomCode
    
    def returnMessage(self, restaurantName, type, totalamt = 0):
        self.restaurantName = restaurantName
        self.totalAmount = totalamt
        if type == "Thankyou":
            return self.thankYouMessage()
        elif type == "TotOrderAmt":
            return self.totalOrderAmount()
        elif type == "ReadyPickUp":
            return self.readyForPickup()
        else:
            return "Invalid message type."
        
    