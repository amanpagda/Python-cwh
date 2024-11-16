name = input("Enter Your Name: ")

letter = ''' Dear <|Name|>, \n You are selected! <|Date|> '''

print(letter.replace("<|Name|>", name).replace("<|Date|>", "Today"))