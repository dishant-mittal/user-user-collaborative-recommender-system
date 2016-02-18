import pandas as pd
import numpy as np 
from sklearn import svm
from sklearn import linear_model

#data = np.genfromtxt(open('train.csv','rb'), delimiter=',')
data = pd.read_csv('train.csv')

m,n = data.shape
print m
data = np.array(data)

x_train = data[0:200000,0:3].astype(np.float)
x_test = data[200001:m,0:3].astype(np.float)

y_votes_train = data[0:200000,5].astype(np.int)
y_votes_test = data[200001:m,5].astype(np.int)

y_comments_train = data[0:200000,6].astype(np.int)
y_comments_test = data[200001:m,6].astype(np.int)

y_views_train = data[0:200000,7].astype(np.int)
y_views_test = data[200001:m,7].astype(np.int)

print x_train.shape
print x_test.shape

clf1 = linear_model.SGDClassifier(n_jobs = -1, penalty = 'l1')
clf1.fit(x_train,y_votes_train)
print clf1.score(x_test,y_votes_test)

clf2 = linear_model.SGDClassifier(n_jobs = -1, penalty = 'l1')
clf2.fit(x_train,y_comments_train)
print clf2.score(x_test,y_comments_test)

clf3 = linear_model.SGDClassifier(n_jobs = -1, penalty = 'l1')
clf3.fit(x_train,y_views_train)
print clf3.score(x_test,y_views_test)





