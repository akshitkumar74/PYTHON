# name = input("Enter any name : ")
# print("Good Afternoon, " + name)

letter = '''Dear <|NAME|>
        your the best coder of 
         my group so do not leave 
         my group.
         Thank you.
                     <|DATE|>'''
name = input("Enter any name : ")
date = input("Enter the date : ")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)