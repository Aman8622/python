def reverse_digits(num):
    rev=0
    while(num>0):
        last_digit=num%10
        rev*=10
        rev+=last_digit
        num//=10
    return rev

def check_palindrome(num):
    rev = reverse_digits(num)
    if rev==num:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

def main():
    n = int(input("Enter a number: "))
    check_palindrome(n)

if __name__ == "__main__":
    main()

# While loop depends on num = num//10.

# Time complexity = O(log10(n))
# Space complexity = O(1)