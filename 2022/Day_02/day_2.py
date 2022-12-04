class PaperRockScissors:
    rock = "A"
    paper = "B"
    scissors = "C"

    my_rock = "X"
    my_paper = "Y"
    my_scissors = "Z" 

    def get_play_value(play):
        if play == PaperRockScissors.rock or play == PaperRockScissors.my_rock:
            return 1
        elif play == PaperRockScissors.paper or play == PaperRockScissors.my_paper:
            return 2
        elif play == PaperRockScissors.scissors or play == PaperRockScissors.my_scissors:
            return 3
    
    def get_play_score_for_win(opposingPlay):
        if opposingPlay == PaperRockScissors.rock:
            return PaperRockScissors.get_play_value(PaperRockScissors.paper) + 6
        elif opposingPlay == PaperRockScissors.paper:
            return PaperRockScissors.get_play_value(PaperRockScissors.scissors) + 6
        elif opposingPlay == PaperRockScissors.scissors:
            return PaperRockScissors.get_play_value(PaperRockScissors.rock) + 6

    def get_play_score_for_tie(opposingPlay):
        return PaperRockScissors.get_play_value(opposingPlay) + 3

    def get_play_score_for_loss(opposingPlay):
        if opposingPlay == PaperRockScissors.rock:
            return PaperRockScissors.get_play_value(PaperRockScissors.scissors)
        elif opposingPlay == PaperRockScissors.paper:
            return PaperRockScissors.get_play_value(PaperRockScissors.rock)
        elif opposingPlay == PaperRockScissors.scissors:
            return PaperRockScissors.get_play_value(PaperRockScissors.paper)

    def are_same_play(opposingPlay, myPlay):
        if  opposingPlay == PaperRockScissors.rock and myPlay == PaperRockScissors.my_rock:
            return True
        elif opposingPlay == PaperRockScissors.paper and myPlay == PaperRockScissors.my_paper:
            return True
        elif opposingPlay == PaperRockScissors.scissors and myPlay == PaperRockScissors.my_scissors:
            return True
        else:
            return False

    def get_play_score(opposingPlay, myPlay):
        if PaperRockScissors.are_same_play(opposingPlay, myPlay):
            return PaperRockScissors.get_play_value(myPlay) + 3
        elif myPlay == PaperRockScissors.my_rock and opposingPlay == PaperRockScissors.scissors:
            return PaperRockScissors.get_play_value(myPlay) + 6
        elif myPlay == PaperRockScissors.my_paper and opposingPlay == PaperRockScissors.rock:
            return PaperRockScissors.get_play_value(myPlay) + 6
        elif myPlay == PaperRockScissors.my_scissors and opposingPlay == PaperRockScissors.paper:
            return PaperRockScissors.get_play_value(myPlay) + 6
        else:
            return PaperRockScissors.get_play_value(myPlay)


totalScore = 0                                                                                                                               
with open("./input.txt", "r") as input:
    for line in input.readlines():
        plays = line.strip().split()

        oppPlay = plays[0]
        #myPlay = plays[1]  # Part 1
        expectedOutcome = plays[1] 

        # Part 1
        #totalScore += PaperRockScissors.get_play_score(oppPlay, myPlay)

        # Part 2
        if expectedOutcome == "X":
            totalScore += PaperRockScissors.get_play_score_for_loss(oppPlay)
        elif expectedOutcome == "Y":
            totalScore += PaperRockScissors.get_play_score_for_tie(oppPlay)
        elif expectedOutcome == "Z":
            totalScore += PaperRockScissors.get_play_score_for_win(oppPlay)

print(totalScore)