x=input("Enter your name : ")
dic = {'ayush':99,'nikhil':87,'nitin':98,'daksh':89}
y=x.lower()
if y in dic:
    print(x,"marks :",dic[y])
else:
    print("Student Not Found")