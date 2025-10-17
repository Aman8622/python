def count_digits(num):
    count = 0

    while(num>0):
        last_digit=num%10
        count+=1
        num//=10
    
    return count


def main():
    n = int(input("Enter a number: "))
    count = count_digits(n)
    print(f"number of digits in {n} = " + str(count))

if __name__ == "__main__":
    main()

# While loop depends on num = num//10.

# Time complexity = O(log10(n))
# Space complexity = O(1)