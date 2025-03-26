def file_list():
    returnlist = []
    f = open("in2a.txt", "r")
    for x in f:
        citystring, substrings = x[0], x[-1]

file_list()