maths = int(input("Enter the marks in Maths : "))
chemistry = int(input("Enter the marks in chemistry : "))
physics = int(input("Enter the marks in physics : "))

if(maths<33 and physics<33 and chemistry<33):
    print("You are failed")

elif(maths + chemistry + physics )/3 < 40:
    print("You are fail due to total percentage less than 40")

else:
    print("Congatulations! You passed the exam")
