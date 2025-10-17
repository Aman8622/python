def reverse_digits(num):
    rev=0
    while(num>0):
        last_digit=num%10
        rev*=10
        rev+=last_digit
        num//=10
    return rev

def main():
    n = int(input("Enter a number: "))
    rev = reverse_digits(n)
    print(f"Reverse of {n} = " + str(rev))

if __name__ == "__main__":
    main()

# While loop depends on num = num//10.

# Time complexity = O(log10(n))
# Space complexity = O(1)