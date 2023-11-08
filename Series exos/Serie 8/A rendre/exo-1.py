# Exercice 1 : Séquence d'ADN
# But : Permet de vérifier si une séquence d'ADN est valide.

sequence_adn = "AAGCTCGAGACATACGATADACCTGAGCACC8TGTFAGACGAGCCACCTCICAAAGTACCCCTATAATGAAAATCACTAAA"
nucleotides_valide = ["A", "T", "C", "G"]

def verif_adn(adn):     # Création d'une fonction qui permet de vérifier la validité d'une séquence d'ADN.
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

verif_adn(sequence_adn)
