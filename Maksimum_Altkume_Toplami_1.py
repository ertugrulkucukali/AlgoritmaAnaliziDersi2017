def maxSubSum1(myvector):
    maxSum=0
    for i in range(len(myvector)):
        thisSum=0
        for j in range(i,len(myvector)):
            for k in range (i,j):
                thisSum=thisSum+myarray[j]
                if (thisSum>maxSum):
                    maxSum=thisSum
    return maxSum


myarray=[4,-3,5,-2,-1,2,6,-2]
print(maxSubSum1(myarray))
