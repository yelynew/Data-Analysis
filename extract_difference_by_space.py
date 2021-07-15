import io
import re
import pandas as pd

df = pd.read_excel('your address')
comment=df['comment']
print(type(comment))
comment.head()
token=df['token']
token.head()

comments=[]
for i in comment:
  i=str(i)
  i = re.sub("\[|\]|\n'","",i) # 공백기준 구분
  i=i.split()
  comments.append(i)
print(comments)

tokens=[]
for j in token:
  j=str(j)
  j = re.sub("\[|\]|\'| ","",j)
  #print(j)
  ntokenj = j.split(",")
  #print(ntokenj)
  tokens.append(ntokenj)
print(tokens)

match1=[]
match2=[]
for x in range(len(comments)):
    y=comments[x]
    z=tokens[x]
    #겹치는 것들 목록
    for k in y:
      for l in z:
        if (l in k):
          match1.append(k)
          match2.append(l)

print(match1)
print(match2)

import pandas as pd
import numpy as np

#df=pd.DataFrame.from_records(match1, match2)

data={ 'comment' : match1, 'tag' : match2}
data= pd.DataFrame(data)
data.to_excel(excel_writer='match2.xlsx')

