import sys
from msvcrt import getch
def main():
  gapPosition = 10
  gapPosition2 = 11
  cursorPosition = 0
  coinArray = ["H","H","H","H","H","T","T","T","T","T","-","-"]
  cursor = ["-","  "," "," "," "," "," "," "," "," ", " "," "]
  printCoins(coinArray)
  moves = 0
  while moves != 5:
      move = "left"
      while not move == "s":
          print("\nChoose which coin to move")
          #temp = cursorPosition
          move = input("Press space to move and s to confirm?\n")
          cursor[cursorPosition] = " "
          if move == " ":
              if cursorPosition + 1 > 11: #puts cursor in beginning if you go over
                  cursor[cursorPosition] = " "
                  cursorPosition = 0
                  cursor[cursorPosition] = "-"
                  move = "reset"
              else:
                  cursorPosition = cursorPosition + 1
          elif move == "s":
               if coinArray[cursorPosition] == "-" or coinArray[cursorPosition+1] == "-" or cursorPosition > 10 : #rules for selecting( cant select a gap
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

          printCoins(coinArray)
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
      printCoins(coinArray)
      print("")
      printCursor(cursor)

      moves = moves + 1
  check = ""
  for coin in coinArray:
      check = check + coin
  if check == "HTHTHTHTHT--" or check == "THTHTHTHTH--":
      print("You win")
  elif check == "--HTHTHTHTHT" or check == "--THTHTHTHTH":
      print("You win")
  else:
      print("You Lose")


def printCoins(coinArray):
  for coin in coinArray:
      print(coin,end='')

def printCursor(cursor):
  for i in cursor:
      print(i,end='')


main()


