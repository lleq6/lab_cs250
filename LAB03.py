def GenerateMatrix(Original, R):
    Column = ""
    Matrix = ""
    W = ""
    for i in InputSplit:
        for j in InputSplit:
            Column += f"{j} "
            if f"{i}R{j}" in R:
                Matrix += "1"
            else:
                if Original != None:
                    Layer = ConvertToLayer(Original)
                    if Layer[ConvertTextToIndex(i)][ConvertTextToIndex(j)] == "1":
                        Matrix += "1"
                    else:
                        Matrix += "0"
                else:
                    Matrix += "0"
            if i != InputSplit[len(InputSplit) - 1] or j != InputSplit[len(InputSplit) - 1]:
                Matrix += " "
        if i == InputSplit[0]:
            print(f"      {Column}")
        Column = ""
        print(f"    {i} {Matrix}")
        W += Matrix
        Matrix = ""
    return W
    
def SearchRowColumn(W, Index):
    P, Q = [], []
    Layer = ConvertToLayer(W)
    if Index >= len(Layer):
        return P, Q
    for i in range(len(InputSplit)):
        for j in range(len(Layer[i])):
            if Layer[i][Index] == "1" and InputSplit[i] not in P:
                P.append(f"{InputSplit[i]}")
            if Layer[Index][j] == "1" and InputSplit[j] not in Q:
                Q.append(f"{InputSplit[j]}")
    if P != [] and Q != []:
        print(f"P = {P}, Q = {Q}")
    return P, Q
        
def GenerateR(P, Q):
    R = []
    for i in P:
        for j in Q:
            R.append(f"{i}R{j}")
    if R != []:
        print(f"R = {R}")
    return R
        
def ConvertToLayer(W):
    Layer = []
    WSplit = W.split(" ")
    Length = len(InputSplit)
    Start, Stop = 0, Length
    for i in range(len(InputSplit)):
        Layer.append([j for j in WSplit[Start:Stop]])
        Start += Length
        Stop += Length
    return Layer

def ConvertTextToIndex(Text : str):
    return InputSplit.index(Text)

def CheckRelation(R):
    print("Property : ")
    Reflexive = []
    Symmetric =[]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i] == R[j]:
                Split = R[i].split("R")
                if Split[0] == Split[1]:
                    Reflexive.append(R[i])
                elif R[j][::-1] in R:
                    Symmetric.append(R[i])
    if len(Reflexive) == len(InputSplit):
        print(f"     Reflexive {Reflexive}")
    else:
        print("     No Reflexive")
    if len(Symmetric) == (len(InputSplit) * ((len(InputSplit) - 1) / 2) * 2):
        print(f"     Symmetric {Symmetric}")
    else:
        print("     No Symmetric")

try:
    Input = input("Input: ")
    # a, b, c, d
    # a, b, c, d, e
    R = input("Input R: ")
    # aRa, aRb, aRc, bRa, bRb, bRd, cRa, cRc, dRc, dRd
    # aRa, aRb, aRc, bRa, bRb, bRe, cRa, cRc, dRc, dRd, eRb
    InputSplit = Input.split(", ")
    RSplit = R.split(", ")
    R = RSplit
    Original = None
    for i in range(0, len(InputSplit) + 1):
        print("-" * 50)
        print(f"W{i} =")
        W = GenerateMatrix(Original, R)
        Original = W
        if i == 0:
            CheckRelation(R)
        P, Q = SearchRowColumn(W, i)
        R = GenerateR(P, Q)
    print("-" * 50)
except:
    print("Error!!, Please try again.")