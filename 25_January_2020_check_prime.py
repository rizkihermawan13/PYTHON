def check_prime(num):
    if num < 1:
        return -1
    else:
        for i in range(2, num//2+1):
            if num%i == 0:
                return 0
        return 1
 
def print_list(l):
    prime = []
    composite = []
    result = []
    for i in l:
        if check_prime(i)==1:
            prime.append(i)
        elif(check_prime(i)==0):
            composite.append(i)
    result.append(prime)
    result.append(composite)
    return result
 
if __name__ == "__main__":
    count = int(input())
    l = list(map(int, input().split()))
    print(check_prime(l[1]))
    print(print_list(l))
