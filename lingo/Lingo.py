import lingowords
import random
from termcolor import colored

while True:

    team1 = {
        "naam": "Team 1",
        "goed_geraden": 0,
        "poging": 0,
        "ballen": [],
        "rood": [],
        "groen": [],
        "bekende_letters": [],
        "kaart": [
            2, 4, 6, 8,
            10, 12, 14, 16,
            18, 20, 22, 24,
            26, 28, 30, 32
        ],
        "bingo_lijnen": [
            [2, 4, 6, 8],
            [10, 12, 14, 16],
            [18, 20, 22, 24],
            [26, 28, 30, 32],

            [2, 10, 18, 26],
            [4, 12, 20, 28],
            [6, 14, 22, 30],
            [8, 16, 24, 32],

            [2, 12, 22, 32],
            [8, 14, 20, 26]
        ]
    }

    team2 = {
        "naam": "Team 2",
        "goed_geraden": 0,
        "poging": 0,
        "ballen": [],
        "rood": [],
        "groen": [],
        "bekende_letters": [],
        "kaart": [
            1, 3, 5, 7,
            9, 11, 13, 15,
            17, 19, 21, 23,
            25, 27, 29, 31
        ],
        "bingo_lijnen": [
            [1, 3, 5, 7],
            [9, 11, 13, 15],
            [17, 19, 21, 23],
            [25, 27, 29, 31],

            [1, 9, 17, 25],
            [3, 11, 19, 27],
            [5, 13, 21, 29],
            [7, 15, 23, 31],

            [1, 11, 21, 31],
            [7, 13, 19, 25]
        ]
    }

    def grabbel_bal(team):

        bingokaart = list(range(1, 33)) + ["groen"] * 3 + ["rood"] * 3

        getrokken_ballen = []

        while len(getrokken_ballen) < 2 and "rood" not in getrokken_ballen:

            bal = random.choice(bingokaart)

            if type(bal) == int and bal not in getrokken_ballen:

                getrokken_ballen.append(bal)

                if bal in team["kaart"] and bal not in team["ballen"]:
                    team["ballen"].append(bal)

            elif bal == "groen":
                team["groen"].append(bal)
                getrokken_ballen.append(bal)

            elif bal == "rood":
                team["rood"].append(bal)
                getrokken_ballen.append(bal)

        return getrokken_ballen

    def geef_feedback(gok, woord, bekende_letters):

        feedback = bekende_letters.copy()

        for i in range(len(gok)):

            if gok[i] == woord[i]:
                bekende_letters[i] = colored(gok[i], "green")
                feedback[i] = colored(gok[i], "green")

            elif gok[i] in woord:
                feedback[i] = colored(gok[i], "yellow")

        print(" | ".join(feedback))

    def nieuwwoord():
        return random.choice(lingowords.nederlands)

    def controleer_bingo(ballen, lijnen):

        for lijn in lijnen:

            if all(x in ballen for x in lijn):
                return True

        return False

    def reset_letters(team, woord):

        team["bekende_letters"] = [" "] * len(woord)
        team["bekende_letters"][0] = woord[0]

    def volgende_beurt(huidig_team, woord):

        huidig_team["poging"] = 0

        reset_letters(team1, woord)
        reset_letters(team2, woord)

        return team2 if huidig_team == team1 else team1

    def controleer_winnaar(team):

        if len(team["groen"]) >= 3:
            print(f'{team["naam"]} wint met 3 groene ballen!')
            return True

        if len(team["rood"]) >= 3:
            print(f'{team["naam"]} verliest met 3 rode ballen!')
            return True

        if controleer_bingo(team["ballen"], team["bingo_lijnen"]):
            print(f'{team["naam"]} heeft bingo!')
            return True

        if team["goed_geraden"] >= 10:
            print(f'{team["naam"]} wint met 10 goed geraden woorden!')
            return True

        return False

    woord = nieuwwoord()

    reset_letters(team1, woord)
    reset_letters(team2, woord)

    huidig_team = team1

    spelen = True

    while spelen:

        print("Woord:", woord)

        print(f'\n{huidig_team["naam"]} is aan de beurt')
        print(" | ".join(huidig_team["bekende_letters"]))

        gok = input("Raad het woord: ").lower()
        
        if gok == "end":

            print(f'{huidig_team["naam"]} geeft op! Het woord was: {woord}')

            spelen = False
            continue

        if len(gok) != len(woord):
            print("Verkeerde woordlengte")
            continue

        if gok == "bingo":

            huidig_team["ballen"].extend([2, 4, 6, 8])

            print(f'bingo! {huidig_team["naam"]} krijgt ballen 2, 4, 6 en 8')

            continue

        if gok == woord:

            print("Goed geraden!")

            ballen = grabbel_bal(huidig_team)

            print("Getrokken ballen:", ballen)

            print(
                f'{huidig_team["naam"]} bingo ballen:',
                huidig_team["ballen"]
            )

            huidig_team["goed_geraden"] += 1

            if controleer_winnaar(huidig_team):
                spelen = False
                continue

            woord = nieuwwoord()

            huidig_team = volgende_beurt(
                huidig_team,
                woord
            )

            continue

        geef_feedback(
            gok,
            woord,
            huidig_team["bekende_letters"]
        )

        huidig_team["poging"] += 1

        print("Poging:", huidig_team["poging"])

        if huidig_team["poging"] >= 5:

            print("Te veel pogingen")

            woord = nieuwwoord()

            huidig_team = volgende_beurt(
                huidig_team,
                woord
            )

    opnieuw = input("\nWil je nog een keer spelen? (ja/nee): ").lower()

    if opnieuw != "ja":
        print("Bedankt voor het spelen!")
        break