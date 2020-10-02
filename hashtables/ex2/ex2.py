#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    route = []
    for i in tickets:
        print(i.source)
        print(d)
        
        if(i.source not in d):
            d[i.source] = i.destination
        if(i.source == "NONE"):
            print("Hello")
            route.append(d[i.source])
    for i in tickets:
        if(len(route) > 0):
            if(route[len(route) - 1] in d and "NONE" not in route):
                route.append(d[route[len(route) - 1]])
            if(d[route[len(route) - 1]] == "NONE" and i == length - 1):
                return route


    return route
print(reconstruct_trip(tickets, 3))