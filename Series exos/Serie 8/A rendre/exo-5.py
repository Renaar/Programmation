# Exercice 5 : Acides aminés
# But : Transformer la nouvelle séquence d'ARN message en acides aminés.

sequence_arn2 = "UUCGAGCUCUGUAUGCUAUAUGGACUCGUGGAACAAUCUGCUCGGUGGAGAGUUUCAUGGGGAUAUUACUUUUAG"
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

def synthèse_acides_aminés(arn2):
    acides_aminés = []
    codon_check = ""

    for i in arn2:
        codon_check += i
        if len(codon_check) == 3:
            if codon_check in aa:
                acides_aminés.append(aa[codon_check])
                codon_check = ""
    print(acides_aminés)

synthèse_acides_aminés(sequence_arn2)