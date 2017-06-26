tp = input()
n = input()
tpd = input()
if(tpd=="carnivoro"):
    print("aguia\n")
elif(tpd=="onivoro" and tp=="invertebrado"):
    print("minhoca\n")
elif(tpd=="onivoro" and n=="ave"):
    print("pomba\n")
elif(tpd=="onivoro"):
    print("homem\n")
elif(tpd=="herbivoro" and n=="mamifero"):
    print("vaca\n")
elif(tpd=="herbivoro" and n=="inseto"):
    print("lagarta\n")
elif(tpd=="hematofago" and n=="inseto"):
    print("pulga\n")
elif(tpd=="hematofago" and n=="anelideo"):
    print("sanguessuga\n")
