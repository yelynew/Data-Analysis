
import io
import re
import pandas as pd
import platform


df = pd.read_excel('your address')
comment=df['comment']
print(type(comment))
comment.head()
token=df['token']
token.head()

import konlpy.tag
comments=[]
for i in comment:
  i=str(i)
  i = re.sub("\[|\]|\n'","",i)
  i=i.split()
  comments.append(i)
  Okt = konlpy.tag.Okt()
  Okt_morphs = Okt.pos(i)  # 튜플반환
  print(Okt_morphs)
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

data={ 'comment' : match1, 'tag' : match2}
data= pd.DataFrame(data)
data.to_excel(excel_writer='match3.xlsx')
