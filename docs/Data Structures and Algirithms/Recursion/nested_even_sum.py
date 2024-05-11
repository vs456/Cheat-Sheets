# Function to find the sum of all even numbers in a dict that can contain other dicts, and non number elements
def nestedevensum(obj):

    result = 0
    for i in obj:
        # Check if the object is of dict type, and then call the function recursively
        if type(obj[i]) is dict:
            result += nestedevensum(obj[i])
        # Else check if its number, and even, and add it to the result
        elif type(obj[i]) is int and obj[i]%2 == 0:
            result += obj[i]
    return result

print(nestedevensum({
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}))
