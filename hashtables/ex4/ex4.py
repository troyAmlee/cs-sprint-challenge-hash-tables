def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []
    for i in a:
        if(i not in d):
            d[i] = 0
    for i in a:
        if((i * -1) < 0 and (i * -1) in d):
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))
