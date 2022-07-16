numJudges = 7
numCompetitors = int(input("Enter number of competitors between 3 and 16: "))
while numCompetitors < 3 or numCompetitors > 16:
    numCompetitors = int(input("ERROR: Re-enter number between 3 and 16: "))


for comp in range(numCompetitors):
    totalC = 0
    print("Input scores between 0 and 10 for each Judge")
    for j in range(numJudges):
        scoreJ = int(input("Score for judge (0-10): "))
        while scoreJ < 0 or scoreJ > 10:
            numCompetitors = int(input("ERROR: Re-enter score (0-10)"))
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("Score for competitor", comp, " is", scoreC)

