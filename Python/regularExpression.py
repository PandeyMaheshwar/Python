''' Example 1
import re

#patterns = ['term1', 'term2']

text = 'This is a string with term1, not not the other!'

for patterns in patterns:
    print("I am searching for: "+patterns)

    if re.search(patterns,text):
        print("match")

    else:
        print("No match")

match = re.search('term1',text)
#print(type(match.start()))

print(match.start())
'''

#Example 2
'''import re

split_term =  '@'

email = "user@gmail.com"

print(re.split(split_term, email))
'''

# Example 3

import re

def mult_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for patterns {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sd...ssdddd.. sd. ddd.   ddd. sssd.   dhcg'
#test_patterns = ['sd*']
test_patterns = ['sd+']
mult_re_find(test_patterns,test_phrase)
