def extract_digits(num):
    num_list = []
    while(num>0):
        last_digit=num%10
        num_list.append(last_digit)
        num//=10
    return num_list

def check_armstrong(num):
    num_list=extract_digits(num)
    sum=0
    for i in num_list:
        sum+=pow(i,len(num_list))
    if sum == num:
        print(f"{num} is a armstrong number.")
    else:
        print(f"{num} is not an armstrong number.")

def main():
    n = int(input("Enter a number: "))
    check_armstrong(n)

if __name__ == "__main__":
    main()
    
# While loop depends on num = num//10.

# Time complexity = O(log10(n))
# Space complexity = O(1)