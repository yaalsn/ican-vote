from PIL import Image
def tobw(im):
	im = im.convert('RGBA')
	(w, h) = im.size
	for x in xrange(w):
		for y in xrange(h):
			pos = (x,y)
			rgb = im.getpixel(pos)
			(r,g,b,a) = rgb
			if r>139 and g<26 and b<42 and (x>0 and x<70):
				im.putpixel(pos,(255,255,255))
			else:
				im.putpixel(pos,(0,0,0))
	return im
		
