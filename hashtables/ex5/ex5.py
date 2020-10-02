# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    d = {}
    for i in files:
        sp = i.split("/")
        if(sp[len(sp) - 1] not in d):
            d[sp[len(sp) - 1]] = [i]
        elif(sp[len(sp) - 1] in d):
            d[sp[len(sp) - 1]].append(i)
    for j in queries:
        if(j in d):
            result.extend(d[j])
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
