file=open('polarityclass.txt')
line=file.readline()
count=pp=pn=po=pcount=0
tp=0.0
fp=0.0
n = 0
ponepos=batpos=scrpos=campos=pricpos=wipos=0
poneneg=batneg=scrneg=camneg=pricneg=wineg=0

with open('sentencestest9.txt') as infp:
    for dd in infp:
       if dd.strip():
          n+= 1

print 'number of non-blank lines found %d' % n

while line != '':
	count+=1;	
	polarity=line.split()[0]
	featur=line.split()[1]

	if featur == "phone:":
		if polarity == "positive":
			pp+=1;
			ponepos+=1
		elif polarity == "negative":
			pn+=1;
			poneneg+=1
		elif polarity == "not_an_opinion":
			po+=1;
		pcount+=1;
	if featur == "camera:":
		if polarity == "positive":
			pp+=1;
			campos+=1
		elif polarity == "negative":
			pn+=1;
			camneg+=1
		elif polarity == "not_an_opinion":
			po+=1;
		pcount+=1;
	if featur == "screen:":
		if polarity == "positive":
			pp+=1;
			scrpos+=1
		elif polarity == "negative":
			pn+=1;
			scrneg+=1
		elif polarity == "not_an_opinion":
			po+=1;
		pcount+=1;
	if featur == "price:":
		if polarity == "positive":
			pp+=1;
			pricpos+=1
		elif polarity == "negative":
			pn+=1;
			pricneg+=1
		elif polarity == "not_an_opinion":
			po+=1;
		pcount+=1;
	if featur == "battery:":
		if polarity == "positive":
			pp+=1;
			batpos+=1
		elif polarity == "negative":
			pn+=1;
			batneg+=1
		elif polarity == "not_an_opinion":
			po+=1;
		pcount+=1;
	if featur == "wifi:":
		if polarity == "positive":
			pp+=1;
			wipos+=1
		elif polarity == "negative":
			pn+=1;
			wineg+=1
		elif polarity == "not_an_opinion":
			po+=1;
		pcount+=1;

	line=file.readline()
	line=file.readline()
tp=pp+pn
fp=po
k1=tp+fp
ns=po+tp
fn=n-ns
k= float(tp*100)/k1
rec=tp*100/(tp+n-pcount)

print '\n\n'
print 'Feature			Feature polarity'
print '				pos	neg\n'
print 'phone			','	',ponepos,'	',poneneg 
print 'battery			','	',batpos,'	',batneg 
print 'Screen			','	',scrpos,'	',scrneg 
print 'Camera			','	',campos,'	',camneg 
print 'Price			','	',pricpos,'	',pricneg 
print 'Wifi			','	',wipos,'	',wineg 
print '\nPRECISION is %f percent' % k
print '\nRECALL is %f percent\n' % rec
		
