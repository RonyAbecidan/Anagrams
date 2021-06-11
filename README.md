## 🎓 Dealing with Anagrams 

- In this repo, I propose to solve some problems I found on the web for learning purposes in Python 

![visitors](https://visitor-badge.glitch.me/badge?page_id=RonyAbecidan.Anagrams)

--- 

:one: We consider words composed of lowercase alphabetic characters, separated by a new line and we are interested in finding the 5 largest anagram groups

**Example :**

``Input``
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

``Output``

- Group of size 5: caret carte cater crate trace .
- Group of size 4: abet bate beat beta .
- Group of size 4: ate eat eta tea .
- Group of size 1: displayed .
- Group of size 1: singleton .

Click [here](http://poj.org/problem?id=2408) to see the source of this problem

---

:two: We want a program that will read in a dictionary and a list of phrases and determine which words from the dictionary, if any, form anagrams of the given phrases.

- The program must find all sets of words in the dictionary which can be formed from the letters in each phrase. We will not include the set consisting of the original words. 

- If no anagram is present, nothing will be printed.

- These words must appear in alphabetic sequence.

- Input will consist of two parts. The first part is the dictionary, the second part is the set of phrases
for which you need to find anagrams. 

**Example :**

`Input Dictionary`

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

`Input sentences`

- ZZXY ABC DEF
- SXZYTWQP KLJ YRTD
- ZZXY YWJSRQ PTYYWQ ZZXY

`Output`

SXZYTWQP KLJ YRTD = DXZ K LJSRT PTYYWQ 

SXZYTWQP KLJ YRTD = DXZ K LT PT Y YWJSRQ

SXZYTWQP KLJ YRTD = KX LJSRT PTYYWQ ZD

SXZYTWQP KLJ YRTD = KX LT PT Y YWJSRQ ZD

Click [here]( https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=84) to see the source of this problem

---

3️⃣ - Finally, we will try to create a spell checker

For simplicity, we will simply study the correction of mistakes in which all the letters of a word are present, but, not in the good order.

**Example :** 'Cra' instead of 'Car'

The program must find such mistakes in a sentence or a paragraph knowing a sets of words in a dictionary.

`Input` : A .txt document with first, the words of the dictionary at each line until a line in which, there will be the symbol "#" indicating that we start to consider sentences

- Today
- ,
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

**Sentence** : 'Today, I will go to the supemakret because I need a copmuter for my romo'

`Output` :  I find errors, I think the correct answer is :

> Today, I will go to the supermarket because I need a computer for my room

**Sentence** : 'I am watching a moive from my cra'

Output` :  I find errors, I think the correct answer is :

> I am watching a movie from my car

- If there is more than one proposition of correction, we will print all the proposed words separated by a '/'

This last problem is not coming from any website, I imagined it considering the previous two ones.

**All the above problems have been solved, you can test it, following the instructions in the OPENME notebook**
