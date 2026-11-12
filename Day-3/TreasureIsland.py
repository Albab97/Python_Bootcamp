# Cool ascii art from https://ascii.co.uk/art
print('''
            .--------------------------------------------.
           ( DO YOU KNOW HOW HARD IT IS TO DRAW AN OKAPI? )
          //'--------------------------------------------'
         /      , _.-~~-.__            __.,----.
      (';    __( )         ~~~'--..--~~         '.
(    . \"..-'  ')|                     .       \  '.
 \\. |\.'                    ;       .  ;       ;   ;
  \ \'"   /9)                 '       .  ;           ;
   ; )           )    (        '       .  ;     '    .
    )    _  __.-'-._   ;       '       . ,     /\    ;
    '-'"'--'      ; "-. '.    '            _.-(  ".  (
                  ;    \,)    )--,..----';'    >  ;   .
                   \   ( |   /           (    /   .   ;
     ,   ,          )  | ; .(      .    , )  /     \  ;
,;'-PjP;.';.-.;._,;/;,;)/;.;.);.;,,;,;,,;/;;,),;.,/,;.).,;,

''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
decision1 = input("You are at a cross road. Where you want to go?\nType 'left' or 'right'.").lower()
if decision1=="left":
    print("You have come to a lake. There is an island in the middle of the lake.")
    decision2 = input("Type 'wait' to wait for boat. Type 'swim' to swim across.").lower()
    if decision2=="wait":
        print("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        decision3 = input("Which color do you choose? ").lower()
        if decision3=="red":
            print("Burned by fire! Game Over.")
        elif decision3=="yellow":
            print("You Win!")
        elif decision3=="blue":
            print("Eaten by beast. Game Over.")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game over.")

else:
    print("Fall into a hole. Game over.")


