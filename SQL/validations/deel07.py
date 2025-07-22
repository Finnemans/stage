from assignment_validator import validate_assignment, report

validate_assignment(
    assigment='Hoeveel personen zijn NPC’s?',
    filename='deel07_vraag01.py', 
    query_contains=['npc'], 
    functionality_used=['SELECT','COUNT'],
    expected_columns=1,
    expected_firstrowValue=194
)

validate_assignment(
    assigment='Hoeveel dieren zijn er in RubyQuest?',
    filename='deel07_vraag02.py', 
    query_contains=['animal'], 
    functionality_used=['SELECT','COUNT'],
    expected_columns=1,
    expected_firstrowValue=105
)

validate_assignment(
    assigment='Hoeveel steden zijn er aanwezig?',
    filename='deel07_vraag03.py', 
    query_contains=['city'], 
    functionality_used=['SELECT','COUNT'],
    expected_columns=1,
    expected_firstrowValue=27
)

validate_assignment(
    assigment='Met welke query kan je zien hoeveel schapen er in RubyQuest te vinden zijn?',
    filename='deel07_vraag04.py', 
    query_contains=['animal','type','Sheep'], 
    functionality_used=['SELECT','WHERE','COUNT'],
    expected_columns=1,
    expected_firstrowValue=23
)

validate_assignment(
    assigment='Hoeveel zeeslangen zijn er te vinden in RubyQuest?',
    filename='deel07_vraag05.py', 
    query_contains=['animal','type','Sea Snake'], 
    functionality_used=['SELECT','WHERE','COUNT'],
    expected_columns=1,
    expected_firstrowValue=6
)

report()