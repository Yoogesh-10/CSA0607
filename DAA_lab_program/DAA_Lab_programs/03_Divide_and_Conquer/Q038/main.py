# DAA Assignment - Question 38
# Topic: Divide and Conquer
# Algorithm: Karatsuba conceptual multiplication
# Time complexity: O(n^1.585)

def karatsuba(x,y):
 if x<10 or y<10:return x*y
 n=max(len(str(x)),len(str(y))); m=n//2
 a,b=divmod(x,10**m);c,d=divmod(y,10**m)
 ac=karatsuba(a,c);bd=karatsuba(b,d);adbc=karatsuba(a+b,c+d)-ac-bd
 return ac*10**(2*m)+adbc*10**m+bd
print("Product:",karatsuba(1234,5678))
