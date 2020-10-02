def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    ex = []
    length = len(arrays)
    for i in arrays:
        
        for j in i:

            if(j not in d):
                d[j] = 1

            elif(d[j] < length): 
                d[j] += 1

            if(d[j] == length):
                ex.append(j)
    return ex


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
