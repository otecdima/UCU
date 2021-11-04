inputcombinations = []
gamerturn = input()
while gamerturn != "":
    inputcombinations.append(gamerturn)
    gamerturn = input()

for i in range(len(inputcombinations)):
    if inputcombinations[i] == "SS" or inputcombinations[i] == "PP" or inputcombinations[i] == "RR":
        print("False | False")

    if inputcombinations[i] == "SP" or inputcombinations[i] == "PR" or inputcombinations[i] == "RS":
        print("True")

    if inputcombinations[i] == "PS" or inputcombinations[i] == "RP" or inputcombinations[i] == "SR":
        print("False")
