your_phenotype = input("Введите вашу группу крови: (I, II, III, IV) ").strip().upper()
your_friend_phenotype = input("Введите группу крови вашего подопытного: (I, II, III, IV)").strip().upper()

if your_phenotype == "I" and your_friend_phenotype == "I":
    print("ДА, сливай его!")
elif your_phenotype == "II" and your_friend_phenotype == "II" or your_friend_phenotype == "I":
    print("Да, сюда его!")
elif your_phenotype == "III" and your_friend_phenotype == "III" or your_friend_phenotype == "I":
    print("Отлично, нам подходит!")
elif your_phenotype == "IV" and your_friend_phenotype == "IV" or your_friend_phenotype == "I":
    print("И этого возьмем!") 
else:
    print("Вас спасет чудо.")