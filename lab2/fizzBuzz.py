def checkNumber(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz";
    if number % 3 == 0:
        return "Fizz";
    if number % 5 == 0:
        return "Buzz";
    return "Bad Number";


print(checkNumber(15));
print(checkNumber(5));
print(checkNumber(9));