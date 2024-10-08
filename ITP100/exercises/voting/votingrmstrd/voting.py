def plurality(election):
    """
    Return the plurality winner among three candidates, 1, 2, and 3. The input
    election is a list of three tuples, so in a plurality election only the
    first element matters.

      >>> plurality([(1, 2, 3), (2, 3, 1), (2, 1, 3)])
      2
      >>> plurality([(3, 2, 1), (3, 2, 1), (2, 1, 3)])
      3
    """
    # Count the votes for each of the three candidates in a dictionary
    vote_totals = {1: 0, 2: 0, 3: 0} 
    for vote in election:
        vote_totals[vote[0]] += 1

    # Return the candidate number with the highest vote count
    return max(vote_totals.items(), key=lambda x: x[1])[0]


def exhaustive(election):
    """
    Loser gets knocked out then it's only the two winners.

      >>> exhaustive([(1, 2, 3), (1, 2, 3), (2, 1, 3), (1, 3, 2), (2, 3, 1), (3, 1, 2)])
      1
      >>> exhaustive([(1, 2, 3), (1, 2, 3), (2, 3, 1), (2, 1, 3), (3, 2, 1)])
      2
    """
    vote_totals = {1: 0, 2: 0, 3: 0}
    for vote in election:
        vote_totals[vote[0]] += 1
    loser = min(vote_totals.items(), key = lambda x: x[1])[0]
    vote_totals2 = {1: 0, 2: 0, 3: 0}
    for vote in election:
        if vote[0] == loser:
            vote_totals2[vote[1]] += 1
        else:
            vote_totals2[vote[0]] += 1
    return max(vote_totals2.items(), key = lambda x: x[1])[0]


def primary12(election):
    """
    1 and 2 face off then the winner faces 3.
      >>> primary12([(1, 2, 3), (1, 2, 3), (2, 3, 1), (1, 2, 3), (3, 2, 1), (3, 1, 2), (1, 3, 2)])
      1
      >>> primary12([(3, 2, 1), (3, 2, 1), (2, 1, 3), (1, 3, 2), (2, 1, 3), (1, 3, 2), (1, 2, 3)])
      3
    """
    vote_totals = {1: 0, 2: 0, 3: 0}
    for vote in election:
        if vote[0] == 3:
            vote_totals[vote[1]] += 1
        else:
            vote_totals[vote[0]] += 1
    loser = min(vote_totals.items(), key = lambda x: x[1])[0]
    winner = max(vote_totals.items(), key = lambda x: x[1])[0]
    vote_totals2 = {1: 0, 2: 0, 3: 0}
    for vote in election:
        if vote[0] != loser and vote[0] != winner:
            vote_totals2[vote[1]] += 1
        else:
            vote_totals2[vote[0]] += 1
    return max(vote_totals2.items(), key = lambda x: x[1])[0]


def primary13(election):
    """
    1 and 3 face off then the winner faces 2.
      >>> primary13([(1, 2, 3), (1, 2, 3), (2, 1, 3), (3, 2, 1), (3, 2, 1), (2, 1, 3)])
      2
      >>> primary13([(1, 2, 3), (2, 3, 1), (1, 3, 2), (2, 3, 1), (1, 3, 2), (2, 1, 3), (3, 1, 2)])
      1
    """
    vote_totals = {1: 0, 2: 0, 3: 0}
    for vote in election:
        if vote[0] == 2:
            vote_totals[vote[1]] += 1
        else:
            vote_totals[vote[0]] += 1
    loser = min(vote_totals.items(), key = lambda x: x[1])[0]
    winner = max(vote_totals.items(), key = lambda x: x[1])[0]
    vote_totals2 = {1: 0, 2: 0, 3: 0}
    for vote in election:
        if vote[0] != loser and vote[0] != winner:
            vote_totals2[vote[1]] += 1
        else:
            vote_totals2[vote[0]] += 1
    return max(vote_totals2.items(), key = lambda x: x[1])[0]


def primary23(election):
    """
    2 and 3 face off then the winner faces 1.
      >>> primary23([(1, 2, 3), (2, 3, 1), (1, 2, 3), (3, 2, 1), (2, 1, 3), (1, 3, 2), (1, 2, 3)])
      1
      >>> primary23([(3, 2, 1), (1, 3, 2), (2, 3, 1), (1, 2, 3), (3, 1, 2)])
      3
    """
    vote_totals = {1: 0, 2: 0, 3: 0}
    for vote in election:
        if vote[0] == 1:
            vote_totals[vote[1]] += 1
        else:
            vote_totals[vote[0]] += 1
    loser = min(vote_totals.items(), key = lambda x: x[1])[0]
    winner = max(vote_totals.items(), key = lambda x: x[1])[0]
    vote_totals2 = {1: 0, 2: 0, 3: 0}
    for vote in election:
        if vote[0] != loser and vote[0] != winner:
            vote_totals2[vote[1]] += 1
        else:
            vote_totals2[vote[0]] += 1
    return max(vote_totals2.items(), key = lambda x: x[1])[0]




if __name__ == '__main__':
    import doctest
    doctest.testmod()
