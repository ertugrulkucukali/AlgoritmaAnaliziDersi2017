s=0
def pow_log_n(x,n):
    """karmaşıklık = log n"""
    global s
    if(n==0):
        s=s+1
        return 1
    elif(n==1):
        s=s+1
        return x
    elif(n%2==0):
        s=s+1
        return pow(x*x,int(n/2))
    else:
        s=s+1
        return pow(x*x,int(n/2))*x


pow_log_n(2,60),s
