from assignment_validator import validate_assignment, report

validate_assignment(
    assigment='Met welke query (icm een subselelect) kun je de steden laten zien die vallen in regios North en South Groval?',
    filename='deel09_vraag01.py', 
    query_contains=['city','region', 'id', 'name', 'North', 'South', 'Groval'], 
    functionality_used=['SELECT','IN', 'OR'],
    expected_rowcount=11, 
    expected_columns=3
)

validate_assignment(
    assigment='Met welke query (icm een subselelect) kun je de dieren laten zien die captian america bezit?',
    filename='deel09_vraag02.py', 
    query_contains=['person','animal','owner', 'id', 'name', 'Captain', 'America'], 
    functionality_used=['SELECT','WHERE'],
    expected_rowcount=2, 
    expected_columns=6
)

report()