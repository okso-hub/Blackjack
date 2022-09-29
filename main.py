from os import system, name
from time import sleep
from random import choice
from termcolor import colored
from simple_term_menu import TerminalMenu


clear = lambda: system("clear") if name == "posix" else "cls"

J = 10
Q = 10
K = 10
A = "Baustelle"




def main():
    clear()

    all_cards = [2, 2, 2, 2,
          3, 3, 3, 3,
          4, 4, 4, 4,
          5, 5, 5, 5,
          6, 6, 6, 6,
          7, 7, 7, 7,
          8, 8, 8, 8,
          9, 9, 9, 9,
          10, 10, 10, 10,
          J, J, J, J, 
          Q, Q, Q, Q,
          K, K, K, K]

    player_cards = []

    dealer_cards = []


    def get_card(player):
        sleep(1.5)
        new_card = choice(all_cards)
        player.append(new_card)
        all_cards.remove(new_card)
        sleep(1.5)

    
    def get_dealer_card():
        sleep(1.5)
        while sum(dealer_cards) < 17:
            new_dealer = choice(all_cards)
            dealer_cards.append(new_dealer)
            all_cards.remove(new_dealer)
            print(f"Dealer: {dealer_cards}, {sum(dealer_cards)}")

        sleep(1.5)


    def consider_win(win, draw, lose):
        sleep(1.5)

        with open("cash", "r") as f:
            money = int(f.read())

        if win:
            money += (stake)
            newMoney = str(money)
            
            with open("cash", "w") as f:
                f.write(newMoney)

            print(colored(f'You won ${stake}!', "green", attrs=["bold"]))
            print(f"Your new balance is: ${newMoney}")

        elif draw:
            newMoney = str(money)

            with open("cash", "w") as f:
                f.write(newMoney)

            print(colored(f"You get your ${stake} back.", "yellow", attrs=["bold"]))
            print(f"Your new balance is: ${newMoney}")

        elif lose:
            money -= stake
            if money <= 0:
                print(colored(f"You lost ${stake}!", "red", attrs=["bold"]))
                print("No money left. Rebuy:")

                buyIn = str(input("Buy-In: $"))

                with open("cash", "w") as f:
                        f.write(buyIn)
            else:
                newMoney = str(money)
                with open("cash", "w") as f:
                        f.write(newMoney)
                print(colored(f"You lost ${stake}!", "red", attrs=["bold"]))
                print(f"Your new balance is: ${newMoney}")

    
    def stand():
        print(f"Dealer: {dealer_cards} {sum(dealer_cards)}")

        get_dealer_card()
        
        if sum(dealer_cards) > 21:
            print("You:", player_cards, sum(player_cards))
            print(colored("The dealer is above 21. You Win!", "green"))
            win = True
            consider_win(win=True, draw=False, lose=False)
            input("\nEnter to restart ")
            main()

        if sum(dealer_cards) <= 21:
            if sum(dealer_cards) > sum(player_cards):
                    print("You:", player_cards, sum(player_cards))
                    print(colored("The Dealer is above you!, YOU LOST", "red"))
                    lose = True
                    consider_win(win=False, draw=False, lose=True)
                    input("\nEnter to restart ")
                    main()

            elif sum(dealer_cards) < sum(player_cards):
                    print("You:", player_cards, sum(player_cards))
                    print(colored("The Dealer is below you!, YOU WIN", "green"))
                    win = True
                    consider_win(win, draw=False, lose=False)
                    input("\nEnter to restart ")
                    main()

            elif sum(dealer_cards) == sum(player_cards):
                    print("Dealer:", dealer_cards, sum(dealer_cards), "\nYou:", player_cards, sum(player_cards))
                    print(f"Dealer:, {dealer_cards} {sum(dealer_cards)} \nYou: {player_cards} {sum(player_cards)}")
                    print(colored("Draw. Nobody won!", "yellow"))
                    draw = True
                    consider_win(win=False, draw=True, lose=False)
                    input("\nEnter to restart ")
                    main()


    def hit():
        get_card(player_cards)
        print("You:", player_cards, sum(player_cards))
        
        if sum(player_cards) == 21:
            if sum(dealer_cards) != 21:
                    win = True
                    print("Dealer:", dealer_cards, sum(dealer_cards))
                    consider_win(win=True, draw=False, lose=False)
            elif sum(dealer_cards) == sum(player_cards):
                    draw = True
                    print("Dealer:", dealer_cards, sum(dealer_cards))
                    consider_win(win=False, draw=True, lose=False)

            input("\nEnter to restart ")
            main()

        elif sum(player_cards) > 21:
            print("You:", sum(player_cards))
            print(colored("You are above 21, YOU LOSE", "red"))
            lose = True
            consider_win(win=False, draw=False, lose=True)
            input("\nEnter to restart ")
            main()


    def double():
        stake *= 2
        print("Your new bet is $" + str(stake))

        get_card(player_cards)

        print("You:", player_cards, sum(player_cards))
        
        if sum(player_cards) == 21:
            if sum(dealer_cards) != 21:
                    win = True
                    consider_win(win=True, draw=False, lose=False)
            elif sum(dealer_cards) == sum(player_cards):
                    draw = True
                    consider_win(win=False, draw=True, lose=False)

            input("\nEnter to restart ")
            main()

        elif sum(player_cards) > 21:
            print("You:", sum(player_cards))
            print(colored("You are above 21, YOU LOSE", "red"))
            lose = True
            consider_win(win=False, draw=False, lose=True)
            input("\nEnter to restart ")
            main()

        get_dealer_card()
        
        if sum(dealer_cards) > 21:
            print(colored("Dealer is above 21. You Win!", "green"))
            win = True
            consider_win(win=True, draw=False, lose=False)
            input("\nEnter to restart ")
            main()

        elif sum(dealer_cards) <= 21:

            if sum(dealer_cards) > sum(player_cards):
                    print("Dealer:", sum(dealer_cards), "\nYou:", sum(player_cards))
                    print(colored("The Dealer is above you!, YOU LOST", "red"))
                    lose = True
                    consider_win(win=False, draw=False, lose=True)
                    input("\nEnter to restart ")
                    main()

            elif sum(dealer_cards) < sum(player_cards):
                    print("Dealer:", sum(dealer_cards), "\nYou:", sum(player_cards))
                    print(colored("The Dealer is below you!, YOU WIN", "green"))
                    win = True
                    consider_win(win=True, draw=False, lose=False)
                    input("\nEnter to restart ")
                    main()

            elif sum(dealer_cards) == sum(player_cards):
                    print("Dealer:", sum(dealer_cards), "\nYou:", sum(player_cards))
                    print(colored("Draw. Nobody won!", "yellow"))
                    draw = True
                    consider_win(win=False, draw=True, lose=False)
                    input("\nEnter to restart ")
                    main()


    def split(): # TODO
        pass


    with open("cash", "r") as f:
        content = f.read()
        credit = int(content)

    stake = int(input("Your bet: $"))

    while stake > credit:
        print("ERROR: You bet more than you have.")
        stake = int(input("Your bet: $"))
    while stake <= 0:
        print(f"ERROR: You cannot bet ${stake}")
        stake = int(input("Your bet: $"))

    # setup for player
    first_player, second_player = choice(all_cards), choice(all_cards)
    all_cards.remove(first_player)
    all_cards.remove(second_player)
    player_cards.append(first_player)
    player_cards.append(second_player)
    print("You:", player_cards, sum(player_cards))

    # setup for dealer
    first_dealer, second_dealer = choice(all_cards), choice(all_cards)
    all_cards.remove(first_dealer)
    all_cards.remove(second_dealer)
    dealer_cards.append(first_dealer)
    print("Dealer:", dealer_cards, sum(dealer_cards))
    dealer_cards.append(second_dealer)


    if (credit - (stake * 2)) < 0:
        options = ["Stand", "Hit"]
        index = TerminalMenu(options)
        first_choice = index.show()
    else:
        if first_player == second_player:
            options = ["Stand", "Hit", "Double", "Split"]
            index = TerminalMenu(options)
            first_choice = index.show()
        else:
            options = ["Stand", "Hit", "Double"]
            index = TerminalMenu(options)
            first_choice = index.show()

    if first_choice == 0:
        stand()
    elif first_choice == 1:
        hit()
        options = ["Stand", "Hit"]
        index = TerminalMenu(options)
        second_choice = index.show()

        if second_choice == 0:
            stand()
        elif second_choice == 1:
            hit()
            third_choice = index.show()

            if third_choice == 0:
                stand()
            elif third_choice == 1:
                hit()
            

    elif first_choice == 2:
        double()
    elif first_choice == 3:
        split()


if __name__ == "__main__":

    buy_in = int(input("Enter your buy in: $"))
    
    while buy_in <= 0:
        print(f"You cannot take {buy_in} as your buy-in. Enter again.")
        buy_in = int(input("Enter your buy in: "))

    with open("cash", "w") as f:
        f.write(str(buy_in))

    main()
