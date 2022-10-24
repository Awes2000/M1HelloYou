from playsound import playsound 
koevoet = 0
antwoord = ['Yes', 'Y', 'y', 'yes', 'YES', 'n' 'No', 'NO']



def pad1_0(): #vrienden zoeken pad langste storyline met beste einde
     print("Je gaat voor je vrienden zoeken") 
     print("Je pakt eerst de auto en alle benodigde voorwerpen")
     print("Tijd om mijn vrienden te zoeken!")
     print("Je rijd langs Skolka, een dorp vlakbij waar 2 goeie vrienden in de buurt zijn")
     print("Er wordt veel geschoten en dergelijke")
     print("Je twijfelt of t veilig is om door te zoeken")
     print("Je parkeert je auto snel ergens veilig en stapt uit")
     print("Er is veel paniek en geschreeuw om je heen")
     print("Je ziet de auto van je vriend geparkeert voor z'n huis")
     print("In de buurt zijn soldaten die mensen beschieten")
     print("Neem je je kans om je vriend z'n huis binnen te glippen?")
     print()
     
     answer = input("\n Ja: \nNee:") #2

     if answer == ("A"): #naar binnen gaan pad 
        (pad1_1) 
     elif answer == ("B"): #niet naar binnen gaan pad
        (pad1_01) 
     else:
        try_again



def pad1_1(): #naar binnen gaan pad
    print("Je besluit om naar binnen te gaan")
    print("De soldaten zijn eventjes afgeleid en je neemt de kans")
    print("Onderweg naar het huis zie je een koevoet op de grond naas het gras bij de ingang")
    print("Neem je de koevoet mee?")
    
    answer = input("\nJa: \nNee:") #
    if answer == 'Ja':
        print("je hebt de koevoet opgepakt") 
        playsound('crowbar.mp3')
        koevoet = 1
    elif answer == 'Nee':
        print("Je hebt de koevoet niet opgepakt")
        koevoet = 0
    else:
        try_again

    print("Je komt aan bij je vrienden zn deur, het stond op een kiertje open")
    print("Hopelijk zijn ze oke")
    print("Je loopt voorzichtig door het huis door en roept voor je vrienden, \n'Oleg, Sasha!, waar zijn jullie??'")
    print("Je raakt bezorgt en ziet in je ooghoek een gleufje met licht")
    print("Je loopt erop af en kijkt door het licht")
    print("Je ziet een mooie blonde dame aan de andere kant zitten in angst, zij heeft geen idee dat je haar kan zien")
    print("Je roept naar haar toe en ze ziet je kijken, ze glimlacht en is blij om je de zien")
    print("Hey + naam, ik ben zo blij om je te zien!") #naam is de userinput in t begin van de game
    print("Sasha zit vast en heeft je hulp nodig")

    if koevoet == 1:
        print("Je gebruikt de koevoet en Sasha is vrijgekomen")
        (pad1_2) #pad 1_2 voor als Sasha vrijkomt

    elif koevoet == 0:
            print("Je hebt geen tools om Sasha te bevrijden")
            (pad1_02) #pad 1_02 Sasha is niet bevrijd
    else:
        (try_again)

def pad1_2(): #Sasha is vrij
    print("Sasha is je zo dankbaar voor het bevrijden van haar")
    print("Jullie zijn allebei blij dat jullie elkaar zien")
    print("Sasha: Oleg... hij is-")
    print("user + str Ja I know")
    print("Kom, pak al je spullen! We moeten snel weg!")
    print("Jullie pakken alles wat jullie nodig hebben")
    print("De auto staat buiten klaar en jullie glippen beide weg")
    print("Je rijdt snel naar het vliegveld toe")
    print("Jullie komen aan")
    print("Dankzij jouw connecties krijgen jullie prioriteit en kunnen jullie snel vluchten")
    print("Jullie zitten naast elkaar in de vliegtuig en troosten elkaar")
    print("De stewardesse komt langs om te vragen wat jullie willen drinken")
    print("Stewardesse: Wat willen jullie drinken?")
    answer = input("\nA:Cola, \nB: Water \nC: Niks") #dit heeft geen invloed op je uitkomst
    if answer =="A":
        print("Ahh, bubblyyyy") #bubbly sound
        (pad1_3)
    elif answer =="B":
        print("Ahhh, verfrissend") #water sound
        (pad1_3)
    elif answer =="C":
        print("Toch maar niet..")
        print("Te veel aan m'n hoofd")
        (pad1_3)
    else:
        (reprogram)

def pad1_3(): #geland in Amsterdam
    print("Jullie zijn geland in Amsterdam")




def pad2_0(): #voor jezelf gaan storyline (kortste en slechtste en 2 einde's)
    print("Je gaat voor jezelf en laat iedereen in de steek")
    print("Je rijd z.s.m naar plekken om alle benodige spullen op te halen")
    print("Voor de zekerheid bedenk je of je een wapen nodig hebt om mee te nemen")
    print("Neem je dat ook mee? \nA Ja \nB Nee") #6
    answer = input()
    if input == ("A"):
        print("Je pakt een pistool maar plotseling ontploft het in je gezicht!")
        print("Zou dit de karma zijn van je vrienden in de steek laten?")
        print("Ending: \n IDIOT ENDING") #1e einde (domme einde)
        (reprogram) #opnieuw starten met de game 
    elif input == 'B':
        print("Je hebt de wapen niet gepakt")
        print("Je gaat naar buiten in paniek en haast je om je spullen in de auto te doen")
        print("Je loopt naar je auto, het is koud en je bibbert van de kou")
        print("Je realiseert je dat je je sleutels bent vergeten")
        print("Je probeert snel terug te rennen maar je glijd uit")
        print("Je glijd uit en breekt je nek in 2 delen")
        print("Wat jammer, misschien kan je in het volgende leven een betere keuze maken")
        print("Einde: \n Idiot ending 2.0") #2e einde (ultra idioot hahahah) #geluid idee met negatief toontje
        (reprogram) #opnieuw starten met de game
    else: 
        try_again




def pad3_0(): #storyline met nationalisme ending (1 einde)
    ("Je neemt het in je eigen handen om alsnog je land te verdidgen")
    ("De Kroatische krijgsmacht roept naar je en het is je eer en kracht om te vechten voor je land")
    ("Je pakt je spullen en start de auto, onderweg naar de kazerne om jezelf aan te bieden als soldaat")
    ("Onderweg naar de Kazerne zie je soldaten langs lopen, doe je je raam omlaag en schreeuw je 'Viva la croatia!' of niet?")
    ("\nA Ja? \nB Nee?") #6
    answer = input()
    if input == ("A"):
        (pad3_1)
        print("Je schreeuwt met eer 'Viva la croatia!!!'")
        print("Moraal \n + 5") #misschien een idee om een geluidje hier te zetten
    elif input ==("B"):
        print("Toch maar niet")
        print("Miscchien later op de kazerne?")
        (pad3_1)
    else:
        try_again

pad1_1()
