# Cmpsc 132
# Summer 2020
# Final Lab
# Omer Canca

# Import modules
import Final_Math as math

def main():

    # Menu of programs
    print('\nChose an option to select from the list below:\n\t1 - Math Operations\n\t2 - Pythagreon Theorem\n\t3 - Quadratic Formula\n\t4 - Baseball Statistics\n\t5 - New Password\n\t6 - Exit')

    temp = input('> ')

    try:
        temp = int(temp)

    except ValueError:

        # Display Error, Restart
        print('\n** Input must be an integer **')
        main()

    if int(temp) > 6 or int(temp) <= 0:

        # Display Error, Restart
        print('\n** The selection is not an option **')
        main()

    if temp == 1:

        print('\n\t---------\tMath Operations')

        # Take input
        s = float(input('\nEnter a real number to perform basic math calculations. '))
        r = float(input('\nEnter a second real number to perform basic math calculations. '))

        # Call function
        math.calcMathOperations(s, r)

        # Restart
        print('\n\t---------')
        main()

    elif temp == 2:

        print('\n\t---------\tPythagreon Theorem')

        # Take input
        a = float(input('\nEnter a real number to perform the pythagorean thereom. '))
        b = float(input('\nEnter a second real number to perform the pythagorean thereom. '))

        # Call function
        math.calcPythagThm(a, b)

        # Restart
        print('\n\t---------')
        main()

    elif temp == 3:

        print('\n\t---------\tQuadratic Formula')
        print('\nThis program will produce two answers using the quadratic formula based off of user inputs')

        # Take input
        a = float(input('\nWhat is the value for a? '))
        b = float(input('\nWhat is the value for b? '))
        c = float(input('\nWhat is the value for c? '))

        # Call function
        math.calcQuadForm(a, b, c)

        # Restart
        print('\n\t---------')
        main()

    elif temp == 4:
        import Final_Stats as stats
        print('\n\t---------\tBaseball Stats')
        print('\nThis program will calculate baseball stats given a file name. ')

        # call function
        stats.calcBaseballStats

        # Restart
        print('\n\t---------')
        main()
    
    elif temp == 5: 
        import Final_NewPassword as password
        print('\n\t----------\tNew Password')
        print('\nThis program will help the user create a new password. ')

        password.createNewPassword

        # Restart
        print('\n\t---------')
        main()

# Call main
main()