from assignment_validator import validate_assignment, report

validate_assignment(
    assigment='Met welke query kun je zien welke minimale snelheid de dieren hebben?',
    filename='deel08_vraag01.py', 
    query_contains=['animal','speed'], 
    functionality_used=['SELECT','MIN'],
    expected_columns=1,
    expected_firstrowValue=3
)

validate_assignment(
    assigment='Met welke query kun je zien wat de snelheid is van het snelste dier?',
    filename='deel08_vraag02.py', 
    query_contains=['animal','speed'], 
    functionality_used=['SELECT','MAX'],
    expected_columns=1,
    expected_firstrowValue=10
)

validate_assignment(
    assigment='Met welke query kun je laten zien wat de minimale attack van een wapen is?',
    filename='deel08_vraag03.py', 
    query_contains=['weapon','attack'], 
    functionality_used=['SELECT','MIN'],
    expected_columns=1,
    expected_firstrowValue=100
)

validate_assignment(
    assigment='Met welke query kun je laten zien hoeveel het duurste wapen kost?',
    filename='deel08_vraag04.py', 
    query_contains=['weapon','price'], 
    functionality_used=['SELECT','MAX'],
    expected_columns=1,
    expected_firstrowValue=2850
)

validate_assignment(
    assigment='Met welke query laat je zien wat het gemiddelde aantal ervaringspunten is (afgerond op een heel getal) die je per quest kan verdienen?',
    filename='deel08_vraag05.py', 
    query_contains=['quest','experience'], 
    functionality_used=['SELECT','AVG', 'ROUND'],
    expected_columns=1,
    expected_firstrowValue=1939.0
)

validate_assignment(
    assigment='Met welke query laat je zien wat het totaal aantal goud dat je met niet opgepakte quests kunt verdienen?',
    filename='deel08_vraag06.py', 
    query_contains=['quest','gold','holder'], 
    functionality_used=['SELECT','WHERE','SUM'],
    expected_columns=1,
    expected_firstrowValue=61431
)

validate_assignment(
    assigment='Met welke query laat je zien de hoeveelheid en wat de gemiddelde prijs en aanvalskracht is van alle wapens met het woord ‘sword’ er in?',
    filename='deel08_vraag07.py', 
    query_contains=['weapon','name','%sword%', 'price', 'attack'], 
    functionality_used=['SELECT','WHERE','LIKE', 'COUNT', 'AVG'],
    expected_columns=3
)

report()