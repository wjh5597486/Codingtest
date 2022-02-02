import re

# \d [0-9]
# \D [^0-9]
# \s [ \t\n\f\r\v]
# \S [^ \t\n\f\r\v]
# \w [a-zA-Z0-9_]
# \W [^a-zA-Z0-9_]

# . all except \n

# * reiteration equal or more than 0 times
# + reiteration more than 0 times
# {n} reiteration n times
# {n,m} reiteration n to m times
# ? = {0,1}

# Boundary
# \ boundary
# \B not boundary
# ^ start
# $ end