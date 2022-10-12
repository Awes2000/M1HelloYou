#import
from re import L
from time import sleep

#function game code
def reprogram():
    restart = input ("Zou je opnieuw willen beginnen? JA of NEE: ")
    if restart == "JA": 
        game()
    elif restart == "NEE":
        exit()
    else:
        print("Voer een geldig antwoord in")
def game():
    wrong = 'Dat is niet het juiste antwoord.'
    try_again = 'Dit is geen geldig antwoord, voer een geldig antwoord in'
    rungame = 0
    while rungame == 0:
        print("Welkom in mijn vluchteling verhaal!")
        sleep(2.0)
        print("Dit verhaal gaat over een man die is ontsnapt uit voormalig Yugoslavie")
        sleep(2.0)
        print("Zijn doel is om een beter leven te leiden")
        sleep(2.0)
        print("Jij zal hem begeleiden in zijn verhaal om een betere toekomst te vinden")
        sleep(2.0)
        print("Er zijn 4 verschillende eindes dus kies maar wat je wilt!")
        sleep(2.0)
        print ("Je bent nu in Yugoslavie, het is onveilig en er onstaat een burgeroorlog...")
        sleep(2.0)
        print("Je bent een hardwerkende man een familie, je bent zorgzaam en doet altijd zijn best")
        sleep(2.0)
        print("Je bent teleurgesteld in je situatie maar je neemt nu de beslissing om verandering in te brengen")
        sleep (1.5)
        print("Wat is het eerste wat je gaat doen?")
        sleep(1.0)
        doorgaan = False
        while doorgaan == False:
            print ("Mijn stap is: \nA Pad 1.0 Vrienden zoeken: \nB Pad 2.0 Voor mezelf gaan \Pad 3.0 Meedoen aan de oorlog") #2
            answer1 = input(str("Antwoord: ")) 
            if answer1 == "A":
                print("Je gaat voor je vrienden zoeken..")
                sleep(2.5)
                print("Je gaat naar de hoofdstad met de auto")
                sleep(2.5)
                print("Je ziet je beste vriend Mido")
                print("Wat ga je doen? \nA Je laat hem binnen in je auto \nB Je zoekt nog rond") #4
                vriendenpad = input("Antwoord: ")
                if vriendenpad == "A":
                    print("Hij zit nu in je auto en jullie rijden verder")
                    sleep(2.5)
            elif answer1 == "B":
                print("Je gaat voor jezelf en laat iedereen in de steek")
                print("Je rijd z.s.m naar plekken om alle benodige spullen op te halen")
                print("Voor de zekerheid bedenk je of je een wapen nodig hebt om mee te nemen")
                print("Neem je dat ook mee? \nA Ja \nB Nee") #6
                pad2 = input()
                if pad2 ==("Ja"):
                    print("Je pakt een pistool maar plotseling ontploft het in je gezicht")
                    print("Zou dit de karma zijn van je vrienden in de steek laten?")
                    print("Ending: IDIOT ENDING") #1e einde (domme einde)
                    (reprogram)
                elif pad2 ==("Nee"):
                    print("Slimme keuze want je zou niet doorgelaten worden op het vliegeld!")
                else:
                    (reprogram)

            
                
            doorgaan = False     

            while doorgaan == False:
                print ("Je loopt door en ziet een kat die vast zit in de boom die miauwt om hulp!")
                sleep (2.0)
                print ("Ik: \n A Bel de dierenambulance \n B Ik klim zelf de boom in en red de kat \n C Ik laat de kat")
                answer2 = input("Antwoord: ")
                if answer2 == "A":
                    print ("De dierenambulance is gekomen en iedereen is blij.!")
                    sleep(2.5)
                    doorgaan = True
                elif answer2 == "B":
                    print("De kat is nu uit de boom maar jij bent gewond geraakt door het klimmem")
                    sleep (2.5)
                    print("Een goeie keuze, maar was er misschien niet een betere alternatief?")
                    sleep (2.5)
                    doorgaan = True
                elif answer2 == "C":
                    print ("Er loopt een opa langs en kijkt teleurstellend naar je...")
                    sleep(2.0)
                    print("Oude opa stem: KLOTE JONG! *waait zijn wandelstok naar je toe*")
                    sleep(2.5)
                    doorgaan = True
                else:
                    try_again
            
            doorgaan = False
            
            while doorgaan == False:
                print ("Je bent aan het einde van de park gekomen en een zwerver vraagt om een euro:")
                sleep (2.0)
                print (" \n A Ik geef de zwerver een euro \n B Ik negeer de zwerver \n C Ik zeg dat hij me met rust moet laten")
                answer3 = input ("Antwoord: ")
                if answer3 == "A":
                    print ("De zwerver is dankbaar, hij stelt zich voor en jij ook en je dag is beter")
                    sleep (2.5)
                    print("De zwerver heet John en jullie hebben een hart tot hart gesprek")
                    sleep (2.5)
                    print("Hij bedankt je nogmaals en zegt het volgende: Hartelijk bedankt",naam) 
                    sleep (2.0)
                    doorgaan = True
                elif answer3 == "B":
                    print ("Bruh")
                    doorgaan = True
                elif answer3 == "C": 
                    print ("Je schreeuwt hardop naar de zwerver om je met rust te laten")
                    sleep(2.0)
                    print("De zwerver bied zijn excuses aan en zegt dat hij geen geld had om te eten")
                    sleep(2.0)
                    print("Hij wenst je alsnog een fijne dag toe met een mooie glimach")
                    doorgaan = True
                else:
                    print(try_again)
            
            doorgaan = False

            while doorgaan == False:
                print("!")
                sleep(1.5)
                print("Het begint donker te worden")
                sleep (2.5)
                print("Je loopt onderweg naar huis")
                sleep(2.5)
                print("Je hoord een vrouw schreeuwen")
                sleep(1.5)
                print("Ze wordt beroofd!")
                print("Ik:"" \n A Help mee met beroven \n B Ik sla de dief k.o \n C Ik pak een baksteen en sla de dief neer")
                answer4 = input ("Antwoord: ")
                if answer4 == "A":
                    print("Jullie hebben haar beroofd maar de dief had haar neergestoken...")
                    sleep(2.0)
                    print("Er is een onderzoek gestart door de politie en je wordt gezocht!")
                    doorgaan = True
                elif answer4 == "B": 
                    print("De dief is K.O geslagen!")
                    sleep(2.0)
                    print("Hij ligt neer op de grond")
                    sleep(2.0)
                    print("De vrouw bedankt je voor het redden van haar")
                    sleep(2.0)
                    print("De politie is gebeld en gekomen en hebben de dief meegenomen")
                    sleep(2.0)
                    doorgaan = True
                elif answer4 == "C":
                    print("De dief is k.o geslagen")
                    sleep(2.0)
                    print("Je doel is bereikt, echter bloed hij nu dood")
                    sleep(2.0)
                    print("Je intenties waren correct maar misschien was er een altenatief methode")
                    sleep(2.0)
                    print("Je rent weg")
                    doorgaan = True
                else:
                    print(try_again)

            doorgaan = False  

        while doorgaan == False:
            print ("Je bent onderweg naar flat laat in de avond en probeert je deur te openen")
            sleep (1.5)
            print("Het lukt niet, wat ga je doen?\n A Je buurman bellen \n B De deur slopen \n C Klimmen")
            answer5 = input ("Antwoord: ")
            if answer5 == "A":
                print("Je buurman neemt op en doet de deur open. Je bedankt hem en gaat z.s.m naar boven en naar bed toe")
                
                
            
                reprogram()
            elif answer5 == "B":
                print("De deur is gesloopt maar ondertussen is iedereen wakker gemaakt")
                sleep(2.0)
                
              
                reprogram()
            elif answer5 == "C":
                print("Het is gelukt maar je hebt wel een aantal bloempotten ondertussen gesloopt van je liefe oude buurvrouw")
                sleep(2.0)
            
                reprogram()
            else:
                print(try_again)
                print("Dankjewel voor het deelnemen van mijn Quiz!")
                reprogram()


#main code 

print ("Laten we starten, wat is je naam?:")
sleep(2.0)
naam = input()
print ("Hallo! " + naam)
game()
    

    