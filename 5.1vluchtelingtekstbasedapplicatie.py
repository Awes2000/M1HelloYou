#import
from re import L
from time import sleep
from defs import *
import defs 
from playsound import playsound 
#from defs import pad1_0, pad1_1 

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
    answer = input("Mijn stap is: \nA: Vrienden zoeken: \nB: Voor mezelf gaan \nC: Meedoen aan de oorlog\n") #2
    if answer =="A":
        pad1_0()
        doorgaan = True
    elif answer =="B":
        pad2_0()
        doorgaan = True
    elif answer=="C":
        pad3_0()
        doorgaan = True
    else:
        try_again
            
        
           

#main code 

print ("Laten we starten, wat is je naam?:")
sleep(2.0)
naam = input()
print ("Hallo! " + naam)
game()
    

    