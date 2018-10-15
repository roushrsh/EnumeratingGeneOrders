##partial Permuations Rosalind 
##http://rosalind.info/problems/pper/
n = 82
k = 10
number = 1

for x in range (0, k):
    number = number * n
    n = n-1
print number % 1000000
