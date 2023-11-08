codon_check = "UAA"

i = "C"

print(codon_check)
update_codon_check = list(codon_check)
print(update_codon_check)
update_codon_check.pop(0)
print(update_codon_check)
update_codon_check.append(i)
print(update_codon_check)
print(codon_check)
codon_check = "".join(update_codon_check)
print(codon_check)