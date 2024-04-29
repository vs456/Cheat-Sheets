# Function to check if the string is palindrome or not
def ispalindrome(string):

    # If the string becomes null, that means all conditions were satisfied till now.
    if len(string) == 0:
        return True
    # Check if the first letter of the strin is same as the last one
    if string[0] != string[len(string)-1]:
        return False
    # Logic here is to remove the first & last letter of the string, and check the above conditions
    return ispalindrome(string[1:-1])

print(ispalindrome("ababa"))
