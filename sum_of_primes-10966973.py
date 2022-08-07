#This is a Python code which takes the sum of prime numbers less than a given number.
#The first line of code accepts input from the user.
num = int(input("Enter your number here: \n"))
prime_sum = 0
#The variable prime_sum is set to 0 in order to accumulate the sum of results after a successful loop is True
for i in range(2, num + 1):
    prime = True
#The range closes at (i//2 + 1). This is to ensure that the compiler doesnt take long to produce our result.
    for j in range(2, i//2 + 1):
        if i % j == 0:
            prime = False
            break
#The loop breaks and proceeds to the next number whenever it identifies a number which isn't prime.
    if prime:
        prime_sum += i
print(f"The sum of prime numbers less than {num} is: \n{prime_sum}")
