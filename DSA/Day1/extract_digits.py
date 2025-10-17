def extract_digits(num):
    while(num>0):
        last_digit=num%10
        print(last_digit)
        num//=10

def main():
    n = int(input("Enter a number: "))
    extract_digits(n)

if __name__ == "__main__":
    main()

# While loop depends on num = num//10.

# Time complexity = O(log10(n))
# Space complexity = O(1)