import collections
import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    play = 'R'

    # n is the number of opponent plays we look behind to create the recent_sequence, i.e the last n opponent plays
    n = 3
    recent_sequence = opponent_history[-n:]
    # we'll use the followup_moves list to gather all the plays that followed the sequence of plays in the recent_sequence list
    followup_moves = []

    for i, move in enumerate(opponent_history[:-n]):
        # every time we find the recent_sequence plays in the opponent_history, we save the opponent play immediately after
        if opponent_history[i:i+n] == recent_sequence:
            followup_moves.append(opponent_history[i+n])

    if followup_moves:
        # we determine what is the most common play the opponent chooses after the sequence of plays in the recent_sequence list 
        counter = collections.Counter(followup_moves)
        most_common_followup_move = counter.most_common(1)[0][0]
        # and we choose the appropriate play to counter it
        if most_common_followup_move == 'P': play = 'S'
        if most_common_followup_move == 'R': play = 'P'
        if most_common_followup_move == 'S': play = 'R'

    # each match has 1000 games so we clean-up for next opponent
    if len(opponent_history) == 1000:
        opponent_history.clear()
    
    return play