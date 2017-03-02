#Kevin Duong 011715000
def main():
  gapPosition = 10
  gapPosition2 = 11
  cursorPosition = 0
  coinArray = ["H","H","H","H","H","T","T","T","T","T","-","-"]
  cursor = ["-","  "," "," "," "," "," "," "," "," ", " "," "]
  printCoins(coinArray)
  moves = 0
  while moves <= 5:
      move = "left"
      while not move == "s":
          print("\nMove: ", moves)
          print("\nChoose which coin to move")
          #temp = cursorPosition
          move = input("Press space to move and s to confirm?\n")
          cursor[cursorPosition] = " "
          if move == " ":
              if cursorPosition + 1 > 11: #puts cursor in beginning if you go over array size
                  cursor[cursorPosition] = " "
                  cursorPosition = 0
                  cursor[cursorPosition] = "-"
                  move = "reset"
              else:
                  cursorPosition = cursorPosition + 1
          elif move == "s": #if you presss select
               if coinArray[cursorPosition] == "-" or coinArray[cursorPosition+1] == "-" or cursorPosition > 10 : #rules for selecting( cant select a gap, etc)
                  print("invalid choose again")
                  cursor[cursorPosition] = " "
                  cursorPosition = 0
                  cursor[cursorPosition] = "-"
                  move = "reset"
               else:
                  move = "s"
          else:
              print("Please type left or right.")
          cursor[cursorPosition] = "-"

          printCoins(coinArray) #prints coins and cursor position
          print("")
          printCursor(cursor)

          #########swap positions
      temp3 = coinArray[gapPosition]
      temp4 = coinArray[gapPosition2]
      coinArray[gapPosition] = coinArray[cursorPosition]
      coinArray[gapPosition2] = coinArray[cursorPosition + 1]
      coinArray[cursorPosition] = temp3
      coinArray[cursorPosition + 1] = temp4
      gapPosition = cursorPosition
      gapPosition2 = cursorPosition + 1
        ########### end swap

      ##reset cursor
      cursor[cursorPosition] = " "
      cursorPosition = 0
      cursor[cursorPosition] = "-"
      move = "reset"
      #end reset

      print("")
      printCoins(coinArray) #prints coins and cursor position
      print("")
      printCursor(cursor)

      moves = moves + 1
  check = ""
  for coin in coinArray:
      check = check + coin

  ##Win/Lose Condition
  if check == "HTHTHTHTHT--" or check == "THTHTHTHTH--":
      print("You win")
  elif check == "--HTHTHTHTHT" or check == "--THTHTHTHTH":
      print("You win")
  else:
      print("You Lose")
  #end win/lose conditions


def printCoins(coinArray): #prints coins
  for coin in coinArray:
      print(coin,end='')

def printCursor(cursor): #prints cursor position
  for i in cursor:
      print(i,end='')


main() #starts main


