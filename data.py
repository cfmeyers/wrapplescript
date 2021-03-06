from models import Name, Address


COMPUTER_SCIENTIST_NAMES = (
    Name(first='Simon', last='Peyton Jones'),
    Name(first='Hal', last='Abelson'),
    Name(first='Charles', last='Babbage'),
    Name(first='John', last='Backus'),
    Name(first='Tim', last='Berners-Lee'),
    Name(first='Sergey', last='Brin'),
    Name(first='Alonzo', last='Church'),
    Name(first='Haskell', last='Curry'),
    Name(first='Edsger', last='Dijkstra'),
    Name(first='Brendan', last='Eich'),
    Name(first='Douglas', last='Engelbart'),
    Name(first='Martin', last='Fowler'),
    Name(first='Grace', last='Hopper'),
    Name(first='Bill', last='Joy'),
    Name(first='Alan', last='Kay'),
    Name(first='Donald', last='Knuth'),
    Name(first='Rasmus', last='Lerdorf'),
    Name(first='Ada', last='Lovelace'),
    Name(first='John', last='McCarthy'),
    Name(first='Douglas', last='McIlroy'),
    Name(first='Marvin', last='Minsky'),
    Name(first='John', last='von Neumann'),
    Name(first='Larry', last='Page'),
    Name(first='Alan', last='Turing'),
    Name(first='Dennis', last='Ritchie'),
    Name(first='Guido', last='van Rossum'),
    Name(first='Bruce', last='Schneier'),
    Name(first='Adi', last='Shamir'),
    Name(first='Claude', last='Shannon'),
    Name(first='Richard', last='Stallman'),
    Name(first='Guy', last='Steele'),
    Name(first='Bjarne', last='Stroustrup'),
    Name(first='Gerald', last='Jay Sussman'),
    Name(first='Andrew', last='Tanenbaum'),
    Name(first='Ken', last='Thompson'),
    Name(first='Linus', last='Torvalds'),
    Name(first='Larry', last='Wall'),
)

EXAMPLE_ADDRESSES_BY_STATE ={
    'NY': Address(
            street_address='138 Eagle Street', 
            city='Albany',
            state='NY',
            zip_code='12202'
        ),
    'CA': Address(
            street_address='1526 H Street', 
            city='Sacramento',
            state='CA',
            zip_code='95814'
        ), 
    'CT': Address(
            street_address='990 Prospect Avenue', 
            city='Hartford',
            state='CT',
            zip_code='06105'
        ), 
    'VA': Address(
            street_address="Governor's Mansion", 
            city='Richmond',
            state='VA',
            zip_code='23219'
        ), 
}

ADJECTIVES = [
    'arcadian',
    'baleful',
    'bellicose',
    'bilious',
    'boorish',
    'calamitous',
    'caustic',
    'cerulean',
    'comely',
    'concomitant',
    'contumacious',
    'corpulent',
    'crapulous',
    'defamatory',
    'didactic',
    'dilatory',
    'dowdy',
    'efficacious',
    'effulgent',
    'egregious',
    'endemic',
    'equanimous',
    'execrable',
    'fastidious',
    'feckless',
    'fecund',
    'friable',
    'fulsome',
    'garrulous',
    'guileless',
    'gustatory',
    'heuristic',
    'histrionic',
    'hubristic',
    'incendiary',
    'insidious',
    'insolent',
    'intransigent',
    'inveterate',
    'invidious',
    'irksome',
    'jejune',
    'jocular',
    'judicious',
    'lachrymose',
    'limpid',
    'loquacious',
    'luminous',
    'mannered',
    'mendacious',
    'meretricious',
    'minatory',
    'mordant',
    'munificent',
    'nefarious',
    'noxious',
    'obtuse',
    'parsimonious',
    'pendulous',
    'pernicious',
    'pervasive',
    'petulant',
    'platitudinous',
    'precipitate',
    'propitious',
    'puckish',
    'querulous',
    'quiescent',
    'rebarbative',
    'recalcitrant',
    'redolent',
    'rhadamanthine',
    'risible',
    'ruminative',
    'sagacious',
    'salubrious',
    'sartorial',
    'sclerotic',
    'serpentine',
    'spasmodic',
    'strident',
    'taciturn',
    'tenacious',
    'tremulous',
    'trenchant',
    'turbulent',
    'turgid',
    'ubiquitous',
    'uxorious',
    'verdant',
    'voluble',
    'voracious',
    'wheedling',
    'withering',
    'zealous',
]
