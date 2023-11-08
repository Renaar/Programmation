# Exercice 2 : Deuxième brin d'ADN
# But : Donne la séquence complémentaire d'une séquence d'ADN.

sequence_adn = "AAGCTCGAGACATACGATATACCTGAGCACCTTGTTAGACGAGCCACCTCTCAAAGTACCCCTATAATGAAAATCACTAAA"

def complementaire_sequence_adn(adn):
    new_sequence = ""
    for i in adn:
        if i == "A":
            new_sequence += "T"
        elif i == "T":
            new_sequence += "A"
        elif i == "C":
            new_sequence += "G"
        elif i == "G":
            new_sequence += "C"
    print(new_sequence)

complementaire_sequence_adn(sequence_adn)
