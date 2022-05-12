import sys

for line in sys.stdin:
	xs = list(map(float, line.strip().split()))
	a = sum(xs)/len(xs)
	print(round(a,4))
