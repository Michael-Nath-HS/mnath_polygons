import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

# Return the dot product of a . b
def dot_product(a, b):
    if len(a) != len(b):
        return None
    ans = 0
    for i in range(len(a)):
        ans += (a[i] * b[i])
    return ans

def cross_product(a, b):
    # assumes both vectors are 3 * 1
    return [(a[1]*b[2]) - (a[2]*b[1]), (a[2]*b[0]) - (a[0]*b[2]), (a[0]*b[1]) - (a[1]*b[0])]  

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    vector_a = [
        polygons[i+1][0] - polygons[i][0], 
        polygons[i+1][1] - polygons[i][1], 
        polygons[i+1][2] - polygons[i][2]
        ]
    vector_b = [
        polygons[i+2][0] - polygons[i][0], 
        polygons[i+2][1] - polygons[i][1], 
        polygons[i+2][2] - polygons[i][2]
        ]
    return cross_product(vector_a, vector_b)