import random
HANGMAN = ("""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

WORDS = ["GRACZ", "ZIOM", "MARTIN", "DUPEK", "NADZIEJA", "TRAKTORZYSTA"]
words = random.choice(WORDS)
slowo = "-" * len(words)
max_zyc = len(HANGMAN)
zycie = 0
uzute = []
while max_zyc > zycie and words != slowo:
    print(f"Litery ktore juz zostalu uzyte:")
    print(uzute)
    print(f'\t{slowo}')
    szansa = input("Podal litere: ")
    szansa = szansa.upper()
    while szansa in uzute:
        print("Ta litera juz byla uzyta")
        szansa = input("Podal litere: ")
        szansa.upper()
    uzute.append(szansa)
    if szansa in words:
        print("Tak ta litera znajduje sie w zgadywaaniym slowie")
        new = ""
        for i in range(len(words)):
            if szansa == words[i]:
                new += szansa
            else:
                new += slowo[i]
        slowo = new
    else:
        print(HANGMAN[zycie])
        print("\nNiestety ta litera nie znajduje sie w slowie")
        zycie +=1
if words == slowo:
    print("gratuluje wygrales")
else:
    print("przegrales")
