from assignment_validator import validate_assignment, report

validate_assignment(
    assigment='Met welke query kun je de wapens laten zien met een prijs van 100 – 1000?',
    filename='deel06_vraag01.py', 
    query_contains=['weapon','price', '100', '1000'], 
    functionality_used=['SELECT','WHERE'],
    expected_rowcount=25, 
    expected_columns=4
)

validate_assignment(
    assigment='Met welke query kun je de wapens laten zien met een attack van 300 – 600?',
    filename='deel06_vraag02.py', 
    query_contains=['weapon','attack', '300', '600'], 
    functionality_used=['SELECT','WHERE'],
    expected_rowcount=7, 
    expected_columns=4
)

validate_assignment(
    assigment='Met welke query kun je het aantal dieren zien die een defense hebben van 7 - 9?',
    filename='deel06_vraag03.py', 
    query_contains=['animal','defense', '7', '9'], 
    functionality_used=['SELECT','WHERE','COUNT()'],
    expected_columns=1,
    expected_firstrowValue=23
)

validate_assignment(
    assigment='Met welke query kan je alle personen laten zien de beginnen met de letter B?',
    filename='deel06_vraag04.py', 
    query_contains=['person','name','B%'], 
    functionality_used=['SELECT','WHERE','LIKE'],
    expected_columns=1,
    expected_firstrowValue=11
)

validate_assignment(
    assigment='Met welke query kan je alle dieren laten zien waar de letter a in zit?',
    filename='deel06_vraag05.py', 
    query_contains=['animal','type', '%a%'], 
    functionality_used=['SELECT','WHERE','LIKE'],
    expected_rowcount=59, 
    expected_columns=6
)

validate_assignment(
    assigment='Met welke query kan je alle dieren laten zien waar achter de letter e een letter a in zit?',
    filename='deel06_vraag06.py', 
    query_contains=['animal','type','%a%e%'], 
    functionality_used=['SELECT','WHERE','LIKE'],
    expected_rowcount=23, 
    expected_columns=6
)

validate_assignment(
    assigment='Met welke query kan je alle wapens laten zien die eindigen op de letter d?',
    filename='deel06_vraag07.py', 
    query_contains=['weapon','name','%d'], 
    functionality_used=['SELECT','WHERE','LIKE'],
    expected_rowcount=7, 
    expected_columns=4
)

report()