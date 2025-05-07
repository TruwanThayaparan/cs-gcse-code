# Challenge 19 - Logic Gate

logic_gate = input("ENTER LOGIC GATE (OR/AND/XOR/NAND/NOR): ").upper()
input1 = input("ENTER FIRST INPUT (0 or 1): ")
input2 = input("ENTER SECOND INPUT (0 or 1): ")

if input1 not in ("0", "1") or input2 not in ("0", "1"):
    print("ERROR: INVALID NUMBER USED.")
else:
    input1 = int(input1)
    input2 = int(input2)
    if logic_gate == "OR":
        result = input1 | input2
    elif logic_gate == "AND":
        result = input1 & input2
    elif logic_gate == "XOR":
        result = input1 ^ input2
    elif logic_gate == "NAND":
        result = int(not (input1 & input2))
    elif logic_gate == "NOR":
        result = int(not (input1 | input2))
    else:
        print("ERROR: INVALID LOGIC GATE USED.")
        result = None

    if result is not None:
        print("RESULT:", result)
