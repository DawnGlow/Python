# EX06_05 탭 to 공백 4개
import sys

src = sys.arvg[1]
dst = sys.argv[2]

f = open(src)
origin = f.read()
f.close()

modi = origin.replace("\t", " "*4)
f = open(dst, 'w')
f.write(modi)
f.close()