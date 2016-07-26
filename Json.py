import json
bitcoin = {
    'recv' : 'aa' ,
    'sender' : 'bb',
    'amount' : 10,
    'msg' : 'test'
}

jsonBit = json.dumps(bitcoin)

print(jsonBit)
print(type(jsonBit))

dict = json.loads(jsonBit)
print dict['amount']