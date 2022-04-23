#nested loop

#making rectangle

rows = int(input("No of rows: "))

columns = int(input("No of columns: "))

symbol = input("Enter symbol: ")

for i in range (rows):
    for j in range (columns):
        print(symbol, end="") #prevent moving the coursor to the line
    print()