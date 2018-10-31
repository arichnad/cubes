#!/usr/bin/python3

b=[
'ooo-------',
'oSoooo----',
'ooooooooo-',
'-ooooooooo',
'-----ooToo',
'------ooo-',
]
#b=['o'*550]*550
#b[0]='S'+b[0][1:-1]+'T'
#b[0]='S'+b[0][1:]
#b[-1]=b[-1][:-1]+'T'
#s=set()

b=['TooS'];s=set()
#breadth first search, please
def a(w,m,n):
	x,y,i,j=w
	if w in s or not(0<=x<len(b[0])-i and 0<=y<len(b)-j)or b[y][x]=='-' or b[y+j][x+i]=='-':return
	#print('---')
	m=m+[n];s.add(w);q.append((w,m))
	if w==e:print(m);return True
for y,r in enumerate(b):
	if r.find('S')+1:q=[((r.find('S'),y,0,0),[])]
	if r.find('T')+1:e=(r.find('T'),y,0,0)
while q:
	(x,y,i,j),m=q.pop(0);k=1-i-j
	if a((x+i+1,y,k,j),m,'r') or a((x-k-1,y,k,j),m,'l') or a((x,y+j+1,i,k),m,'d') or a((x,y-k-1,i,k),m,'u'):q=0

