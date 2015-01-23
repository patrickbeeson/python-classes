import shelve
import os


def highscore(name, score):
    """
    Function to return the high score from our
    persistent storage of score records for a given
    person.
    """
    # Get our working directory
    working_dir = os.getcwd()
    # Create our shelf object for a player
    highscore_fn = os.path.join(working_dir, 'highscore.shelve')
    # Open our shelf
    with shelve.open(highscore_fn, writeback=True) as shelf:
        # Check if player exists in shelf
        if name in shelf:
            # Check if score is greater than existing score
            if score > shelf[name]:
                # Assign our new high score
                high_score = score
                # Assign the value of player to our shelf
                shelf[name] = score
            else:
                # Existing high score stands for player
                high_score = shelf[name]
        else:
            # Assign the player to the shelf
            shelf[name] = score
            # Assign the high score to the player score
            high_score = score

    return high_score
