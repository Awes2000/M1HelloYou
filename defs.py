
koevoet = 0
antwoord = ['Yes', 'Y', 'y', 'yes', 'YES', 'n' 'No', 'NO']
moraal = 0
try_again = 'Dit is geen geldig antwoord, voer een geldig antwoord in'
from playsound import playsound 
    


def pad1_0(): #vrienden zoeken pad langste storyline met beste einde 1#
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
     
     answer = input("\nA: Ja \nB: Nee") #2

     if answer == ("A"): #naar binnen gaan pad 
        pad1_1()
     elif answer == ("B"): #niet naar binnen gaan pad
        pad1_01()
     else:
        print(try_again)

def pad1_01(): #niet naar binnen gaan pad
    print("Je besluit om niet naar binnen te gaan")
    print("Je loopt terug naar je auto")
    print("Je stapt je auto in")
    answer = input("Waar ga je heen?\n:A Pula \nB: Dubrovnik\n")
    if answer =="A":
        print("Je rijdt naar Pula...") #auto geluid
        pad_pula()
    elif answer =="B":
        print("Je gaat naar Dubrovnik") #auto geluid
        pad_Dubrovnik()
    else:
        print(try_again)
    
def pad_pula(): #je gaat naar Pula
    print("Je bent in Pula aangekomen\n"
    "Het is erg stil\n")



def pad_Dubrovnik(): #je gaat naar Dubrovnik
    print("Je bent in Dubrovnik aangekomen")
    

def pad1_1(): #naar binnen gaan pad #2
    print("Je besluit om naar binnen te gaan")
    print("De soldaten zijn eventjes afgeleid en je neemt de kans")
    print("Onderweg naar het huis zie je een koevoet op de grond naas het gras bij de ingang")
    print("Neem je de koevoet mee?")
    
    answer = input("\nJa: \nNee:") #4
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
        pad1_2() #pad 1_2 voor als Sasha vrijkomt

    elif koevoet == 0:
            print("Je hebt geen tools om Sasha te bevrijden")
            (pad1_02) #pad 1_02 Sasha is niet bevrijd
    else:
        (try_again)

def pad1_2(): #Sasha is vrij en jullie gaan naar het vliegveld
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
    answer = input("\nA:Cola, \nB: Water \nC: Niks") #(7)
    if answer =="A":
        print("Ahh, bubblyyyy") #bubbly sound
        pad1_3()
    elif answer =="B":
        print("Ahhh, verfrissend") #water sound
        pad1_4()
    elif answer =="C":
        print("Toch maar niet..")
        print("Te veel aan m'n hoofd")
        pad1_5()
    else:
        (try_again)

def pad1_3():#buikbijn door Cola, overgeven #4
    print("Je bent een beetje misselijk geworden door de cola en je gaat naar de wc")
    print("Je moet overgeven en je voelt je beter")
    answer = input("Spoel je door?, \nJa: \nNee: ")
    if input =="Ja":
        print("Goed opgevoed")
        pad1_5()
    elif input =="Nee":
        print("Slecht opgevoed")
        pad1_5()
    else:
        (try_again)




def pad1_4(): #plassen door water #5
    print("Je moest naar de wc door zoveel water te drinken")
    answer = input("Spoel je door?, \nJa: \nNee: ")
    if input =="Ja":
        print("Goed opgevoed")
        pad1_5()
    elif input =="Nee":
        pad1_5()
        print("Slecht opgevoed")
    else:
        (try_again)


def pad1_5(): #geland in Amsterdam met Sasha, nog aan werke
    print("De vliegtuig land")
    print("Jullie pakken je spullen maken zich klaar voor vertrek naar Amsterdam")






def pad2_0(): #voor jezelf gaan storyline (kortste en slechtste en 2 einde's) #6
    print("Je gaat voor jezelf en laat iedereen in de steek")
    print("Je rijd z.s.m naar plekken om alle benodige spullen op te halen")
    print("Voor de zekerheid bedenk je of je een wapen nodig hebt om mee te nemen")
    print("Neem je dat ook mee? \nA Ja \nB Nee") #9
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




def pad3_0(): #storyline met nationalisme ending (2 einde's) #7
    ("Je neemt het in je eigen handen om alsnog je land te verdidgen")
    ("De Kroatische krijgsmacht roept naar je en het is je eer en kracht om te vechten voor je land")
    ("Je pakt je spullen en start de auto, onderweg naar de kazerne om jezelf aan te bieden als soldaat")
    ("Onderweg naar de Kazerne zie je soldaten langs lopen, doe je je raam omlaag en schreeuw je 'Viva la croatia!' of niet?")
    ("\nA Ja? \nB Nee?") #11
    answer = input()
    if input == ("A"):
        print("Je schreeuwt met eer 'Viva la croatia!!!'")
        moraal +5
        print("Je moraal is omhoog")
        pad3_01()
    elif input ==("B"):
        print("Toch maar niet")
        pad3_1() #pad met einde dat jullie niet winnen en moraal laag is
    else:
        try_again

def pad3_01(): #op kazerne met hoog moraal #8
    print("Je komt op de kazerne met hoog moraal")
    print("Jullie verzamelen zich op de campus")
    print("Je geeft je mede-soldaten goed moraal")
    print("Iedereen voelt zich goed")
    print("Tijd om een wapen te kiezen")
    answer = input ("Welke wapen kies je? \nA: M4A1 \n:B M36TAR")
    if answer =="A":
     print("Je hebt de M4A1 gepakt")
     print("Tijd om te gaan")
     pad3_02()
    elif answer =="B":
     print("Je hebt de M36TAR gepakt")
     print("Tijd om te gaan")
     pad3_02()
    else:
        (try_again)

def pad3_02(): #we gaan voor battle (je moraal is hoog btw) #9
    print("Jullie marsen met de grootste leger die jullie ooit hebben gezien")
    print("De commandant selecteerd je als leider, je had goeie feedback door je mede-soldaten")
    print("De tegenstander ziet je op het veld")
    print("De tijd is gekomen om te vechten")
    answer = input("Houd je een speech of ga je direct naar battle? \nA: Battle \nB: Speech")
    if answer=="A":
        print("Je houd je speech:")
        print("Lets kill some noobs")
        print("Het was de beste speech ooit en iedereen is gemotiveerd")
        print("Je leger stormt het veld op en schreeuwt: 'Viva la croatia!!!'")
        pad3_03()
    elif answer=="B":
        print("Je gaat gelijk het veld in")
        print("Een speech is niet nodig")
        print("Je leger achter je ziet je moed en inspirerende gedrevenheid om te vechten voor je laten")
        print("Je leger stormt het veld op en schreeuwt: 'Viva la croatia!!!'")
        pad3_03()

def pad3_03(): #oorlog gewonnen!! 10#
    print("Het was een lange gevecht...")
    print("Op een of andere andere manier hebben jullie gewonnen")
    print("Je bent trots..")
    print("Vele kameraden waren verloren")
    print("Je kijkt om je heen in verdriet maar je bent blijk dat je hebt gewonnen")
    print("De burgeroolog is over en je kan eindelijk naar huis gaan")
    print("Jammer genoeg is Yugoslavie nu verdeeld in verschillende soorten landen")
    print("Maar je hebt hard gestreden voor je land en behoud je eer")
    (reprogram)

def pad3_1(): #11 #niet juichen
    print("Je besluit om toch niet te juichen")
    print("Op een of andere manier is je moraal laag")
    print("Je komt op de kazerne en verzamelt je met je mede-soldaten")
    print("De commandant geeft je een bevel om een wapen te kiezen")
    answer = input("Wat kies je? \nA: M4A1 \nB: Banaan")
    if answer =="A":
     print("Je hebt een M4A1 gekozen")
     print("Tijd om de veld op te gaan!")
     pad3_2() #m4a1 pad
    elif answer =="B":
     print("Je hebt een banaan gekozen")
     print("De commandant kijkt je raar aan")
     print("Tijd om de veld op te gaan!")
     pad3_banaan() #banaan pad en secret ending
    else:
        (try_again)

def pad3_2(): #13 #Arnold schiet je dood (ending)
    print("Je bent aan het marsen met je kameraden door een grote berg heen\n"
    "Dit is de grootste leger die je ooit hebt gezien\n"
    "Helaas is je moraal laag en je kan niemand aanmoedingen\n"
    "In de verte zie je de Amerikaanse leger die zicht bemoeien met de burgeroolog\n"
    "Had je maar iets motiverend te zeggen op dit moment tegen je kameraden\n"
    "Jullie vechten maar verliezen heel hard\n"
    "Je bent de enige over die nog leeft"
    "Je ligt op de grond neer met kogelwnden in je lichaam en je bent op t rand om dood te gaan\n"
    "Een van je vijanden loopt naar je af om je af te maken\n"
    "Het is Arnold Schwarzenegger\n"
    "Hij pakt z'n gun en zet het op je hoofd en zegt: 'Asta la vista, baby'\n") #gunshot, slechte einde
    (reprogram)
     
def pad3_banaan(): #14 #Banaan
    print("Je bent voorbereid met je banaan als wapenIedereen kijkt je raar aan maar jij hebt een diepere vertrouwen in je keuze. \n "
    "Wat is er speciaal aan deze banaan?\n"
    "Jullie marsen door en je ziet de vijand, het is de Amerikaanse leger\n"
    "Je stapt naar voren toe en zegt: 'Jongens, laat dit maar aan mij over'\n"
    "Je peeled je banaan wapen en er komt een gun uit\n"
    "Je drukt de knop in op je banaan gun en er vliegt een kogel naar de verte\n"
    "De kogel land en explodeert in een atoombom\n"
    "Iedereen kijkt in shock\n")
    pad3_03()

