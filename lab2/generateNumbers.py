def generate(len,start):
    numbers=[];
    for i in range(start,(start+len)):
        numbers.append(i);
    return numbers

print(generate(5,5));