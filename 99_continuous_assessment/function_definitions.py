def isOptionValid(optionType):
    if not optionType.isnumeric():
        print("Please enter a valid digit!")
        return False
    optionType = int(optionType)
    if optionType > 3 or optionType < 1:
        print("Please enter a valid option!")
        return False
    return True

def transactionFee(pPaymentType):
    if pPaymentType == 1:
        return 1
    elif pPaymentType == 2:
        return 1.1
    else:
        return 1.2

def policyOutput(pPolicyType):
    if pPolicyType == 1:
        return "Car insurance"
    elif pPolicyType == 2:
        return "Home insurance"
    else:
        return "Mobile Phone insurance"

def paymentOutput(pPaymentType):
    if pPaymentType == 1:
        return "Bank transfer"
    elif pPaymentType == 2:
        return "PayPal"
    else:
        return "Credit Card"

def paymentInterval(pPolicyType):
    if pPolicyType < 3:
        return "Yearly"
    else:
        return "Monthly"

def isInputValid(pInputOption):
    if not pInputOption.isnumeric():
        print("Please enter a valid digit!")
        return False
    pInputOption = int(pInputOption)
    if pInputOption > 2 or pInputOption < 1:
        print("Please enter a valid option!")
        return False
    return True
