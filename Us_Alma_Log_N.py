def pow_log_n(x,n):
    """karmaşıklık = log n"""
    
    if(n==0):
        return 1
    elif(n==1):
        return x
    elif(n%2==0):
        
        return pow(x*x,int(n/2))
    else:
       
        return pow(x*x,int(n/2))*x
        


pow_log_n(2,60)
