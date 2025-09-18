#sys
import sys
#sys.argv
'''print("hello my name is ",sys.argv[1])

print("hello my name is ",sys.argv[0])'''

#sys.exit

if len(sys.argv) < 2:
    sys.exit("Too small arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    print("hello my name is ",sys.argv[1])
