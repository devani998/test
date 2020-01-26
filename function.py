def baby_Trouble(a_smile, b_smile):
    """
    parameters 
    - a_smile datatype in boolean
    - b_smile datatype in boolean

    return 
    data type is in boolean
    true - Smiling
    False - Smiling
    """
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    else:
        return False


def int_sum(a, b):
    if a==b:
        return (a+b)*2
    else:
       return (a+b)

if __name__ == '__main__':
    # val = baby_Trouble(True,False)
    # print(val)
        var= int_sum(3,3)
        print(var)




