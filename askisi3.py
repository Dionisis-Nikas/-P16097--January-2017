print "\n\nHello this is my app to move zeros in the end of the list without changing the order or position of other objects in the list \n\n"
print "\nWARNING!! The app will move objects that have zero as their value!! f.e yew0 wont move the zero.\n"

lista= raw_input("\n\nGive the 1st object of the list\n")

counter=1
answer= raw_input("\n\nDo you want to add another object to the list??? Answer with 'yes' or 'no' please.\n")
while answer!="yes" and answer!="no":
    print "You didn't give a correct answer"
    answer= raw_input("\n\nDo you want to add another object to the list??? Answer with 'yes' or 'no' please.\n")
while (answer=="yes"):
    counter=counter+1
    if counter==2:
        print "\n\nGive the %dnd object of the list" %(counter)
        lista_add=raw_input()

    elif counter ==3:
        print "\n\nGive the %drd object of the list" %(counter)
        lista_add=raw_input()
    else:
        print "\n\nGive the %dth object of the list" %(counter)
        lista_add=raw_input()
    lista= lista+ " " +lista_add
    answer= raw_input("\n\nDo you want to add another object to the list??? Answer with 'yes' or 'no' please.\n")
    while answer!="yes" and answer!="no":
        print "\nYou didn't give a correct answer"
        answer= raw_input("\n\nDo you want to add another object to the list??? Answer with 'yes' or 'no' please.\n")
lista= lista.split()
#in case of spaces between objects
diafora=len(lista)-counter
counter=counter+diafora
lista_final= ""
zeros=0
if len(lista)!=0:

    for i in range (0,counter):
        if i<counter-1:
            if lista[i].isdigit() :
                if float(lista[i])==float(0) or int(lista[i])==int(0) :
                    lista_final=lista_final+" "+"Empty"
                    zeros=zeros+1
                else:
                    lista_final=lista_final+" "+lista[i]
            else:
                lista_final=lista_final+" "+lista[i]
        else:
            lista_final=lista_final+" "+lista[i]
    if zeros!=0:
        for i in range (0, zeros):
            lista_final=lista_final+" "+"0"
        print "\n %d  zeros were moved to the end of the list" %(zeros)
    else:
        print "No zeros found or last object is zero..."
    lista_final=lista_final.split()
    print lista_final
else:
    print "Sorry your list was Empty"
