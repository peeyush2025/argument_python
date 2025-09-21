# define function to caluculate cube
def cube(number):
    return number*number*number
# define a function which will execute cube function if the user enter the number is divisble by 3
def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
# disply result
print(by_three(9))
print(by_three(4))