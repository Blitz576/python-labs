def checkNumber():
    sum = 0
    cnt = 0
    while True:
        number = input("Enter a number: ")
        if not number.isnumeric():
          if number =="done":
             break;
          else:
            print("Invalid please try again....")
            continue;
        else:
            sum += int(number)
            # sum += number
            cnt +=1

    return [sum , (sum / cnt)];


print(checkNumber());