from assignment_validator import validate_assignment, report

validate_assignment(
    assigment='Met welke query laat je alle personen zien gesorteerd op naam (ascending)?',
    filename='deel04_vraag01.py', 
    query_contains=['person','name'], 
    functionality_used=['SELECT','DISTINCT','ORDER BY'],
    expected_rowcount=204, 
    expected_columns=1
)

validate_assignment(
    assigment='Met welke query laat je alle steden zien gesorteerd op naam (descending)?',
    filename='deel04_vraag02.py', 
    query_contains=['city','name'], 
    functionality_used=['SELECT','ORDER BY','DESC'],
    expected_rowcount=27, 
    expected_columns=3
)

validate_assignment(
    assigment='Met welke query kun je de eerste 10 personen laten zien?',
    filename='deel04_vraag03.py', 
    query_contains=['person', '10'], 
    functionality_used=['SELECT','LIMIT'],
    expected_rowcount=10, 
    expected_columns=11
)

validate_assignment(
    assigment='Met welke query kun je de 5 duurste wapens laten zien?',
    filename='deel04_vraag04.py', 
    query_contains=['weapon','price'], 
    functionality_used=['SELECT','ORDER BY','DESC'],
    expected_rowcount=5, 
    expected_columns=4
)

validate_assignment(
    assigment='Met welke query kun je de 3 zwakste wapens laten zien?',
    filename='deel04_vraag05.py', 
    query_contains=['weapon','attack'], 
    functionality_used=['SELECT','ORDER BY','ASC'],
    expected_rowcount=3, 
    expected_columns=4
)

validate_assignment(
    assigment='Met welke query kun je laten zien welke verschillende dieren er bestaan?',
    filename='deel04_vraag06.py', 
    query_contains=['animal','type'], 
    functionality_used=['SELECT','DISTINCT'],
    expected_rowcount=7, 
    expected_columns=['type']
)

validate_assignment(
    assigment='Met welke query kun je op alphabetische volgorde laten zien welke professions er zijn bij de NPC\'s?',
    filename='deel04_vraag07.py', 
    query_contains=['npc','profession'], 
    functionality_used=['SELECT','DISTINCT'],
    expected_rowcount=8, 
    expected_columns=['profession']
)

report()