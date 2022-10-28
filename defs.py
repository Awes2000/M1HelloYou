
koevoet = 0
antwoord = ['Yes', 'Y', 'y', 'yes', 'YES', 'n' 'No', 'NO']
moraal = 0
try_again = 'Dit is geen geldig antwoord, voer een geldig antwoord in'
from time import sleep
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
     
     answer = input("\nA: Ja \nB: Nee\n") #2

     if answer == "A": #naar binnen gaan pad 
        pad1_1()
     elif answer == "B": #niet naar binnen gaan pad
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
    "Het is erg stil\n"
    "Het lijkt wel alsof iedereen weg is\n"
    "Je loopt langs een huis die je herkent\n")
    answer = input("Ga je naar binnen?\nA: Ja\nB: Nee\n")
    if answer =="A":
        print("Je besluit om naar binnen te gaan")
        print("Maar plots..")
        print("BOOOOOMMMM!!")
        print("Helaas, in het huis was een boobytrap")
        print("Einde: Killed by boobytrap.")
    elif answer =="B":
        print("Je besluit om niet naar binnen te gaan")
        print("Je loopt rond en plots...")
        print("Boooom!, er valt een UFO op je vanuit de lucht")
        print("Uit de UFO stapt een Alien uit")
        print("Terwijl je dood gaat aan je verwondingen zegt de Alien:")
        print("Ik ben van de toekomst, dit is niet het juiste pad dat je had moeten kiezen!")
    else:
        print(try_again)



def pad_Dubrovnik(): #je gaat naar Dubrovnik
    print("Je bent in Dubrovnik aangekomen")
    print("Een prachtige stad met mooie gebouwen")
    print("Helaas is het leeg en verlaten")
    print("Je ziet families door hun ramen heen kijken in angst terwijl je langsloopt")
    print("Terwijl je loopt, roept een kind naar je om te komen")
    answer = input("Kom je?\nA: Ja \nB: Nee")
    if answer =="A":
        print("Je gaat met de kind mee")
        print("De kind loopt een steegje in en je verliest zich van hem")
        print("Het was een val!")
        print("3 soldaten tonen zich tevoorschijn en schieten je dood")
        print("Einde: Killed by a kid (lol)")
    elif answer =="B":
        print("Je besluit niet om met de kind mee te gaan")
        print("De kind begint te huilen")
        print("Je neemt een stap dichterbij en probeert de kind te troosten")
        print("De kind wordt boos en tranformeerd in de hulk?!")
        print("Hij slaat je met 1 mep dood")
        print("Einde: Killed by the hulk")
    else:
        print(try_again)
    

def pad1_1(): #naar binnen gaan pad #2
    print("Je besluit om naar binnen te gaan")
    print("De soldaten zijn eventjes afgeleid en je neemt de kans")
    print("Onderweg naar het huis zie je een koevoet op de grond naast het gras bij de ingang")
    print("Neem je de koevoet mee?")
    
    answer = input("\nA: Ja \nB: Nee\n") #4
    if answer == "A":
        print("Je hebt de koevoet opgepakt") 
        playsound('crowbar.mp3')
        koevoet =+ 1
    elif answer == "B":
        print("Je hebt de koevoet niet opgepakt")
        koevoet =- 0
    else:
       print(try_again)

    print("Je komt aan bij je vrienden zn deur, het stond op een kiertje open")
    print("Hopelijk zijn ze oke")
    print("Je loopt voorzichtig door het huis door en roept voor je vrienden, \n'Oleg, Sasha!, waar zijn jullie??'")
    print("Je raakt bezorgt en ziet in je ooghoek een gleufje met licht")
    print("Je loopt erop af en kijkt door het licht")
    print("Je ziet een mooie blonde dame aan de andere kant zitten in angst, zij heeft geen idee dat je haar kan zien")
    print("Je roept naar haar toe en ze ziet je kijken, ze glimlacht en is blij om je de zien")
    print("Hey, ik ben zo blij om je te zien!") #naam is de userinput in t begin van de game
    print("Sasha zit vast en heeft je hulp nodig")

    if koevoet == 1:
        print("Je gebruikt de koevoet en Sasha is vrijgekomen")
        pad1_2() #pad 1_2 voor als Sasha vrijkomt

    elif koevoet == 0:
            print("Je hebt geen tools om Sasha te bevrijden")
            (pad1_02) #pad 1_02 Sasha is niet bevrijd
    else:
        print(try_again)

def pad1_02(): #Sasha is NIET BEVRIJD
    print("Je hebt geen tools om Sasha te bevrijden")
    print("Je probeert in te breken door je handen en voeten te gebruiken maar het lukt niet")
    print("De soldaten horen geluid van het huis komen")
    print("Je moet helaas Sasha in de steek laten")

def pad1_2(): #Sasha is vrij en jullie gaan naar het vliegveld
    print("Sasha is je zo dankbaar voor het bevrijden van haar")
    sleep(1.0)
    print("Jullie zijn allebei blij dat jullie elkaar zien")
    sleep(1.0)
    print("Sasha: Oleg... hij is-")
    sleep(1.0)
    print(" Ja I know")
    sleep(1.0)
    print("Kom, pak al je spullen! We moeten snel weg!")
    sleep(1.0)
    print("Jullie pakken alles wat jullie nodig hebben")
    sleep(1.0)
    print("De auto staat buiten klaar en jullie glippen beide weg")
    sleep(1.0)
    print("Je rijdt snel naar het vliegveld toe")
    sleep(4.0)
    print("Jullie komen aan")
    print("Dankzij jouw connecties krijgen jullie prioriteit en kunnen jullie snel vluchten")
    print("Jullie zitten naast elkaar in de vliegtuig en troosten elkaar")
    print("De stewardesse komt langs om te vragen wat jullie willen drinken")
    print("Stewardesse: Wat willen jullie drinken?")
    answer = input("\nA: Cola \nB: Water \nC: Niks\n") #(7)
    if answer =="A":
        print("Ahh, lekker!!..") #bubbly sound
        playsound('water.mp3')
        sleep(4.0)
        pad1_3()
    elif answer =="B":
        print("Ahhh, verfrissend") #water sound
        playsound('water.mp3')
        pad1_4()
    elif answer =="C":
        print("Toch maar niet..")
        print("Te veel aan m'n hoofd")
        print("Loading schiphol scene..")
        sleep(4.0)
        pad1_5()
    else:
        (try_again)

def pad1_3():#buikbijn door Cola, overgeven #4
    print("Je bent een beetje misselijk geworden door de cola en je gaat naar de wc")
    print("Je moet overgeven en je voelt je beter")
    answer = input("Spoel je door?, \nA: Ja \nB: Nee\n")
    if answer =="A":
        print("Goed opgevoed")
        print("Loading schiphol scene..")
        sleep(4.0)
        pad1_5()
    elif answer =="B":
        print("Slecht opgevoed")
        print("Loading schiphol scene..")
        sleep(4.0)
        pad1_5()
    else:
        (try_again)




def pad1_4(): #plassen door water #5
    print("Je moest naar de wc door zoveel water te drinken")
    answer = input("Spoel je door?, \nA: Ja \nB: Nee ")
    if answer =="A":
        print("Goed opgevoed")
        print("Loading schiphol scene..")
        sleep(4.0)
        pad1_5()
    elif answer =="B":
        print("Slecht opgevoed")
        print("Loading schiphol scene..")
        sleep(4.0)
        pad1_5()
    else:
        print(try_again)


def pad1_5(): #geland in Amsterdam met Sasha.
    print("De vliegtuig land")
    print("Jullie pakken je spullen, tijd om een toekomst te starten")
    print("Waar in Amsterdam ga je eerst heen?")
    answer = input("\nA: Amsterdam-Noord\nB: Amsterdam-Oost\n")
    if answer =="A":
      print("Loading Amsterdam-Noord")
      sleep(2.0)
      pad_amsterdam_noord()
    elif answer =="B":
        print("Je bent in Amsterdam-Oost aangekomen")
        pad_amsterdam_oost()
    else:
        print(try_again)

def pad_amsterdam_noord(): #amsterdam noord
    print("Je bent in Amsterdam-Noord aangekomen met Sasha")
    print("Een goeie vriend van jullie die Erik heet woont in Amsterdam-Noord")
    print("Jullie gaan naar hem toe om hem te zien en te spreken")
    print("Jullie komen aan en praten over je situatie, Erik bied je werk en voorlopige huisvesting aan")
    answer = input("Erik: Welke baan zou je willen hebben?, \nA: Timmerman \nB: Loodgieter")
    if answer =="A":
      print("Je kiest om een loodgieter te worden")
      print("1 jaar later..")
      print("Je hebt eindelijk heel veel geld dat je hebt gespaard")
      print("De Nederlandse overheid is gunstig en bied jij en Sasha huisvesting")
      print("Jullie hebben de gelegenheid om een huis te kiezen, wat voor soort huis wil je")
      answer2 = input("\nA: Rijtjeshuis \nB: Villa\n")
      if answer2 =="A":
        print("Loading Rijtjeshuis story....")
        sleep(3.5)
        pad_rijtjeshuis()

      elif answer2 =="B":
        print("Loading Villa...")
        sleep(3.5)
        pad_villa()

def pad_amsterdam_oost(): #amsterdam oost
    print("Je bent in Amsterdam-Oost aangekomen met Sasha")
    print("Een goeie vriend van jullie die Erik heet woont in Amsterdam-Noord")
    print("Jullie gaan naar hem toe om hem te zien en te spreken")
    print("Jullie komen aan en praten over je situatie, Erik bied je werk en voorlopige huisvesting aan")
    answer = input("Erik: Welke baan zou je willen hebben?\nA: Loodgieter \nB: Timmerman\n")
    if answer =="A":
      print("Je kiest om een loodgieter te worden")
      print("1 jaar later..")
      sleep(3.0)
      print("Je hebt eindelijk heel veel geld dat je hebt gespaard")
      print("De Nederlandse overheid is gunstig en bied jij en Sasha huisvesting")
      print("Jullie hebben de gelegenheid om een huis te kiezen, wat voor soort huis wil je")
      answer2 = input("\nA: Rijtjeshuis \nB: Villa\n")
      if answer2 =="A":
        print("Loading Rijtjeshuis story....")
        sleep(3.5)
        pad_rijtjeshuis()

      elif answer2 =="B":
        print("Loading Villa")
        sleep(3.5)
        pad_villa()



    elif answer =="B":
      print("Je kiest om een timmerman te worden")
      sleep(2.0)
      print("1 jaar later...")
      sleep(3.0)
      print("Je hebt eindelijk heel veel geld dat je hebt gespaard")
      print("De Nederlandse overheid is gunstig en bied jij en Sasha huisvesting")
      print("Jullie hebben de gelegenheid om een huis te kiezen, wat voor soort huis wil je")
      answer2 = input("\nA: Rijtjeshuis \nB: Villa\n")
      if answer2 =="A":
        print("Loading Rijtjeshuis story....")
        sleep(3.5)
        pad_rijtjeshuis()

      elif answer2 =="B":
        print("Loading Villa")
        pad_villa()

def pad_rijtjeshuis(): #rijtjeshuiss
    print("Eindelijk, jullie hebben je eigen huis!")
    print("Na zoveel tijd samen besteed te hebben is er een emotionele connectie ontstaan")
    print("Jij en Sasha zijn verliefd geworden en besluiten om een betere toekomst te hebben")
    print("Een toekomst is beter met kinderen")
    answer = input("Hoeveel kinderen wil je met Sasha hebben?\nA: 1 \nB: 2 \nC: Zo veel mogelijK!!")
    if answer =="A":
     print("Jullie besluiten om 1 kind te nemen")
     babynaam = input("Het is een jongen en hij wordt geboren, hoe wil je hem noemem?")
     print(babynaam, "Wat een mooie naam!")
     sleep(2.0)
     print(" 10 jaar later...")
     sleep(4.0)
     print("Een hele mooie toekomst")
     print("Wauw" + babynaam, "is erg opgegroeid")
     print("Jij en Sasha zijn dolgelukkig samen en een betere toekomst kon je niet wensen")
     print("Einde laden...")
     sleep(4.0)
     print("Gefeliciteerd, je hebt de liefdes einde bereikt met 1 kind")
    elif answer =="B":
        print("Jullie besluiten om 2 kinderen te nemen")
        print("Het wordt een tweeling! 2 jongens!")
        babynaam2 = input("Hoe wil je je 1e kind noemen?")
        print(babynaam2, "Prachtige naam!")
        babynaam3 = input("En je 2e zoon?")
        print(babynaam3, "Ook een prachtige naam!")
        sleep(2.0)
        print("10 jaar later....")
        sleep(4.0)
        print("Wat een mooie toekomst!")
        print(babynaam2, + babynaam3, "Hebben een geweldige toekomst!")
        print(babynaam2,"Houd zich voornamelijk bezig met coderen in scrap en", babynaam3, "houd zich bezig met schilderen en tekenen")
        print("Jij en Sasha zijn dolgelukkig samen en een betere toekomst kon je niet wensen")
        print("Einde laden...")
        sleep(4.0)
        print("Gefeliciteerd, je hebt de liefdes einde bereikt met 2 kinderen!")
    elif answer =="C":
        print("Jullie besluiten om zoveel kinderen te maken")
        print("Op een of andere manier gaat het mis..")
        print("Door een speciale aandoening kan Sasha elke uur een kind baren zonder problemen")
        print("Sasha baard ongeveer 7000 kinderen per jaar")
        print("10 jaar later..")
        sleep(4.0)
        print("De wereld is overgenomen door jullie kinderen, jullie hebben te veel kinderen gemaakt!!")
    else:
      print(try_again)


        
     
      


def pad_villa(): #pad villlaaaa
    print("Eindelijk, jullie hebben je eigen huis!")
    print("Na zoveel tijd samen besteed te hebben is er een emotionele connectie ontstaan")
    print("Jij en Sasha zijn verliefd geworden en besluiten om een betere toekomst te hebben")
    print("Een toekomst is beter met kinderen")
    answer = input("Hoeveel kinderen wil je met Sasha hebben?\nA: 1 \nB: 2 \nC: Zo veel mogelijK!!")
    if answer =="A":
     print("Jullie besluiten om 1 kind te nemen")
     babynaam = input("Het is een jongen en hij wordt geboren, hoe wil je hem noemem?")
     print(babynaam, "Wat een mooie naam!")
     sleep(2.0)
     print(" 10 jaar later...")
     sleep(4.0)
     print("Een hele mooie toekomst")
     print("Wauw" + babynaam, "is erg opgegroeid")
     print("Jij en Sasha zijn dolgelukkig samen en een betere toekomst kon je niet wensen")
     print("Einde laden...")
     sleep(4.0)
     print("Gefeliciteerd, je hebt de liefdes einde bereikt met 1 kind")
    elif answer =="B":
        print("Jullie besluiten om 2 kinderen te nemen")
        print("Het wordt een tweeling! 2 jongens!")
        babynaam2 = input("Hoe wil je je 1e kind noemen?")
        print(babynaam2, "Prachtige naam!")
        babynaam3 = input("En je 2e zoon?")
        print(babynaam3, "Ook een prachtige naam!")
        sleep(2.0)
        print("10 jaar later....")
        sleep(4.0)
        print("Wat een mooie toekomst!")
        print(babynaam2, + babynaam3, "Hebben een geweldige toekomst!")
        print(babynaam2,"Houd zich voornamelijk bezig met coderen in scrap en", babynaam3, "houd zich bezig met schilderen en tekenen")
        print("Jij en Sasha zijn dolgelukkig samen en een betere toekomst kon je niet wensen")
        print("Einde laden...")
        sleep(4.0)
        print("Gefeliciteerd, je hebt de liefdes einde bereikt met 2 kinderen!")
    elif answer =="C":
        print("Jullie besluiten om zoveel kinderen te maken")
        print("Op een of andere manier gaat het mis..")
        print("Door een speciale aandoening kan Sasha elke uur een kind baren zonder problemen")
        print("Sasha baard ongeveer 7000 kinderen per jaar")
        print("10 jaar later..")
        sleep(4.0)
        print("De wereld is overgenomen door jullie kinderen, jullie hebben te veel kinderen gemaakt!!")
    else:
      print(try_again) 







     






def pad2_0(): #voor jezelf gaan storyline (kortste en slechtste en 2 einde's) #6
    print("Je gaat voor jezelf en laat iedereen in de steek")
    print("Je rijd z.s.m naar plekken om alle benodige spullen op te halen")
    print("Voor de zekerheid bedenk je of je een wapen nodig hebt om mee te nemen")
    print("Neem je dat ook mee? \nA Ja \nB Nee") #9
    answer = input()
    if answer == "A":
        print("Je pakt een pistool maar plotseling ontploft het in je gezicht!")
        print("Zou dit de karma zijn van je vrienden in de steek laten?")
        print("Ending: \n IDIOT ENDING") #1e einde (domme einde)
         #opnieuw starten met de game 
    elif answer == "B":
        print("Je hebt de wapen niet gepakt")
        print("Je gaat naar buiten in paniek en haast je om je spullen in de auto te doen")
        print("Je loopt naar je auto, het is koud en je bibbert van de kou")
        print("Je realiseert je dat je je sleutels bent vergeten")
        print("Je probeert snel terug te rennen maar je glijd uit")
        print("Je glijd uit en breekt je nek in 2 delen")
        print("Wat jammer, misschien kan je in het volgende leven een betere keuze maken")
        print("Einde: \n Idiot ending 2.0") #2e einde (ultra idioot hahahah) #geluid idee met negatief toontje
         #opnieuw starten met de game
    else: 
        print(try_again)




def pad3_0(): #storyline met nationalisme ending (2 einde's) #7
    print("Je neemt het in je eigen handen om alsnog je land te verdidgen")
    print("De Kroatische krijgsmacht roept naar je en het is je eer en kracht om te vechten voor je land")
    print("Je pakt je spullen en start de auto, onderweg naar de kazerne om jezelf aan te bieden als soldaat")
    print("Onderweg naar de Kazerne zie je soldaten langs lopen, doe je je raam omlaag en schreeuw je 'Viva la croatia!' of niet?")
    print("\nA Ja? \nB Nee?") #11
    answer = input()
    if answer == "A":
        print("Je schreeuwt met eer 'Viva la croatia!!!'")
        moraal +5
        print("Je moraal is omhoog")
        pad3_01()
    elif answer =="B":
        print("Toch maar niet")
        pad3_1() #pad met einde dat jullie niet winnen en moraal laag is
    else:
        print(try_again)

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
        print(try_again)

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
    else:
        print(try_again)

def pad3_03(): #oorlog gewonnen!! 10#
    print("Het was een lange gevecht...")
    print("Op een of andere andere manier hebben jullie gewonnen")
    print("Je bent trots..")
    print("Vele kameraden waren verloren")
    print("Je kijkt om je heen in verdriet maar je bent blijk dat je hebt gewonnen")
    print("De burgeroolog is over en je kan eindelijk naar huis gaan")
    print("Jammer genoeg is Yugoslavie nu verdeeld in verschillende soorten landen")
    print("Maar je hebt hard gestreden voor je land en behoud je eer")
    #einde

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
        print(try_again)

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
    "Hij pakt z'n gun en zet het op je hoofd en zegt: 'Asta la vista, baby'\n" #gunshot, slechte einde
    "Einde: Terminated")
    
     
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

