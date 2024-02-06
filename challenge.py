print("Chcete zadat IPv4 v dec (1) nebo bin (2)?")
volba = int(input("Zadejte Vaší volbu: "))

if volba == 1:
    
    cislo = int(input("zadejte dec číslo v dec: "))
    binarni = bin(cislo)
    print("binární soustava:", binarni[2** cislo])

if volba == 2:
    
    bin_cislo = input("zadejte bin číslo v bin: ")
    dec_cislo = 0
    mocnina = len(bin_cislo) - 1 
    for bit in bin_cislo:
        dec_cislo += int(bit) * 2 **mocnina
        mocnina -= 1
    print("dec soustava:", dec_cislo)
    










