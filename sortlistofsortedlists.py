" Code to sort multiple sorted lists of numbers into a single sorted list. "

def inputLists(): 

    lists = []
    while True:
        try:
            line = input()
            if not line.strip():  # Stop on empty line
                break
            numbers = list(map(int, line.split()))
            lists.append(numbers)
        except EOFError:
            break
    return lists

def sortInputLists(input_lists):

    if not input_lists: # Check if the input list is empty
        return []

    newList = [0 for sublist in input_lists for lst in sublist]  # Initialize the empty final list

    n = len(input_lists)  # Number of sublists
    indexLst = [0 for _ in range(n)]  # Initialize index list for each sublist
    
    
    index = 0
    length = len(newList)  # Total number of elements in the flattened list

    smallest = input_lists[0][0]
    smallestindex = 0
        
    while index < length:

        for i in range(n):
            if indexLst[i] == -1:  # If the index is -1, it means the sublist is exhausted
                continue
            if (smallest > input_lists[i][indexLst[i]]):
                smallest = input_lists[i][indexLst[i]]
                smallestindex = i

        newList[index] = input_lists[smallestindex][indexLst[smallestindex]]
        indexLst[smallestindex] += 1
        index += 1
        if (indexLst[smallestindex] >= len(input_lists[smallestindex])):
            indexLst[smallestindex] = -1
            for i in range(n):
                if indexLst[i] == -1:
                    continue
                smallest = input_lists[i][indexLst[i]]
                smallestindex = i
                break
        else:
            smallest = input_lists[smallestindex][indexLst[smallestindex]]


    return newList

print("Enter lists of integers (space-separated). Press Enter on an empty line to finish:")
input_data = inputLists()
lst = sortInputLists(input_data)
print("Sorted list:", lst)
