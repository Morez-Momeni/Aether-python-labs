"""
    Converts a file size in bytes to the appropriate unit
    (KB, MB, GB, TB, PB, EB, ZB, YB) based on its magnitude.
    
"""



def byte_converter(number : int):

    if number < 10**3:
        print(number, "B")
        
    elif 10**3 <= number < 10**6:
        print(number / 10**3, "KB")

    elif 10**6 <= number < 10**9:
        print(number / 10**6, "MB")

    elif 10**9 <= number < 10**12:
        print(number / 10**9, "GB")

    elif 10**12 <= number < 10**15:
        print(number / 10**12, "TB")

    elif 10**15 <= number < 10**18:
        print(number / 10**15, "PB")

    elif 10**18 <= number < 10**21:
        print(number / 10**18, "EB")

    elif 10**21 <= number < 10**24:
        print(number / 10**21, "ZB")

    elif number >= 10**24:
        print(number / 10**24, "YB")

    else:
        print(number,">= YB")

byte_converter()