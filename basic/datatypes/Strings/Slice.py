var="HELLO PYTHON"

print ("var:",var)
#print ("var[:5]:", var[:5])
print ("var[:6][:2]:", var[:6][:2])
"""
 HE
"""

var1=var[:6]
print ("slice:", var1)
#print ("var1[:2]:", var1[:2])

s1="WORD"
print ("original string:", s1)
l1=list(s1)

l1.insert(3,"L")

print (l1)

s1=''.join(l1)
print ("Modified string:", s1)