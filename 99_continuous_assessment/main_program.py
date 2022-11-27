# Import the functions
import function_definitions

# Ask the user for all the inputs
usersName = input("Please enter your name...\n")
policyDuration = input("Please enter the duration of the insurance policy in years...\n")
policyDuration = float(policyDuration)
while True:
    print("""
    Policy types:
    1. Car insurance
    2. Home insurance
    3. Mobile Phone insurance
    """)
    policyType = input("Please enter an option between 1 and 3...\n")
    if not function_definitions.isOptionValid(policyType):
            continue
    policyType = int(policyType)
    break
 
while True:
    print("""
    Payment types:
    1. Bank transfer
    2. PayPal
    3. Credit Card
    """)
    paymentType = input("Please enter an option between 1 and 3...\n")
    if not function_definitions.isOptionValid(paymentType):
        continue
    paymentType = int(paymentType)
    break

# Calculate Total Cost
totalCost = 0

if policyType == 1:
    totalCost = 500 * policyDuration * function_definitions.transactionFee(paymentType)
elif policyType == 2:
    totalCost = 1000 * policyDuration * function_definitions.transactionFee(paymentType)
else:
    totalCost = 10 * 12 * policyDuration * function_definitions.transactionFee(paymentType)

# Print summary of the policy terms
print("***Summary of your Insurance Policy***")
print("Name of the policy holder:", usersName)
print("Duration of the insurance policy:", policyDuration, "years")
print("Policy type:", function_definitions.policyOutput(policyType))
print("Payment type:", function_definitions.paymentOutput(paymentType))
print("Payment interval:", function_definitions.paymentInterval(policyType))
print("Total cost over the entire duration of the policy: £", round(totalCost,2))