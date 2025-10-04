#rotate number of times 90*
#[[1,2,3],[4,5,6],[7,8,9]]
#[[7,4,1],[8,5,2],[9,6,3]]

def rotate(matrix, n):
    w = 0
    while(w < n):
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
        w+=1
  
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]], 1))

def factors(n):
    if n == 0:
        return [1]  
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

perfect_squares_factors = []

for i in range(11):  
    square = i * i
    perfect_squares_factors.append([square] + factors(square))

for entry in perfect_squares_factors:
    print(entry)

from math import gcd, lcm

class Solution:
    def maxLength(self, nums):
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            current_gcd = nums[i]
            current_lcm = nums[i]
            current_prod = nums[i]
            
            for j in range(i, n):
                if j > i:
                    current_gcd = gcd(current_gcd, nums[j])
                    current_lcm = lcm(current_lcm, nums[j])
                    current_prod *= nums[j]
                
                if current_prod == current_gcd * current_lcm:
                    max_len = max(max_len, j - i + 1)
        
        return max_len