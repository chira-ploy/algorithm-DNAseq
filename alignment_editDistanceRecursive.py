#!usr/bin/env python

def editDistanceRecursive(x, y):
    
    # This implementation is very slow
    if len(x) == 0:
        return len(y)
    elif len(y) == 0:
        return len(x)
    else:
        distHor = editDistanceRecursive(x[:-1], y) + 1
        distVer = editDistanceRecursive(x, y[:-1]) + 1
        if x[-1] == y[-1]:
            distDiag = editDistanceRecursive(x[:-1], y[:-1])
        else:
            distDiag = editDistanceRecursive(x[:-1], y[:-1]) + 1

        return min(distHor, distVer, distDiag)
