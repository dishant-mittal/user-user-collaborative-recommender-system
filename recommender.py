import csv
import numpy as np
import pandas as pd
def recommend(user):
	cr=csv.reader(open("similarity.csv","rb"))
#initializations begin
	problemlist=[]
	for row in cr:
   		problemlist.append(row)

	numusers= len(problemlist)
	numproblems= len(problemlist[1])
	print "%d ,%d" % (numproblems,numusers)
	similarity=[[0 for i in range(numusers)] for j in range(numusers)]
	similarity3=[[0 for i in range(numusers-1)] for j in range(numusers-1)]
	listy = [[]]*numusers
	similarity1= [];
	for i in xrange(0,numusers):	
	    similarity1.append(0);

	x=[]
	for i in xrange(0,numusers-1):
	    x.append(0);

	similarity3=[[0 for i in range(numproblems)] for j in range(numusers)]
	prediction=[[0 for i in range(numproblems)] for j in range(numusers)]

	final = [[]]*numproblems
	finaltemp=[[0 for i in range(numproblems-1)] for j in range(numusers-1)]
#initializations end
	avg=0
	count=0
	for i in range(1,numusers):	
	  		for j in range(1,numproblems):
				if problemlist[i][j]!= '':		
					count=count+1
					avg=avg+float(problemlist[i][j])
			avg=avg/count
			problemlist[i].append(avg)
        	        problemlist[i].append(count)
		#print problemlist[i]
			avg=0
			count=0
#avg done
	for i in range(1,numusers):
		for k in range(1,numproblems+2):
			if problemlist[i][k]!= '':
				problemlist[i][k]=float(problemlist[i][k])
				
	for i in range(1,numusers):	
			for k in range(1,numproblems):
				if (problemlist[i][k]!=''):
					similarity1[i]=similarity1[i]+(problemlist[i][k]-problemlist[i][numproblems])**2
			similarity1[i]=(similarity1[i])**(0.5)
	for i in range(1,numusers):	
		for j in range(1,numusers):         	
			similarity3[i][j]=similarity1[i]*similarity1[j]		
		print
	for i in range(1,numusers):
		for j in range(1,numusers): 
			if (similarity3[i][j]!= 0.0 or similarity3[i][j]!= 0):        				
				for k in range(1,numproblems):
					if (problemlist[i][k]!='' and problemlist[j][k]!=''):
						similarity[i][j]=similarity[i][j]+(problemlist[i][k]-problemlist[i][numproblems])*(problemlist[j][k]-problemlist[j][numproblems])
				similarity[i][j]=similarity[i][j]/similarity3[i][j]
				listy[i].append(similarity[i][j])
			else:
				listy[i].append(0)
	temp=zip(*[iter(listy[1])]*(numusers-1))	
	
	for i in range(0,numusers-1):	
		for j in range(0,numusers-1):         		
			if i!=j:
				x[i]=x[i]+abs(temp[i][j])	
		

	for i in range(1,numusers):	
		for k in range(1,numproblems):         		
			for j in range(1,numusers): 
				if i!=j:
					if problemlist[i][k]=='':							        			
						if problemlist[j][k]!= '':
							prediction[i][k]=prediction[i][k]+problemlist[j][k]*(temp[i-1][j-1])
					else:
						prediction[i][k]=0	
				prediction[i][k]=(prediction[i][k])/x[j-1]
			
	recommend=[]
	recommendlist=[]
	print "unsorted is"
	for i in range(1,numproblems):
		recommend.append(prediction[user][i])
	print prediction[user]
	recommend.sort()
	recommend=recommend[::-1]
	new=[]
	for i in range(1,numproblems):
		new.append(prediction[user][i])
	for i in range(0,4):		
		for j in range(1,numproblems):
			if(recommend[i] is new[j]):
				recommendlist.append(j)					
				break
	print "problem ids are"
	print recommendlist
	return recommendlist
recommend(11)
	
	

	
	


   		




           


































