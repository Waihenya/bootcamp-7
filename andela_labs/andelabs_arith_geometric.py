def ari_geo(A):

    length = len(A)

    for i in range(1, length+1):

        if A[i+1] - A[i] == A[i+2] - A[i+3]:

            return "arithmetic"

        elif A[i+1] / A[i] == A[i+2] / A[i+1]:
            return "geometric"

        elif A == None:
            return 0

        else:
            return -1

print ari_geo([2,4,6,8,10])