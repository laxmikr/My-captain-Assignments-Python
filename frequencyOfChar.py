def most_frequent():
    string=input("Enter the string: ")
    dict={}

    for i in string:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    print(sorted(dict.items(),key=lambda x:x[1],reverse=True))
  

most_frequent()

