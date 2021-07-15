import io
import re
import pandas as pd

df = pd.read_excel('your address')
tag=df['tags']
#print(type(tag))
tag.head()
token=df['token']
token.head()

tags=[]
for i in tag:
  i=str(i)
  i = re.sub("\[|\]|\'| ","",i)
  i = re.sub("\#",",",i)
  ntagi = i.split(",")
  tags.append(ntagi)
#print(tags)  
  #print(ntagi[0])

tokens=[]
for j in token:
  j=str(j)
  j = re.sub("\[|\]|\'| ","",j)
  #print(j)
  ntokenj = j.split(",")
  #print(ntokenj)
  tokens.append(ntokenj)
print(tokens)
diff1=[]
diff2=[]
for x in range(len(tags)):
    y=tags[x]
    z=tokens[x]
    y1=tags[x]
    z1=tokens[x]
    for k in y:
      for l in z:
        if (k==l):
          if (k in y1):
            y1.remove(k)
          if (l in z1):
            z1.remove(l)

    set1=set(y1)
    list1=list(set1)
    set2=set(z1)
    list2=list(set2)
    diff1.append(list1)
    diff2.append(list2)

    


#print(diff1)
#print(diff2)

import pandas as pd
import numpy as np

df=pd.DataFrame.from_records(diff1)
df.to_excel('diff3.xlsx')
df2=pd.DataFrame.from_records(diff2)
df2.to_excel('diff4.xlsx')

#중복제거
