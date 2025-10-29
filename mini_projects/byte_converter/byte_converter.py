"""
    Converts a file size in bytes to the appropriate unit
    (KB, MB, GB, TB, PB, EB, ZB, YB) based on its magnitude.
    
"""

def byte_converter(number : int):

    if number < 0 :
        show_negative_number = f"{number} is negative try again!"
        return show_negative_number 

    elif number < 10**3:
        return str(number) + "B"
        
    elif 10**3 <= number < 10**6:
        return str(number / 10**3) + "KB" 

    elif 10**6 <= number < 10**9:
        return str(number / 10**6) + "MB" 

    elif 10**9 <= number < 10**12:
        return str(number / 10**9) + "GB"

    elif 10**12 <= number < 10**15:
        return str(number / 10**12) + "TB"

    elif 10**15 <= number < 10**18:
        return str(number / 10**15) + "PB"

    elif 10**18 <= number < 10**21:
        return str(number / 10**18) + "EB"

    elif 10**21 <= number < 10**24:
        return str(number / 10**21) + "ZB"

    elif number >= 10**24:
        return str(number / 10**24) + "YB"

    else:
        return str(number) + ">= YB"



while True :
    user_number = int(input("Enter your number :: "))
    print(byte_converter(user_number))
    continue_or_not = input("yes or no :: ")
    if continue_or_not.strip().lower() == "yes" :
        continue
    else :
        break
    
