w = [12, 6, 7, 14, 19, 3, 0, 25, 40, 7]
l = 9
li = 7

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    arr = []
    for i, j in enumerate(weights):
        print(i)
        print(length)
        
        if(j not in d):
            d[j] = [i]
            print(d)
        elif(j in d):
            d[j].append(i)
            print(d)
    for i, j in enumerate(weights):
        if(limit - j in d):
            if(len(d[j]) > 1):
                d[j].sort()
                tup = (d[j][1], d[j][0])
            else:
                tup = (d[limit - j][0],d[j][0])
            return tup

    return None

print(get_indices_of_item_weights(w, l, li))