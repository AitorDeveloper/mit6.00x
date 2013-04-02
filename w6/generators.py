myGenerator = (x*x for x in range(3))
#myGenerator = [x*x for x in range(3)]
for i in myGenerator:
    print i
for i in myGenerator:
    print i, 'second time'
