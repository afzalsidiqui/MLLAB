import numpy as np
import pandas as pd
data=pd.read_csv('finds.csv')
print('Data',data)
def train (concepts,target):
    specific_h=concepts[0]
    print('specific1',specific_h)
    for i,h in enumerate(concepts):
        print('i',i)
        print('h',h)
        if target[i]=="Yes":
            for x in range(len(specific_h)):
                print('x',x)
                print('specific',specific_h)
                if h[x]==specific_h[x]:
                    pass
                else:
                    specific_h[x]="?"
    return specific_h
concepts=np.array(data.iloc[:,0:-1])
target=np.array(data.iloc[:,-1])
print('Concept',concepts)
print('Target',target)
print(train(concepts,target))

