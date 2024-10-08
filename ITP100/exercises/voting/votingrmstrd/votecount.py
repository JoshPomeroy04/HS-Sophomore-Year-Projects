import sys
from voting import plurality, exhaustive, primary12, primary13, primary23


def get_voting_data(infile):
    """
    Read voters choices among three candidates into a list of lists of
    3-tuples: each inner list contains tuples that hold votes in the form of
    a voters ranking of the three candidates in order from best to worst.
    """
    elections = []

    line_tuples = []
    for line in infile.readlines():
        try:
            line_tuples.append(tuple([int(n.strip()) for n in line.split()]))
        except (ValueError, TypeError):
            print(f"ERROR: Bad input file.")
            return
        infile.close()

    election = []
    for vote in line_tuples:
        if vote[0] == -1:
            elections.append(election)
            return elections
        if vote[0] == 0:
            elections.append(election)
            election = []
        else:
            election.append(vote)

    return elections


def print_results(elections):
    for election_num, election in enumerate(elections):
        print(f'-------- election {election_num + 1}')
        print(f' plurality winner {plurality(election)}')
        print(f'exhaustive ballot {exhaustive(election)}')
        print(f'       12 primary {primary12(election)}')
        print(f'       13 primary {primary13(election)}')
        print(f'       23 primary {primary23(election)}')
    

if __name__ == "__main__":
    try:
        infile_name = 'voting.txt'
        infile = open(infile_name)
    except IndexError:
        print("USAGE ERROR: Must include data input file name as an argument.")
    except FileNotFoundError:
        print(f"ERROR: File {infile_name} not found.")
    else:
        print_results(get_voting_data(infile))

