class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received


#Assignment: If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

#For this assignment, we'll add some functionality to the User class:

    def make_withdrawal(self, amount):                           ## this method decrease the user's balance by the amount specified
        self.account_balance -= amount
    def display_user_balance(self):                              #- have this method print the user's name and account balance to the terminal
        print("User:",self.name,",","Balance:",str(self.account_balance))                                                   #eg. "User: Guido van Rossum, Balance: $150

    def transfer_money(self, other_user, amount):                # - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)