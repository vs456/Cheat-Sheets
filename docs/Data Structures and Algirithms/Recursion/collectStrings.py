# Function to collect all strings in an array from a dict object
def collectStrings(obj):

    result = []
    for key in obj:
        if type(obj[key]) is str:
            result.append(obj[key])
        if type(obj[key]) is dict:
            result += (collectStrings(obj[key]))
        
    return result

print(collectStrings({
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}))
