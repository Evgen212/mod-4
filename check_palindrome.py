def func(a,n):
    if a%n == 0:   
    
        print(f"{n} - является делителем числа {a}")
    else:
        print(f"{n} - не является делителем числа {a}")
    
        

func(40,4)
##
##print("-----")
##
##def lec(n):
##
##    for i in range(n,0,-1):
##        print("*"*i)
##   
##    
##
##lec(3)
##print("------")
##
##
##def pow_func(base, n=2):
##    inside_result = base ** n
##    #print(base ** n)
##    return inside_result
##
###print()
##
##r = pow_func(3,3)
##print(r)
##print("____")
##    
##    
##def bobo(a):
##    sch = 0    
##    for i in range(1,a+1):        
##        if a % i == 0:
##            sch+=1
##    return sch
##   
##
##print(bobo(6))
print("-------")
#@def check_palindrome(str_)
##def check_palindrome(str_):
##   str_ = str_.lower()
##   str_ = str_.replace(" ", "")
##
##   if str_ == str_[::-1]:
##       return True
##   else:
##       return False    
##print(check_palindrome("22222"))

def s():
    
    global a
    a = 45
    print(a, "local")
    


    
a = 10,5

s()
print(a, "global")


x = 3
def function():
    print(x)
    return x

print(function())


