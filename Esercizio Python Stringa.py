stringa= input("Scrivere una stringa: ")
lettere = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
print("i numeri di volte in cui i le lettere si ripetono all'interno della stringa è")
stringa = list(stringa.upper())
for lettera in lettere:
    if stringa.count(lettera) > 0:
        print(lettera, " = ",stringa.count(lettera))
