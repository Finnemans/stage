import math
import time
oliebol = 1.20
appelflap = 1.60
zak = 10.00
zakken = 0
subtotaal = 0
opnieuw = True

while opnieuw == True:
    while True:
        try:
            print(f"Hoeveel oliebollen van €{oliebol:.2f} wilt u?")
            bollen = int(input('? '))
            
            zakken = bollen // 10
            overigbollen = bollen % 10
            bedrag = zakken * zak
            subtotaal += bedrag
            text3 = f"Oliebollen (zak):   {zakken} x  €{zak:.2f} =  €{bedrag:.2f}"

            bedrag = overigbollen * oliebol
            subtotaal += bedrag
            text1 = f"Oliebollen (los):   {overigbollen} x  €{oliebol:.2f} =  €{bedrag:.2f}"
            break
        except:
            print('Dit is geen heel getal!')



    while True:
        try:
            print(f"Hoeveel appelflappen van €{appelflap:.2f} wilt u?")
            flappen = int(input('? '))
            bedrag = flappen * appelflap
            subtotaal += bedrag
            text2 = f"Appelflappen:      {flappen} x  €{appelflap:.2f} =  €{bedrag:.2f}"
            break
        except: 
            print('Dit is geen heel getal!')

    bolbaktijd = 75
    zakvultijd = 15
    flappaktijd = 30

    baktijdoliebol = (bollen // 15) * bolbaktijd
    restoliebol = bollen % 15
    if restoliebol > 0:
        baktijdoliebol += bolbaktijd

    zakkentijd = zakken * zakvultijd
    if overigbollen > 0:
        zakkentijd += zakvultijd

    olieboltijd = baktijdoliebol + zakkentijd

    inpakflappentijd = math.ceil(flappen / 3) * flappaktijd

    wachtseconden = olieboltijd + inpakflappentijd
    wachtmin = math.ceil(wachtseconden / 60)

    print('-------------[UW BESTELLING]-------------')
    if zakken >= 1:
        print(text3)

    if overigbollen >= 1:
        print(text1)

    if flappen >= 1:
        print(text2)

    if subtotaal >= 50:
        totaal = subtotaal / 100 * 92.5
        korting = subtotaal /100 * 7.5
        print('-----------------------------------------')
        print(f"Subtotaal                       €{subtotaal:.2f}")
        print(f"Korting(7.5%):                  -€{korting:.2f}")
    else:
        totaal = subtotaal

    BTW = totaal * 9 / 109

    print('-----------------------------------------')
    print(f'Totaal:                          €{totaal:.2f}')
    print(f'BTW (9%):                         €{BTW:.2f}')
    print(' ')
    print(f'Wachttijd: {wachtmin} minuten')
    opnieuw = False

    time.sleep(5)
    while True:
        try:
            print(' ')
            print("Nog een bestelling invoeren? ")
            JN = input('Ja/Nee ').upper()
            print(' ')
            if JN == 'Ja'.upper():
                opnieuw = True
                break
            elif JN == 'Nee'.upper():
                break
        except:
            print('?')