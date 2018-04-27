# k's moment

def surpriseNumber(rawlist):
    distinctEle = set(rawlist)
    dictionary = {}
    for item in distinctEle:
        dictionary.update({item:rawlist.count(item)})
    surpriseNum = 0
    for items in dictionary:
        surpriseNum = surpriseNum + dictionary[items]**2
    return surpriseNum

def thirdMoment(list):
    distinctEle = set(list)
    dictionary = {}
    for item in distinctEle:
        dictionary.update({item:list.count(item)})
    thirdMom = 0
    for items in dictionary:
        thirdMom = thirdMom + dictionary[items]**3
    return thirdMom

if __name__=="__main__":
    streamData = input('Please input the stream data(Separate each data with space): ')
    streamList = streamData.split(' ')
    # streamList = list(map(int, streamList))
    surpNum = surpriseNumber(streamList)
    thirNum = thirdMoment(streamList)
    print(surpNum)
    print(thirNum)