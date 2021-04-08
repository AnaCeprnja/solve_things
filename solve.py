def leftRotateByOne(A):
 
    first = A[0]
    for i in range(len(A) - 1):
        A[i] = A[i + 1]
 
    A[-1] = first
 
 
# Function to left-rotate a list by `r` positions
def leftRotate(A, r):
 
    for i in range(r):
        leftRotateByOne(A)
 
 
if __name__ == '__main__':

    A = [1, 2, 3, 4, 5] #my  array
    r = 4 # the amount of times it will rotate 
 
    leftRotate(A, r)
    print(A)

    ##########
def array_left_rotation(a, n, k):
    a = list(a)
    return a[k:] + a[:k]

n, k = map(int, input().strip().split(' '))
a = map(int, input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
