# Exercice 7 : Mutations (BONUS)

# Exercice 6 : Assemblage final
# But : Rassembler chaque exercice pour en faire un seul programme.

aa = {
    "UUA":"Leu",
    "UUG":"Leu",
    "CUU":"Leu",
    "CUC":"Leu",
    "CUA":"Leu",
    "CUG":"Leu",
    "UUU":"Phe",
    "UUC":"Phe",
    "AUU":"Ile",
    "AUC":"Ile",
    "AUA":"Ile",    
    "AUG":"Met",
    "GUU":"Val",
    "GUC":"Val",
    "GUA":"Val",
    "GUG":"Val",
    "UCU":"Ser",
    "UCC":"Ser",
    "UCA":"Ser",
    "UCG":"Ser",
    "AGU":"Ser",
    "AGC":"Ser",
    "CCU":"Pro",
    "CCC":"Pro",
    "CCA":"Pro",
    "CCG":"Pro",
    "ACU":"Thr",
    "ACC":"Thr",
    "ACA":"Thr",
    "ACG":"Thr",
    "GCU":"Ala",
    "GCC":"Ala",
    "GCA":"Ala",
    "GCG":"Ala",
    "UAU":"Tyr",
    "UAC":"Tyr",
    "CAU":"His",
    "CAC":"His",
    "CAA":"Gln",
    "CAG":"Gln",
    "AAU":"Asn",
    "AAC":"Asn",
    "AAA":"Lys",
    "AAG":"Lys",
    "GAU":"Asp",
    "GAC":"Asp",
    "GAA":"Glu",
    "GAG":"Glu",
    "UGU":"Cys",
    "UGC":"Cys",
    "UGG":"Trp",
    "CGU":"Arg",
    "CGC":"Arg",
    "CGA":"Arg",
    "CGG":"Arg",
    "AGA":"Arg",
    "AGG":"Arg",
    "GGU":"Gly",
    "GGC":"Gly",
    "GGA":"Gly",
    "GGG":"Gly",
    "UAA":"STOP",
    "UAG":"STOP",
    "UGA":"STOP",
}

adn_normal = "AAGCTCGAGACATACGATADACCTGAGCACC8TGTFAGACGAGCCACCTCICAAAGTACCCCTATAATGAAAATCACTAAA"
adn_mute1  = "AAGCTCGAGACGTACGATADACCTGAGCACC8TGTFAGTCGAGCCACCTCICAAAGTACCCCTATAATGAAAATCACTAGA"
adn_mute2  = "AAGCTCGAGACGTACGATADACCTGAGCACC8TGTFAGTCGAGCCACCTCICAAAGTACACCTATAATGAAAATCACTAGA"
nucleotides_valide = ["A", "T", "C", "G"]
stop = ("UAA", "UAG", "UGA")    # Les codons STOP

def verif_adn(adn):     # Permet de vérifier la validité d'une séquence d'ADN.
    new_sequence = ""
    index = 0
    for i in adn:       # Parcourt la séquence d'ADN
        if i in nucleotides_valide:
            new_sequence += i
            index += 1
        else:           # Si une erreur est détectée, remplace le nucléotide invalide par T
            print("- Erreur à l'index " + str(index) + " : " + str(i) + " n'est pas un nucléotide valide. Remplacement par T.")
            new_sequence += "T"
            index += 1
    print("=== Nouvelle séquence ===\n" + new_sequence)
    return new_sequence

def creation_arn_messager(adn2):
    new_sequence = ""
    for i in adn2:
        if i == "A":
            new_sequence += "U"
        elif i == "T":
            new_sequence += "A"
        elif i == "C":
            new_sequence += "G"
        elif i == "G":
            new_sequence += "C"
    print("=== Séquence d'ARN messager ===\n" + new_sequence)
    return new_sequence

def verif_stop(arn):
    index = 0
    new_sequence = ""
    codon_check = ""
    for i in arn:
        codon_check += i
        new_sequence += i
        if len(codon_check) == 3:
            if codon_check in stop:
                break
            else:
                codon_check = ""
        index += 1
    print("Codon STOP trouvé à l'index " + str(index) + " (" + codon_check + ")\n=== Nouvelle séquence d'ARN ===\n" + new_sequence)
    return new_sequence

def synthèse_acides_aminés(arn2):
    acides_aminés = []
    codon_check = ""
    for i in arn2:
        codon_check += i
        if len(codon_check) == 3:
            if codon_check in aa:
                acides_aminés.append(aa[codon_check])
                codon_check = ""
    return acides_aminés

# Création de la liste d'acides aminés pour l'ADN normal
print("")
print("__ Nouvelle analyse __")
adn_normal_valide        = verif_adn(adn_normal)
arn_normal_messager      = creation_arn_messager(adn_normal_valide)
arn_normal_messager2     = verif_stop(arn_normal_messager)
acides_aminés_adn_normal = synthèse_acides_aminés(arn_normal_messager2)
print("=== Liste acides aminés ADN normal ===\n" + str(acides_aminés_adn_normal))

# Création de la liste d'acides aminés pour l'ADN-mute-1
print("")
print("__ Nouvelle analyse __")
adn_mute1_valide         = verif_adn(adn_mute1)
arn_mute1_messager       = creation_arn_messager(adn_mute1_valide)
arn_mute1_messager2      = verif_stop(arn_mute1_messager)
acides_aminés_adn_mute1  = synthèse_acides_aminés(arn_mute1_messager2)
print("=== Liste acides aminés ADN mute 1 ===\n" + str(acides_aminés_adn_mute1))

# Création de la liste d'acides aminés pour l'ADN-mute-2
print("")
print("__ Nouvelle analyse __")
adn_mute2_valide         = verif_adn(adn_mute2)
arn_mute2_messager       = creation_arn_messager(adn_mute2_valide)
arn_mute2_messager2      = verif_stop(arn_mute2_messager)
acides_aminés_adn_mute2  = synthèse_acides_aminés(arn_mute2_messager2)
print("=== Liste acides aminés ADN mute 2 ===\n" + str(acides_aminés_adn_mute2))

print("")
print("__ Tous les acides aminés __")
print(str(acides_aminés_adn_normal))
print(str(acides_aminés_adn_mute1))
print(str(acides_aminés_adn_mute2))

def comparaison_aa(aa1, aa2):   # Permet de comparer 2 listes d'acides aminés entre elles.
    index = 0                   # Permet de garder la position d'où on se trouve lors de l'itération sur les listes d'acides aminés.
    check_final = 0             # Permet juste de vérifier qu'il n'y a pas eu de mutations, et d'afficher "Pas de mutation détectée" à la fin.
    for i, j in zip(aa1, aa2):  # Permet de prendre mes 2 paramètres aa1 et aa2 de la fonction (qui sont des listes de str), et de combiner les i-ème et j-ème élément en des tuples, que l'on va ensuite comparer.
        if i != j:              # Permet de comparer les éléments i et j de chaque tuple crée. S'il sont différents, cela veut dire qu'il y a une mutation.
            print("Mutation détectée !")
            print("Au rang " + str(index) + ", " + str(i) + " est devenu " + str(j) + ".")
            comparaison_codon(adn_normal_valide, adn_mute2_valide, index)     # Maintenant je dois savoir quel nucléotide (parmi les 3) a changé dans le codon qui a provoqué la mutation.
            check_final += 1
        index += 1
    if check_final == 0:
        print("Pas de mutation détectée.")

def comparaison_codon(adn1, adn2, rang):    # Permet de savoir quel nucléotide a changé dans le codon muté.
    index = (rang*3)                        # Je ne veux comparer que le codon correspondant à la mutation. Et je sais que les codons sont des paquets de 3 nucléotides. Donc les nucléotides coupables seront au rang = rang_du_codon * 3.
    if adn1[index] != adn2[index]:          # Comme je ne sais pas lequel des 3 nucléotides du codon a muté, je vérifie simplement les 3 nucléotides du codon.
        print("Le nucléotide de rang " + str(index) + " est passé de " + str(adn1[index]) + " à " + str(adn2[index]) + ".")
    elif adn1[index+1] != adn2[index+1]:
        print("Le nucléotide de rang " + str(index+1) + " est passé de " + str(adn1[index+1]) + " à " + str(adn2[index+1]) + ".")
    elif adn1[index+2] != adn2[index+2]:
        print("Le nucléotide de rang " + str(index+2) + " est passé de " + str(adn1[index+2]) + " à " + str(adn2[index+2]) + ".")
    
print("")
print("== Comparaison de adn et adn-mute-1 ==")
comparaison_aa(acides_aminés_adn_normal, acides_aminés_adn_mute1)

print("")
print("== Comparaison de adn et adn-mute-2 ==")
comparaison_aa(acides_aminés_adn_normal, acides_aminés_adn_mute2)