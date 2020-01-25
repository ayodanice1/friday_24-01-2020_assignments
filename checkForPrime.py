
import math

def is_prime(num) :
    if num > 1 and num <= 3:
        return True
    elif num > 3 :
        sqrt_of_num = math.sqrt(num)
        # The square root of a prime number cannot be an integer, rather always a float
        if sqrt_of_num - math.trunc(sqrt_of_num) > 0 :
            for i in range(3, num) :
                if num % i == 0 :
                    return False
            return True
        else :
            return False
        pass
    else :
        return False


if __name__ == "__main__" :
    num = int(input("Enter your number here: "))
    check = is_prime(num)
    if check : print(num, " is a Prime number.")
    else : print(num, " is not a Prime number.")