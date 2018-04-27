# For each element, compute the value of X.value

def computeValue(slist):
    xval = []
    for ii in range(len(slist)):
        count = 0;
        for j in range(len(slist) - ii):
            if (slist[ii] == slist[ii + j]):
                count += 1
        xval.append(count)
    return xval

if __name__=='__main__':
    streamData = input('Please input the stream data(Separate each data with space): ')
    streamList = streamData.split(' ')
    Xvalue = computeValue(streamList)
    i = []
    for items in range(len(streamList)):
        i.append(items + 1)
    result = dict(zip(i, Xvalue))
    print(result)