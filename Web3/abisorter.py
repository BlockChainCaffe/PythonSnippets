#!/usr/bin/python3
import sys
import json
import pdb

abifile = sys.argv[1]
outname = sys.argv[2] if sys.argv[2]!= "" else abifile+"_sorted"

# Read ABI
with open(abifile, 'r') as inputfile:
    abi = inputfile.read()

inabi = json.loads(abi)
outabi = []

pdb.set_trace()

# # move constructor
# # for i in inabi:
# #     if i["type"] == "constructor":
# #         outabi.append(i)
# # for i in inabi:
# #     if i["type"] == "constructor":
# #         inabi.remove(i)
# outabi.extend( filter( lambda i : i["type"] == "constructor" , inabi) )


# # print ("len : ", len(inabi))
# # # move events
# # for i in inabi:
# #     if i["type"] == "event":
# #         outabi.append(i)
# #         print("adding ", i["name"])
# # for i in inabi:
# #     if i["type"] == "event":
# #         inabi.remove(i)
# #         print("removing ", i["name"])
# outabi.extend( filter( lambda i : i["type"] == "event" , inabi) )


# # print ("len : ", len(inabi))
# # # move write functions
# # for i in inabi:
# #     if i["type"] == "function" and i["constant"] == True :
# #         outabi.append(i)
# #         print("adding ", i["name"])
# # for i in inabi:
# #     if i["type"] == "function" and i["constant"] == True :
# #         inabi.remove(i)
# #         print("removing ", i["name"])
# outabi.extend( filter( lambda i : i["type"] == "event" and i["constant"] == True , inabi) )



# # print ("len : ", len(inabi))
# # # move read functions
# # for i in inabi:
# #     if i["type"] == "function" and i["constant"] == False :
# #         outabi.append(i)
# #         print("adding ", i["name"])
# # for i in inabi:
# #     if i["type"] == "function" and i["constant"] == False :
# #         inabi.remove(i)
# #         print("removing ", i["name"])
# outabi.extend( filter( lambda i : i["type"] == "event" and i["constant"] == False , inabi) )


# # print ("len : ", len(inabi))
# # # move the rest
# # for i in inabi:
# #     outabi.append(i)
# #     print("adding ", i["name"])
# print ("len : ", len(inabi))

def getVal(i) :
    t = i.get("type", "Zzzzzzzz")
    c = i.get("constant", "Zzzzzzzz")
    n = i.get("name", "Zzzzzzzz")
    return (t,c,n)

outabi = sorted(inabi, key=getVal)

# Write new ABI
with open(outname, 'w') as outfile:
    outfile.write( json.dumps(outabi, indent=4))