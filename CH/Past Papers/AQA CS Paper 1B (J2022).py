# second to last question
# cards = [1, 2, 3, 5, 6, 9, 10, 13, 14, 16, 17, 21, 23, 24, 25, 27, 28, 30, 32, 33, 36, 41, 43, 47, 48, 49, 50, 51, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 66, 69, 71, 77, 79, 80, 81, 82, 90, 91, 92, 94, 97, 98, 101, 103, 104, 106, 107, 110, 112, 113, 114, 117, 118, 119, 120, 123, 124, 126, 128, 130, 132, 134, 139, 140, 141, 142, 147, 148, 149, 150, 151, 154, 156, 158, 159, 161, 165, 174, 179, 180, 181, 183, 184, 185, 187, 190, 193, 194, 196, 200]

cards = [...] # assume the cards are already set
gameWon = False
Rep = 1
for i in range(99):
	if cards[i] + 1 == cards[i + 1]:
		Rep += 1
		if Rep == 5:
			gameWon = True
	else:
		Rep = 1

ticket = [["","",""],
["","",""],
["","",""]]

def checkWinner(ticket):
    x = 0
    for i in range(3):
        for j in range(3):
            if ticket[i][j] == "*":
                x += 1
            
    if x == 9:
        print("Bingo")
    else:
        print(x)
            
checkWinner(ticket)
