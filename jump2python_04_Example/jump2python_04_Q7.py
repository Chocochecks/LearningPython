f = open("test1.txt","r")
body = f.read()
f.close()

body = body.replace("java","python")
f = open("test1.txt","w")
f.write(body)
f.close()