import sys

src = sys.argv[1]
dst = sys.argv[2]

srcf = open(src,'r')
contents = srcf.read()
srcf.close()

contents = contents.replace("\t", ""*4)
dstf = open(dst,'w')
dstf.write(contents)
dstf.close()