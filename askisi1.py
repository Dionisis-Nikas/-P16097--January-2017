print "\n\nHey there!!! This is my app for removing exclamation marks who aren't in the end of the sentence \n"
protasi=raw_input("Give me your sentence please \n\n")

length=len(protasi)
delete=0
x="\n"
for i in range (0,length):
    if (protasi[i]=="!"):
        if i<(length-1):

            if (protasi[i+1]==" "):
                x=x+protasi[i]

            elif (protasi[i+1]!=" "):
                nex =1
                if (protasi[i+1]=="!"):
                    if i==length-2:
                        x=x+protasi[i]
                    else:

                        y=""
                        num=1
                        while ((protasi[i+num]=="!")and (i+num<length-1)):
                            y= y+protasi[i+num]
                            num=num+1
                            if (protasi[i+num]!="!")and(protasi[i+num]!=" "):
                                nex = 1
                            if protasi[i+num]==" ":
                                nex = 0
                            if i+num==length-1:
                                nex = 2

                        if nex == 1:
                            x= x+protasi[i].strip("!")
                            delete=delete+1
                        elif nex == 0:
                            x= x+protasi[i]
                        elif nex == 2:
                            x= x+protasi[i]
        elif i==length-1:
            x=x+protasi[i]
    else:
        if (protasi[i]==" "):
            x= x+" "+protasi[i]
        else:
            x=x+protasi[i]


if delete==0:
    print "\n \nNo '!' deleted....my app was no use to you..."
else:
    print "\n\n %d '!' were deleted....your welcome" %(delete)
print "\n"+ x+"\n"
