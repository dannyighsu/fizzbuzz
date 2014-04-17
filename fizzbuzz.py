""" Prints numbers 1 to 100. For multiples of 3, prints "Fizz"; for multiples of
5, prints "Buzz"; for multiples of 5 and 3, prints "FizzBuzz". """

def main(argv=None):
    buzz = "Buzz"
    fizz = "Fizz"
    fizzbuzz = "FizzBuzz"
    for i in range(1, 101):
        if i % 15 == 0:
            print(fizzbuzz)
        elif i % 3 == 0:
            print(fizz)
        elif i % 5 == 0:
            print(buzz)
        else:
            print(i)

if __name__ == "__main__":
    main()
