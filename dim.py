A = [-1, -10]
B = [5, -5]
C = [1, 1]
D = [-2, 3]

def dim(P):

    if P[0] > 0:
        if P[1] > 0:
            return "is First Quadrant"
        else:
            return "is Fourth Quadrant"
    else:
        if P[1] > 0:
            return "is Second Quadrant"
        else:
            return "is Third Quadrant"


print("A",str(A),dim(A))
print("B",str(B),dim(B))
print("C",str(C),dim(C))
print("D",str(D),dim(D))