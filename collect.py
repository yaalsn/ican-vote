from PIL import Image

def to10(im,x1,y1,x2,y2):
	#im = Image.open(im)
	(w, h) = im.size
	traindata = ''
	for y in xrange(h):
		for x in xrange(w):
			if (x>=x1 and x<=x2) and (y>=y1 and y<=y2):
				pos = (x,y)
				rgb = im.getpixel(pos)
				if rgb == (255, 255, 255, 255):
					traindata += '1'
				else:
					traindata += '0'
	return str(traindata)
