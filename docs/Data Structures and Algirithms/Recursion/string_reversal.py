# Function to reverse a string
def reverse_string(string):

    if not string:
        return ""
    else:
        # Logic here is to strip last character and concat it with the function call of string excluding the last character
        return string[-1] + reverse_string(string[:-1])
    
print(reverse_string("a"))
