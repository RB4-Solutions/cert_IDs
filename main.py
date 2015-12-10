'''
Created by: Russell Brinson
Created for: RB4 Solutions, LLC
Function: Create a Certification ID to be used for the comprehensive security report
Input: the consistent word or phrase
Output: Certification ID to be used
'''

import hashlib 

print "Please Use All Caps" # This message should be updated per individual as it is the reminder to be be consistent with input

word_format = raw_input("Enter number: ")
word_format_plus_salt = word_format + "@$certID*&"
first_hash = hashlib.md5(word_format_plus_salt).hexdigest()

'''
Once the input has been taken in, the function needs to convert to hexdigest
After this conversion has taken place, the digest needs to be shortened to 16 characters
in length
'''

half_hash = first_hash[:16]
print half_hash
