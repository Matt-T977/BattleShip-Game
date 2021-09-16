import asset_creator


class UserInterface:
    def __init__(self) -> None:
        pass


    def position_input_format(self):
        invalid_input = True
        position_list = []
        while invalid_input:
            position_input = input("Where would you like to attack? Example: A 01\n").upper()
            position_input = position_input.split(" ")
            letter_input = position_input[0]
            number_input = position_input[1]
            if letter_input in asset_creator.Board.column_letters and number_input in range(20):
                position_list.append(letter_input)
                position_list.append(number_input)
                return position_list
            else:
                print("Invalid Input: Please try again.")    
