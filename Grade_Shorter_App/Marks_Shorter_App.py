print("Welcome to Marks Sorter App")

#get user input
marks = []
n=0
while(n<3):
    n = int(input("How many marks you want to enter?"))
    if (n<3):
        print("Enter more than two marks!")
for i in range(1,n+1):
    mark = int(input(f"\n Enter your {i} marks (0-100): "))
    marks.append(mark)

print("\n Your marks are: ", str(marks))

#Sort the list from highest to lowest
marks.sort(reverse=True)
print("\nYour marks from highest to lowest: ", str(marks))

#Removing the lowest two marks
print("Removed marks are: ",marks.pop(),marks.pop())

#Printing the highest marks
print("Your highest mark is: ", str(marks[0]))