
# coding: utf-8

# In[1]:


def ShortestSuperSeq(X,Y):
    print (X,Y)
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 2) for i in range(m + 2)] 
    for i in range(m + 1):
        for j in range(n+1):
            if(i==0):
                dp[i][j]=j
            elif(j==0):
                dp[i][j]=i
            elif(X[i-1]==Y[j-1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    index = dp[m][n]
    strng= ""
    i,j=m,n
    while(i>0 and j>0):
        if (X[i-1]==Y[j-1]):
            strng = strng + (X[i-1])
            i,j,index=i-1,j-1,index-1
        elif (dp[i-1][j]>dp[i][j-1]):
            strng = strng + (Y[j-1])
            j,index=j-1,index-1
        else:
            strng = strng + (X[i-1])
            i,index=i-1,index-1
    while(i>0):
        strng = strng + (X[i-1])
        i,index=i-1,index-1
    while(j>0):
        strng = strng + (Y[j-1])
        j,index=j-1,index-1
    print (strng[::-1])


# In[5]:


ShortestSuperSeq("GTCAGTATCGCCGCCTCCACTAACCCGTAGGGACCTTGTACAGGAACAGCGCGTTGCTTACTAGTAGTAATGGGCACATTTAGTAACGCTT",
                 "TGCAAACACTACATACCTTTCAAACCTACCCGCTTCTGTGTGTGTTATCGATATTAGGTACGAGTGGGATGAGCTGGATTAAATCTTATCGAAACTCTCG")

