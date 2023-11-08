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

sequence_adn = "AAGCTCGAGACATACGATADACCTGAGCACC8TGTFAGACGAGCCACCTCICAAAGTACCCCTATAATGAAAATCACTAAA"
nucleotides_valide = ["A", "T", "C", "G"]
stop = ("UAA", "UAG", "UGA")    # Les codons STOP

def verif_adn(adn):     # Permet de vérifier la validité d'une séquence d'ADN.
    new_sequence = ""
    index = 1
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
    index = 1
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

adn_valide = verif_adn(sequence_adn)
arn_messager = creation_arn_messager(adn_valide)
arn_messager2 = verif_stop(arn_messager)
liste_acides_aminés = synthèse_acides_aminés(arn_messager2)
print("=== Séquence d'acides aminés ===\n " + str(liste_acides_aminés))
