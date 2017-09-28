
import os
import wget

def foerste(nr, start, stop):
	ii=0
	jj=0

	for i in range(start,stop):
		for j in range(i+1,stop):
			url = "http://www.npd.no/engelsk/cwi/pbl/core_photo_jpgs/2288_" + str(nr).zfill(2) + "_" + str(i) + "-" + str(j) +"m.jpg"
		
			f = wget.download(url)
			print f
			b = os.path.getsize(f)
			print b
			if b==0:
				os.remove(f)
			else:
				ii=i
				jj=j
				return ii, jj 

ii, jj = foerste(1,2020,2040)

print ii, jj

for i in range(2,9):
	ii, jj = foerste(i,jj,jj+20)
