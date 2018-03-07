def countPaycheck():
    value=-1

    while value<=0:

        try:
            hours=int(input('How many hours did you work? '))
            ##  Work on getting payrate to accept 12.00
            payrate=int(input('At what hourly wage? '))
            total=hours*payrate
            tax=total*.20
            afterTax=total-tax
            s='\nYou will make ${} this pay period before tax.\n\nAfter tax it will be around ${} give or take.'.format(total,afterTax)
            return s
            
        except(ValueError, TypeError):
            print('Enter an actual number.')
            value=-1
            


def salary():
    value=-1
    while value<0:
        try:
    
            salary=int(input('What do you normally expect a paycheck? '))
            bonus=(input('\nAny bonuses this month? (Yes or No) ')).lower()
            if bonus=='yes':
                bonusTotal=int(input('\nHow much? '))
                bonusByPaycheck=(bonusTotal/2)
                total=salary+bonusByPaycheck
                tax=(salary+bonusByPaycheck)*.25
                afterTax=total-tax
                return '\nYou can expect ${} before tax, ${} being taxed, and ${} after tax!'.format(total,tax,afterTax)
            elif bonus=='no':
                print('\nThat\'s too bad!')
                taxWithNoBonus=salary*.25
                totalNoBonus=salary-taxWithNoBonus
            return'\nYou can expect ${} this paycheck.'.format(totalNoBonus)
        except(ValueError, TypeError):
            print('Enter a whole number.')
            value=-1


            
def main(countPaycheck,salary):
    value=-1
    attempts=3
    while value<0:
        try:
            user=input('Who is using this? ').lower()
            validUserNames=['oj','oscar','bruce']
            validUserNames2=['lex','lexi','alexis','lex luthor']
            if user in validUserNames:
                return countPaycheck()
            if user in validUserNames2:
                return salary()
            else:
                s=('You are not authorized.\n\nYou have {} attempts left.'.format(attempts-1))
                attempts-=1
                print(s)
                if attempts==0:
                    return'Try again later'
        except(ValueError, TypeError):
            print('Enter a name, asshole.')
            value=-1

print(main(countPaycheck,salary))