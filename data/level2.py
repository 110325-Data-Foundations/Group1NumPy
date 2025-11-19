def notInArray(A, K):

    # Write your logic here
    A.sort()
    result=0
    check=K+1
    for x in A:
        if x==check:
            result=check+1
            check+=1
        elif check==K+1:
            result=K+1
    return result
if __name__ == "__main__":
    N = int(input()) 
    A = [int(input()) for i in range(N)][:N]  
    K = int(input()) 
    result = notInArray(A, K)
    print(result)