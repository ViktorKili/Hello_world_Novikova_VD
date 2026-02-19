quantity_of_capsuls = float(input("введите общее количество произведенных капсул: "))
capsuls_in_pac = float(input("введите количество капсул в одной упаковке: "))

full_packs = quantity_of_capsuls//capsuls_in_pac
remaining = quantity_of_capsuls%capsuls_in_pac

print(f"\n---отчет фасовочного цеха")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул: \t{remaining}")