# Metacharacters

- "." : any character except a newline
- "*" : 0 or more repetitions
- "+" : 1 or more repetitions
- ? : 0 or 1 repetition
- {m} : m repetitions
- {m,n} : m-n repetitions
- ^ : matches the start of the string
- $ : matches the end of the string or just before the newline at the end of the string
- [] : set of characters
- [^] : complementing the set
- A|B : either A or B
- (...) : a group
- (?:...) : non-capturing version

# Sets

- [a-zA-Z] : Returns a match for any character alphabetically between a and z, lower case OR upper case
- [0-9] : Returns a match for any digit between 0 and 9

# Special Sequences

- \d : decimal digit
- \D : not a decimal digit
- \s : whitespace characters
- \S : not a whitespace character
- \w : word character ... as well as numbers and the underscore
- \W : not a word character

# Functions

## search()

```
#Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
```

## findall()

```
#Print a list of all matches:
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
```

## split()

```
#Split at each white-space character:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
```

## sub()

```
# Replace every white-space character with the number 9:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
```

## count()

```
# Replace the first 2 occurrences:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
```

# Syntax

- search() : re.search(pattern, string, flags=0)

- match() : re.match(pattern, string, flags=0)

- fullmatch() : re.fullmatch(pattern, string, flags=0)

- sub() : re.sub(pattern, replace, string, count=0, flags=0)

- findall() : re.findall(pattern, string, flags=0)

## Flags

- re.IGNORECASE
- re.MULTILINE
- re.DOTALL


