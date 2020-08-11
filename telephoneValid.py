# \w is equivalent to writing [ a-z | A-Z | 0-9 | _ ]
# ^ means everything except the characters provided after this symbol in the braces i.e.
# [ ^ a-z | A-Z | 0-9 | _ ]
# \W is used similarly to the ^ symbol, as it matches everything except the characters
# within the provided braces i.e. \W [ a-z | A-Z | 0-9 | _ ]

import re

telephonestr = "412-555-1212"

if re.search("\w{3} =\w{3} -\w{4}", telephonestr):
    print("Telephone number provided is valid")
else:
    print("Telephone number provided is invalid")



