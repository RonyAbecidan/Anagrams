
<p style='font-size:40px;color:blue;'> Topic of the Project </p>

### For this second project, I chose to play with strings and I propose to attempt to solve the two following problems

# 1- We consider words composed of lowercase alphabetic characters, separated by whitespace(or new line) and we are interested in finding the 5 largest anagram groups

### Example :

#### Input
- undisplayed
- trace
- tea
- singleton
- eta
- eat
- displayed
- crate
- cater
- carte
- caret
- beta
- beat
- bate
- ate
- abet

#### Output

- Group of size 5: caret carte cater crate trace .
- Group of size 4: abet bate beat beta .
- Group of size 4: ate eat eta tea .
- Group of size 1: displayed .
- Group of size 1: singleton .

Source of this problem : http://poj.org/problem?id=2408

## 2 - We want a program that will read in a dictionary and a list of phrases and determine which words from the dictionary, if any, form anagrams of the given phrases.

The program must find all sets of words in the dictionary which can be formed from the letters in each phrase. We will not include the set consisting of the original words. 

If no anagram is present, do not write anything, not even a blank line.

### Example :

#### Input 

ABC
AND
DEF
DXZ
K
KX
LJSRT
LT
PT
PTYYWQ
Y
YWJSRQ
ZD
ZZXY
ZZXY ABC DEF
SXZYTWQP KLJ YRTD
ZZXY YWJSRQ PTYYWQ ZZXY

#### Output

SXZYTWQP KLJ YRTD = DXZ K LJSRT PTYYWQ 

SXZYTWQP KLJ YRTD = DXZ K LT PT Y YWJSRQ

SXZYTWQP KLJ YRTD = KX LJSRT PTYYWQ ZD

SXZYTWQP KLJ YRTD = KX LT PT Y YWJSRQ ZD

Source of this problem : https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=84
