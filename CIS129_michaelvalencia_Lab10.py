def protect_check_amount(amount):
    # Convert amount to string
    amount_str = str(amount)
    
    # how many number of characters including the decimal point
    num_chars = len(amount_str)
    
    # how many number of spaces needed for the check amount
    num_spaces = 10 - num_chars
    
    # does the amount have fewer characters than 10, add asterisks as leading characters
    if num_spaces > 0:
        protected_amount = '*' * num_spaces + amount_str
    else:
        protected_amount = amount_str
    
    return protected_amount

# Input the unknown dollar amount
dollar_amount = float(input("Enter the dollar amount: "))

# this is going to be the printed protected amount being displayed
print("Protected amount:", protect_check_amount(dollar_amount))
