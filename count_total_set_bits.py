import math

def CountBits(n):
    l=int(math.log(n,2)//1)
    ans=l* (1<<(l-1))
    #print(ans)
    for i in range(l):
        ans+=(1<<i)*((n - (1<<l) + 1)//(1<<(i+1)))
        #print(1, ans)
        if (((n - (1<<l) + 1)%(1<<(i+1)))-(1<<i))>0:
            ans+= (((n - (1<<l)+1)%(1<<(i+1)))-(1<<i))
            #print(2,ans)
    ans+=(n - (1<<l) +1)
    return ans
