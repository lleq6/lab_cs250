Input = input("Input: ")

def convertStrToInt(Str):
    return [int(i) for i in Str]

def listSubset(PowerSet):
    Subset = []
    Length = len(PowerSet)
    for i in range(1 << Length):
        Subset.append({list(PowerSet)[j] for j in range(Length) if (i & (1 << j))} if i != 0 else chr(216))
    return Subset

setOfNumbers = set(convertStrToInt(Input))
print(f"Set of numbers: {setOfNumbers}")
Subsets = listSubset(setOfNumbers)
print(f" P({setOfNumbers}) = {Subsets}")
print(f"|P({setOfNumbers})|= {len(Subsets)}")