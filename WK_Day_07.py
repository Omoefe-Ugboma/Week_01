# Working IF Statement
# ATM Withdrawal
# balance = 5000
# withdraw = int(input("Amount: "))
# if withdraw <= balance:
#     print("Withdrawal Approved")
# else:
#     print("Invalid Amount, please topup your balance")   

# E-Commerce Discount
# purchase = int(input("Purchase Amount: "))
# if purchase >= 1000:
#     print("10% Discount Applied")
# else:
#     print("No Discount Applied")

# Model Access Control
# subscription = input("Subscription")
# if subscription == "premium":
#     print("GPT-5 Access Granted")
# else:
#     print("GPT-5 Access Denied")

# score = int(input("Score:  "))
# if score >= 50:
#     print("Pass")
# if score < 50:
#     print("Fail")
    
score = int(input("Score:  "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")