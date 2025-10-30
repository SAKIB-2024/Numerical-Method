# solve f(x)=x^2-2 , [1,2] upto 7 iteration

f= lambda x: x**2-2
a=1
b=2
true=2**(1/2)
iter=1
while iter<=7:
    c=(a+b)/2
    #c=(a*f(b)-b*f(a))/(f(b)-f(a))
    err=abs(true-c)
    print(f"Iteration: {iter}  approx root: {c}  error={err}")
    if f(c)<0:
        a=c
    else:
        b=c
    iter=iter+1
