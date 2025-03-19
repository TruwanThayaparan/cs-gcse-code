Cards = [...]
gameWon = False
Rep = 1
for i in range(99):
  if cards[i] + 1 == cards[i + 1]:
		Rep += 1
		If Rep == 5:
			gameWon = True
	else:
		Rep = 1
