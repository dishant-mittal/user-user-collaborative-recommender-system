import pandas as pd
import numpy as np 
from sklearn import svm
from sklearn import linear_model
from sklearn import preprocessing

#data = np.genfromtxt(open('train.csv','rb'), delimiter=',')
data = pd.read_csv('train.csv',nrows=2000)

data = np.array(data)

m,n = data.shape

for i in range(0,data.shape[0]):
    if(pd.isnull(data[i,10])):
         data[i,10]=0.0
    if((data[:,10]=='abandoned_vehicle')[i]):
         data[i,10]=1.0
    if((data[:,10]=='abandoned_vehicles')[i]):
         data[i,10]=1.0
    if((data[:,10]=='animal_problem')[i]):
         data[i,10]=2.0
    if((data[:,10]=='bad_driving')[i]):
         data[i,10]=3.0
    if((data[:,10]=='bench')[i]):
         data[i,10]=4.0
    if((data[:,10]=='bike_concern')[i]):
         data[i,10]=5.0
    if((data[:,10]=='blighted_property')[i]):
         data[i,10]=6.0
    if((data[:,10]=='bridge')[i]):
         data[i,10]=7.0
    if((data[:,10]=='crosswalk')[i]):
         data[i,10]=8.0
    if((data[:,10]=='drain_problem')[i]):
         data[i,10]=9.0
    if((data[:,10]=='drug_dealing')[i]):
         data[i,10]=10.0
    if((data[:,10]=='flood')[i]):
         data[i,10]=11.0
    if((data[:,10]=='graffiti')[i]):
         data[i,10]=12.0
    if((data[:,10]=='heat')[i]):
         data[i,10]=13.0
    if((data[:,10]=='homeless')[i]):
         data[i,10]=14.0
    if((data[:,10]=='hydrant')[i]):
         data[i,10]=15.0
    if((data[:,10]=='illegal_idling')[i]):
         data[i,10]=16.0
    if((data[:,10]=='lost_and_found')[i]):
         data[i,10]=17.0
    if((data[:,10]=='noise_complaint')[i]):
         data[i,10]=18.0
    if((data[:,10]=='odor')[i]):
         data[i,10]=19.0
    if((data[:,10]=='other')[i]):
         data[i,10]=20.0
    if((data[:,10]=='overgrowth')[i]):
         data[i,10]=21.0
    if((data[:,10]=='parking_meter')[i]):
         data[i,10]=22.0
    if((data[:,10]=='pedestrian_light')[i]):
         data[i,10]=23.0
    if((data[:,10]=='pothole')[i]):
         data[i,10]=24.0
    if((data[:,10]=='prostitution')[i]):
         data[i,10]=25.0
    if((data[:,10]=='public_art')[i]):
         data[i,10]=26.0
    if((data[:,10]=='public_concern')[i]):
         data[i,10]=27.0
    if((data[:,10]=='road_safety')[i]):
         data[i,10]=28.0
    if((data[:,10]=='roadkill')[i]):
         data[i,10]=29.0
    if((data[:,10]=='robbery')[i]):
         data[i,10]=30.0
    if((data[:,10]=='rodents')[i]):
         data[i,10]=31.0
    if((data[:,10]=='sidewalk')[i]):
         data[i,10]=32.0
    if((data[:,10]=='signs')[i]):
         data[i,10]=33.0
    if((data[:,10]=='snow')[i]):
         data[i,10]=34.0
    if((data[:,10]=='street_light')[i]):
         data[i,10]=35.0
    if((data[:,10]=='street_signal')[i]):
         data[i,10]=36.0
    if((data[:,10]=='test')[i]):
         data[i,10]=37.0
    if((data[:,10]=='traffic')[i]):
         data[i,10]=38.0
    if((data[:,10]=='trash')[i]):
         data[i,10]=39.0
    if((data[:,10]=='tree')[i]):
         data[i,10]=40.0
    if((data[:,10]=='zoning')[i]):
         data[i,10]=41.0

tempest=np.array(data[:,3])
data[:,3]=data[:,10]
data[:,10]=tempest

X = data[:1600,1:4].astype(np.float)

X = preprocessing.scale(X)
#print X[:5,:]
x_train = X[:1400,:].astype(np.float)
x_test = X[1400:1600,:].astype(np.float)
print x_train
print x_test

#x_train = data[0:200000,0:3].astype(np.float)
#x_test = data[200001:m,0:3].astype(np.float)
#print x_train[:5,:]
#print x_test[:,:]

y_votes_train = data[:1400,5].astype(np.int)
y_votes_test = data[1400:1600,5].astype(np.int)


y_comments_train = data[:1400,6].astype(np.int)
y_comments_test = data[1400:1600,6].astype(np.int)

y_views_train = data[:1400,7].astype(np.int)
y_views_test = data[1400:1600,7].astype(np.int)

#print(y_comments_test[0:100])

#scaler = preprocessing.StandardScaler.fit(X)
#x_train = scaler.transform(x_train)
#x_scaled = preprocessing.scale(x_train)
#x_train = x_scaled

print x_train.shape
print x_test.shape

#clf1 = linear_model.SGDRegressor(penalty = 'l1', alpha = 0.01)
clf1 = linear_model.Lasso(alpha = 0.000001)
#clf1 = linear_model.Ridge(normalize = False, alpha = 0.01)
#clf1 = svm.SVR(kernel='linear')
clf1.fit(x_train,y_votes_train)
print clf1.score(x_test,y_votes_test)
votes= clf1.predict(x_test)

clf2 = linear_model.Lasso(alpha = 0.00001)
#clf2 = linear_model.SGDRegressor(penalty = 'l1', alpha = 0.01)
#clf2 = linear_model.Ridge(normalize = False, alpha = 0.01)
clf2.fit(x_train,y_comments_train)
print clf2.score(x_test,y_comments_test)
comments=clf2.predict(x_test)

clf3 = linear_model.Lasso(alpha = 0.001)
#clf3 = linear_model.SGDRegressor(penalty = 'l2')
clf3.fit(x_train,y_views_train)
print clf3.score(x_test,y_views_test)
views=clf2.predict(x_test)
#data_test = pd.read_csv('test.csv')
#data_test = np.array(data_test)


#clf4 = linear_model.SGDClassifier(n_jobs=-1, penalty = 'l1')


col=0.5*comments+0.3*votes+0.2*views
mx=max(col)
mn=min(col)
mu=np.mean(col)
norm=(col-mu)/(mx-mn)

data_test=np.c_[votes,comments]
data_test=np.c_[data_test,views]
data_test=np.c_[data_test,norm]

col=3
data_test=data_test[np.argsort(data_test[:,col])]







