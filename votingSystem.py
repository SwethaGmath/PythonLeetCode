from collections import defaultdict
def rankTeams(votes):
    numberofTeams= len(votes[0])
    vote_counts = defaultdict(lambda: [0] * numberofTeams)
    print(vote_counts)

    # for vote in votes:
    #     for rank,team in enumerate(vote):
    #         vote_counts[team][rank]+=1

    for vote in votes:
        ranking = 3
        for i,c in enumerate(vote[::-1],1):
            vote_counts[c]+=ranking
            ranking-=1
    
    for team,voting in vote_counts.items():
        print(team,"---->",voting)

# myl = [(lambda x: x+45)(x) for x in range(3)]
# print(myl)
# just checkng hoe enumerate work
notes = ["BCA", "CAB", "CBA", "ABC"]
# for note in notes:
#     print(note)
#     for i ,j in enumerate(notes):
#         print(i,j)
#         print("\n")

rankTeams(["BCA", "CAB", "CBA", "ABC"])