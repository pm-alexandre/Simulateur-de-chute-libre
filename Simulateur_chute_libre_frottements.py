import matplotlib.pyplot as plt

m=0
g=9.81
v=0

while True:
    try:
        avec_ou_sans_f=input("Premièrement, souhaites-tu négliger les frottements [Y/N] ?  ").strip().upper()
        if avec_ou_sans_f not in ['Y','N']:
            raise ValueError
        break
    except ValueError:
        print("Erreur : tu dois répondre par Y(es) ou N(o) (oui pour 'Y' et non pour 'N' ^^)")
    
    
    
try:    
    h_0=float(input("A quelle hauteur veux-tu lacher ton objet (en mètre(s)) ?  "))
except ValueError:
    print("Erreur : tu dois entrer un nombre réel (ex: 1.618)")
    exit()
    
    
try:
    m=float(input("Quelle sera la masse de ton objet (en kilogramme) ?  "))
    if m <= 0:
        raise ValueError("La masse doit être positive !")
except ValueError as e:
    print(f"Erreur:{e}")
    exit()
   
    
if avec_ou_sans_f=="Y":
    try:
        k=float(input("Quelle sera la valeur du coefficient de frottement (en N.s/m)?  "))
    except ValueError:
        print("Erreur : tu dois entrer un nombre réel (ex. 2.718)")
        exit()


    
h= h_0
dt=0.1
t=0


liste_h=[]
liste_t=[]
liste_v=[]
liste_Ec=[]
liste_Ep=[]
liste_Em=[]


while h > 0:
    if avec_ou_sans_f == "Y":
        a= g-(k/m)*v
    else:
         a=g   
    h = h - v * dt
    v = v + a * dt
    E_p= m*g*h
    E_c=0.5*m*v**2
    E_m=E_c + E_p
    
    if h < 0:
        h=0
    liste_t.append(t)
    liste_h.append(h)
    liste_v.append(v)
    liste_Ec.append(E_c)
    liste_Ep.append(E_p)
    liste_Em.append(E_m)
    t += dt
    
    
    
plt.figure(figsize=(15,12))

plt.subplot(2, 2,1)
plt.title("Chute libre sans frottement")
plt.plot(liste_t,liste_h,"o",label="Hauteur ($m$)")
plt.grid()
plt.xlabel("Temps ($s$)")
plt.ylabel("Hauteur ($m$)")
plt.legend()

plt.subplot(2, 2,2)
plt.title("Vitesse en fonction du temps")
plt.grid()
plt.plot(liste_t,liste_v,"o",label="Vitesse ($m.s^{-1}$)",color="r")
plt.xlabel("Temps ($s$)")
plt.legend()
plt.ylabel("Vitesse ($m.s^{-1}$)")


plt.subplot(2,2, 3)
plt.title("Courbe d'énergie en fonction du temps")
plt.grid()
plt.plot(liste_t,liste_Ec,"-",color="g",label="Energie cinétique")
plt.plot(liste_t,liste_Ep,"-",color="gray",label="Energie potentielle")
plt.plot(liste_t, liste_Em,"-",color="brown",label="Energie mécanique")
plt.xlabel("Temps ($s$)")
plt.ylabel("Energies ($J$)")
plt.legend()

plt.tight_layout()
plt.show()





















    
    

    
