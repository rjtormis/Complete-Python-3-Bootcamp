#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
import builtins

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(*args):
    cons = list(args)
    total = 0
    Bust = False
    for x in cons:
       if x != 11:
           total += x
           if total > 21:
               Bust = True
       elif x == 11:
           total += x -10
           if total > 21:
               Bust = True

    if Bust == True:
        print('BUST')
    else:
        print(total)
              
            
    
blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)