# import Counter module from collections library
from collections import Counter
#creating a function named elect
# that will select the elected condidate name
def elect(input_votes):
    # convert the input list into dictionary
    Vote=Counter(input_votes)
    Dict={}
    for Values in Vote.values():
        #initialize empty
        Dict[Values]=[]
    for (key,value) in Vote.items():
        Dict[value].append(key)
    # sort keys in descending order to get the maximum votes
    Maximum=sorted(Dict.keys(), reverse=True)[0]
    #check if more then one person have same no. of votes
    if(len(Dict[Maximum])>1):
        # if True then sort and then print the first element
        print(sorted(Dict[Maximum])[0])
    else:
        # else print the first element of dictionary heaving maximum vote
        print(Dict[Maximum][0])
#Driver Code
if __name__ == "__main__":
    input_votes =input("Enter space seperated candidate votes: ")
    input_votes =input_votes.split()
    print("Winner of election is: ",end='')
    elect(input_votes)