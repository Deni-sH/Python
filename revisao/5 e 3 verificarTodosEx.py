def fizzbuzz(num):
    for n in range(1, num+1):
        
        if(n % 3 == 0 and n % 5 != 0):
            print("Fizz")
        elif(n % 5 == 0 and n % 3 != 0):
            print("Buzz")
        elif(n % 5 == 0 and n % 3 == 0):
            print("FizzBuzz")
        else:
            print(n)
            




n = int(input("Digite um número"))
fizzbuzz(n)
     
