# Topic of the Project 

### For this second project, I chose to play with strings and I propose to attempt to solve the following problems

# 1- We consider words composed of lowercase alphabetic characters, separated by a new line and we are interested in finding the 5 largest anagram groups

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


# 2 - We want a program that will read in a dictionary and a list of phrases and determine which words from the dictionary, if any, form anagrams of the given phrases.

The program must find all sets of words in the dictionary which can be formed from the letters in each phrase. We will not include the set consisting of the original words. 

If no anagram is present, do not write anything, not even a blank line.

These words must appear in alphabetic sequence.

Input will consist of two parts. The first part is the dictionary, the second part is the set of phrases
for which you need to find anagrams. Each part of the file will be terminated by a line consisting of a
single ‘#’

### Example :

#### Input 

- ABC
- AND
- DEF
- DXZ
- K
- KX
- LJSRT
- LT
- PT
- PTYYWQ
- Y
- YWJSRQ
- ZD
- ZZXY

#
- ZZXY ABC DEF
- SXZYTWQP KLJ YRTD
- ZZXY YWJSRQ PTYYWQ ZZXY

#### Output

SXZYTWQP KLJ YRTD = DXZ K LJSRT PTYYWQ 

SXZYTWQP KLJ YRTD = DXZ K LT PT Y YWJSRQ

SXZYTWQP KLJ YRTD = KX LJSRT PTYYWQ ZD

SXZYTWQP KLJ YRTD = KX LT PT Y YWJSRQ ZD

Source of this problem : https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=84

# 3 - Finally, we will try to create a spell checker

We will study first, the correction of the mistakes in which all the letters of a word are present, but, not in the good order.

### Example :'Cra' instead of 'Car'

The program must find such mistakes in a sentence or a paragraph knowing a sets of words in a dictionary.

Moreover, I will extend the power of this spell checker in considering the case where some letters are forgotten in a word

### Exemple : 'Rom' instead of 'Room'

For instance, let's say that we want to also guess a word written by someone in which there are at most 2 letters missing (knowing a dictionary)


### Input : A .txt document with first, the words of the dictionary at each line until a line in which there will be the symbol "#" which will indicate that we start to consider sentences

- Today
- I
- Am
- Watching
- From
- Will
- Go
- To
- The
- Because
- Need
- A
- For
- My
- Movie
- Car
- Room
- Supermarket
- Computer
- #
- Today, I will go to the supemakret because I need a copmuter for my romo
- I am watching a moive from my cra


### Output : Proposition of corrections for the sentences

Sentence : 'Today, I will go to the supemakret because I need a copmuter for my romo'

I find errors, I think the correct answer is :

'Today, I will go to the supermarket because I need a computer for my room'

Sentence : 'I am watching a moive from my cra'

I find errors, I think the correct answer is :

'I am watching a movie from my car'
