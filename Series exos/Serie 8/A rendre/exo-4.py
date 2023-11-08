# Exercice 4 : Recherche de STOP
# But : Vérifier s'il existe des codons STOP dans une séquence d'ADN.
# Version simple où la séquence d'ARN est simplement découpée en paquet de 3 nucléotides.

sequence_arn = "UUCGAGCUCUGUAUGCUAUAUGGACUCGUGGAACAAUCUGCUCGGUGGAGAGUUUCAUGGGGAUAUUACUUUUAGUGAUUU"
stop = ("UAA", "UAG", "UGA")    # Les codons STOP

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

    print("Codon STOP trouvé à l'index " + str(index) + " (" + codon_check + ")\nNouvelle séquence d'ARN :\n" + new_sequence)


verif_stop(sequence_arn)