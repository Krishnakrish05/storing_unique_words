def unique():
    files= open("places.txt","r")
    words =files.read().split()
    newfile=open("sortedfile.txt","w")

    list=[]
    for i in words:
        if i not in list:
            list.append(i)


    list.sort(key=len)
    print(list)

    for j in list:
        newfile.write(j + ":" + str(len(j)) + "\n")



unique()