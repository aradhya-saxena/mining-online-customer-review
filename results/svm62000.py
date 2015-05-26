#polarity classification

file=open('featureclass12.txt')
line=file.readline()
f1=open('polarityclasssvm.txt','wb')
f2=open('positiveclustersvm.txt','wb')
f3=open('negativeclustersvm.txt','wb')
f4=open('NOopinion.txtsvm','wb')

pos=open('positive-words.txt')
neg=open('negative-words.txt')
f2.write("POSITIVE"+"\n")
f3.write("NEGATiVE"+"\n")
f4.write("GENERAL NO OPINION"+"\n")
flag=0
positive={}
negative={}
c=0
k=0
for i in pos.read().split():
	positive[i]=c
	c=c+1

for j in neg.read().split():
	negative[j]=k
	k=k+1
flag=0
while line!= '':
	flag=0
	for w in positive:
		if w in (line.lower()).split():
			f1.write("positive"+" "+str(line)+"\n")
			f2.write(str(line)+"\n")
			flag=1
					
	if flag==0:
		for l in negative:
			if l in (line.lower()).split():
				f1.write("negative"+" "+str(line)+"\n")
				f3.write(str(line)+"\n")
				flag=1
	if flag==0:
		f1.write("not_an_opinion"+" "+str(line)+"\n")
		f4.write(str(line)+"\n")
	line=file.readline()
	line=file.readline()

f1.close()
f2.close()
f3.close()
f4.close()
