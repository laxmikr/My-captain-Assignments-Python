str=input("Input the filename: ")
ext=str.split(".")
if ext[-1]=="py":
    print("The extension of the file is : 'python'")
else:
    print("The extension of the file is :"+repr(ext[-1]))
