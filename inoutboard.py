#usr/bin/python

import bluetooth
import time

line1 = "define"
line2 = "notdefine"
line3 = "yetanotherdefine"

def inoutprint (name, inout, line):
	status = "bogeyyyy"
	global line1
	global line2
	global line3
	if inout != None:
		print(name, " is in the house right now.")
		if line == 1:
			line1 = "%s is in the house right now." % name
		else:
			 if line == 2:
				line2 = "%s is in the house right now." % name
			 else:
				if line == 3:
					line3 = "%s is in the house right now." % name	
	else:
		print(name, " is not in the house right now.")
		if line == 1:
                        line1 = "%s is not in the house right now." % name
                else:
                         if line == 2:
                                line2 = "%s is not in the house right now." % name
                         else:
                                if line == 3:
					line3 = "%s is not in the house right now." % name 
	print (line1 + "hello")
	print (line2 + "hello2")
	print (line3 + "hello3")
	return
def filewrite ():
	global line1
	global line2
	global line3
	file = open("lol.html", "w")
        file.write("<!DOCTYPE html>" + "\n")
        file.write("<html>" + "\n")
        file.write("<head>" + "\n")
	file.write("""<META HTTP-EQUIV="refresh" CONTENT="15">""")
	file.write("\n")
	file.write("</head>" + "\n")
	file.write("<body>" + "\n")
        file.write("<p>" + line1 + "</p>" + "\n")
	file.write("<p>" + line2 + "</p>" + "\n")
	file.write("<p>" + line3 + "</p>" + "\n")
        file.write("</body>" + "\n" + "</html>")
        file.close()
	return

print "Helloooooooo."
n1 = "Prakash"
n2 = "Tejas"
n3 = "Nirmala"
prakash = "00:61:71:BE:24:E5"
tejas = "B4:8B:19:B7:10:21"
nirmala = "C0:EE:FB:42:5A:82"

while True:
	print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
	result = bluetooth.lookup_name(prakash, timeout=5)
	inoutprint (n1, result, 1)
	result = bluetooth.lookup_name(tejas, timeout=5)	
	inoutprint (n2, result, 2)
	result = bluetooth.lookup_name(nirmala, timeout=5)
	inoutprint (n3, result, 3)
	filewrite()	
	time.sleep(5) 
