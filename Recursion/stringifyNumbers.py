# Function to take in an object(dict) and find all of the values which are numbers and converts them to strings
def stringifyNumbers(obj):

    newobj = obj
    
    for key in obj:
        if type(obj[key]) is int:
            newobj[key] = str(obj[key])
 
    if type(obj[key]) is dict:
        newobj[key] = stringifyNumbers(obj[key])

    return newobj

print(stringifyNumbers({
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}))
            