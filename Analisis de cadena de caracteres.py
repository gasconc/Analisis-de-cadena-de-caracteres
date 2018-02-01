phrase='bob'
count=0
c=0
for x in range(len(s)):
    count+=1
    if count < len(s)-1:
        if (s[x]+s[x+1]+s[x+2])== phrase:
            c+=1
print('Number of times bob occurs is:'+ str(c))
   