# coding=utf-8
__author__ = 'Guoliang Lin'
Softwarename = 'trim replicates'
version = '1.0.1'
bugfixs = ''
import getopt
import sys
import time

print('%s software version is %s in 2016-01-19' % (Softwarename, version))
print(bugfixs)
print('starts at :' + time.strftime('%Y-%m-%d %H:%M:%S'))
opts, args = getopt.getopt(sys.argv[1:], 'i:h', ['inputfile=', 'help'])
for o, a in opts:
    if o in ['-i', '--inputfile']:
        InputFileName = a
    elif o in ['-h', '--help']:
        help = True
InputFileNameList = InputFileName.split(" ")
FDict = {}
SDict = {}


def trim(y):
    y = y.replace("[", '')
    y = y.replace(']', '')
    y = y.replace("',", '\t')
    y = y.replace("'", '')
    y = y.replace('\\n', '')
    y = y.replace(' ', '')
    # y=y.replace(',','')
    y = y.strip()
    y = y + '\n'
    return y


def repos(poslist):
    """


    :param poslist:
    :rtype : str
    """
    if poslist[0].find('.') == -1:
        return poslist[0]
    else:
        return poslist[1]


number = 0
string=""
for i in range(0, len(InputFileNameList)):
    rnumber = 0
    with open(InputFileNameList[i], 'r') as infile:
        for element in infile:
            list1 = element.split()
            if FDict.has_key(list1[0]):
                number = number + 1
                rnumber += 1
                if SDict.has_key(list1[0]):
                    SDict[list1[0]].append(InputFileNameList[i])
                else:
                    SDict[list1[0]] = FDict[list1[0]]
                    SDict[list1[0]].append(InputFileNameList[i])
            else:
                FDict[list1[0]] = list1
                FDict[list1[0]].append(InputFileNameList[i])
    string+=InputFileNameList[i]+"\t"+str(rnumber)+'\n'
with open("commonsegment.diff-filter.out", 'r') as inputfile:
    with open("diff.text", 'w') as outfile:
        with open("replicates.txt", 'w') as innerd:
            with open("stastic.txt",'w') as tongji:
                for element in inputfile:
                    list1 = element.split()
                    string1 = list1[0] + '_' + repos(list1[1:3])
                    if not FDict.has_key(string1):
                        outfile.write(trim(str(list1)))
                for value in SDict.values():
                    innerd.write(trim(str(value)))
                tongji.write(string)