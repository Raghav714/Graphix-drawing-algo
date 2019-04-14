def pointDDA(x1,y1,x2,y2):
	cor = []
	x,y = x1,y1
	cor.append((x1,y1))
	m = 1.0*(y2-y1)/(x2-x1)
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	if m <1:
		for i in range(length):
			cor.append((x+1,round(y+m)))
			x = x+1
			y = y+m
	elif m>1:
		for i in range(length):
			cor.append((round(x+1/m),y+1))
			x = x+1/m
			y = y+1
	else:
		for i in range(length):
			cor.append((x+1,y+1))
			x = x+1
			y = y+1
	return cor

def pointbres (x0, y0, x1, y1):
	cor = []
	dx = abs(x1-x0)
	dy = abs(y1-y0)
	if x0 < x1:
		sx = 1
	else:
		sx = -1
	if y0 < y1:
		sy = 1
	else:
		sy = -1
	err = dx-dy
	while True:
		cor.append((x0, y0))
		if x0 == x1 and y0 == y1:
			return cor
		e2 = 2*err
		if e2 > -dy:
			err = err - dy
			x0 = x0 + sx
		if e2 < dx:
			err = err + dx
			y0 = y0 + sy
def circleMidpoint(xcenter,ycenter,radius):
	x=0
	y=radius
	p=1 - radius
	cor = []
	cor = circlePlotpoints(cor,xcenter,ycenter,x,y)
	while x < y:
		x+=1
		if p<0:
			p=p+2*x+1
		else:
			y-=1
			p= p+ 2*(x-y) + 1
		cor = circlePlotpoints(cor,xcenter,ycenter,x,y)
	return set(cor)

def circlePlotpoints(cor, xcenter,ycenter,x,y):
	cor.append((xcenter + x , ycenter + y))
	cor.append((xcenter + x , ycenter - y))
	cor.append((xcenter - x , ycenter + y))
	cor.append((xcenter - x , ycenter - y))
	cor.append((xcenter + y , ycenter + x))
	cor.append((xcenter + y , ycenter - x))
	cor.append((xcenter - y , ycenter + x))
	cor.append((xcenter - y , ycenter - x))
	return cor

def ROUND(a):
	return int(a+0.5)
def ellipseMidpoint(xcenter,ycenter,rx,ry):
	cor = []
	x=0
	y=ry
	px=0
	py=2*y*rx*rx
	p=ROUND(ry*ry- (rx*rx*ry) + (0.25*rx*rx))
	while px < py:
		x+=1
		px+=2*ry*ry
		if p < 0:
			p +=ry*ry+px
		else:
			y-=1
			py -= 2*rx*rx
			p+=ry*ry+px-py
		cor = ellipsePlotpoint(cor,xcenter,ycenter,x,y)

	p= ROUND(ry*ry*(x+0.5)*(x+0.5)+rx*rx*(y-1)*(y-1) - rx*rx*ry*ry)
	while y > 0:
		y=y-1
		py-=2*rx*rx
		if p>0:
			p +=rx*rx - py
		else:
			x=x+1
			px+=2*ry*ry
			p+=rx*rx+px-py
		cor = ellipsePlotpoint(cor,xcenter,ycenter,x,y)
	return set(cor)	

def ellipsePlotpoint(cor, xcenter,ycenter,x,y):
	cor.append((xcenter + x , ycenter + y))
	cor.append((xcenter + x , ycenter - y))
	cor.append((xcenter - x , ycenter + y))
	cor.append((xcenter - x , ycenter - y))
	return cor

'''print "dda",pointDDA(4,5,12,13)
print "bes",pointbres(4,5,12,13)
print "circle",circleMidpoint(0,0,4)
print "ellipse",ellipseMidpoint(0,0,4,9)'''
