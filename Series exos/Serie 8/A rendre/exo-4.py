# Exercice 4 : Recherche de STOP
# But : Vérifier s'il existe des codons STOP dans une séquence d'ADN.

sequence_adn = "UUCGAGCUCUGUAUGCUAUAUGGACUCGUGGAACAAUCUGCUCGGUGGAGAGUUUCAUGGGGAUAUUACUUUUAGUGAUUU"
stop = ("UAA", "UAG", "UGA")    # Les codons STOP

def verif_stop(adn):
    index = 1
    new_sequence = ""
    codon_check = ""

    for i in adn:
        codon_check += i        # Je crée une variable codon_check qui ne contiendra que 3 nucléotides et qui s'actualise à chaque itération.
        new_sequence += i
        #print(codon_check)
        if len(codon_check) == 3:       # Une fois que codon_check contient 3 nucléotides, je vérifie s'il est dans le tuple stop. Utile surtout pour le début de l'itération.
            if codon_check in stop:
                break                   # Si codon_check est dans le tuple stop, j'arrête l'analyse, et je donne la nouvelle séquence ARN.
            update_codon_check = list(codon_check)      # Pour pouvoir actualiser codon_check (qui est un str), je le transforme en liste.
            update_codon_check.pop(0)                   # je retire le 1er élément de codon_check.
            codon_check = "".join(update_codon_check)   # puis je retransforme codon_check (qui était une liste) en str.
        index += 1

    print("Codon STOP trouvé à l'index " + str(index) + " (" + codon_check + ")\nNouvelle séquence d'ARN :\n" + new_sequence)


verif_stop(sequence_adn)