def importWords():
     return listOfWords

def importBoard():
     return board

def printBoard(board):
     pass

def searchHorizontally(word,board):
     return

def searchVerically(word,board):
     return

def searchRightDiagonal(word,board):
     return

def searchLeftDiagonal(word,board):
     return

wordSearchBoard=importBoard()
#Heads up, for testing, you could comment out this line and set words=your own list
words=importWords()

print(f'''
      
Original Board
{printBoard(wordSearchBoard)}

''')

#TODO:  Between these two print statements, you will run all of your searches.


print(f'''
      
Answer Board
{printBoard(wordSearchBoard)}

''')