#!/usr/bin/env python
# coding: utf-8

# <p style='font-size:40px;color:blue;'> Topic of the Project </p>
#
# Note : During the project, we will apply continuous integration
# principles using CircleCI

# # 1- We consider words composed of lowercase alphabetic characters, separated by whitespace(or new line) and we are interested in finding the 5 largest anagram groups
#
# ### Example :
#
# #### Input
# - undisplayed
# - trace
# - tea
# - singleton
# - eta
# - eat
# - displayed
# - crate
# - cater
# - carte
# - caret
# - beta
# - beat
# - bate
# - ate
# - abet
#
# #### Output
#
# - Group of size 5: caret carte cater crate trace .
# - Group of size 4: abet bate beat beta .
# - Group of size 4: ate eat eta tea .
# - Group of size 1: displayed .
# - Group of size 1: singleton .
#
# Source of this problem : http://poj.org/problem?id=2408

# <hr/>
#
# #### In order to solve this problem we will apply the oriented object principle learned in course.
#
# I propose to consider the following classes.
#
# The Class <strong>Word</strong> will represent a word. We can imagine the following methods.
#
# - A method shuffle able to shuffle the letters in a word (useful for unitest)
# - A method is_anagram able to tell us if a word is an anagram of an other one
#
# The Class <strong>Dictionary</strong> will represent a set of words, inside which there are anagrams. We can imagine the following method:
# - A method groups_of_anagrams able to find all the groups of anagrams included in the dictionary we consider.
#
# The Class <strong>Parse</strong> will be used to parse oracles for our problem. We can imagine the following method:
# - A method parse able to transform a .txt file into a dictionary of words if it respects the format given by the statement
#
# The Class <strong>Problem</strong> will be used to resolve a problem of this type with a .txt file. We can imagine the following method:
# - A method resolve which use the .txt file in order to solve the problem (so it returns the groups of anagrams of the dictionary defined by the .txt file)
#
# The Class <strong>TestMethods</strong> will be used to check the good
# working of our methods from the different classes

# In[43]:


import random as rd
import unittest


# In[82]:


class Word:
    def __init__(self, word):
        self.string = word

    ''' To check if two words are anagram of each other we will procede like this :

    First, we check if they have the same length. If it's the case...

    We take the first letter of the first word and 
	we check if it's present in the second one.

    If it's not, we can conclude that the two words aren't anagrams

    If it's the case, we delete the first occurence of the letter 
	considered in the second word and we continue with the

    next letter of the first word.

    Finally, we continue like that until the end of the first word considered.

    Note : We will not take in account the uppercase for this exercise 
	and so we will consider that two words made of the exact same letters 
	(even if some of them are maybe uppercase) are anagrams
    '''

    def is_anagram(self, word):
        first = self.string.lower()
        second = word.string.lower()
        length_1 = len(first)
        length_2 = len(second)
        result = False

        if length_1 == length_2:
            for i in range(0, length_1):
                if first[i] in second:
                    result = True
                    # We remove the first apparition of s1[i] in s2
                    second = second.replace(first[i], '', 1)
                else:
                    result = False
                    break
        return result

    def shuffle(self):
        # random.shuffle works on list so we decompose our word in a list of
        # letters
        s_list = list(self.string)
        rd.shuffle(s_list)
        string = "".join(s_list)
        word = Word(string)  # and then we recompose the word
        return word

    def __str__(self):
        return self.string

    def __repr__(self):
        return "Word(" + self.string + ")"


# In[83]:


class TestMethods(unittest.TestCase):

    def test_is_anagram(self):
        word_1 = Word('ChanCe')
        word_2 = Word('chnaec')
        word_3 = Word('kangaroo')
        word_4 = Word('KgroOanao')
        word_5 = Word('pneumonoultramicroscopicsilicovolcanoconiosis')
        word_6 = word_5.shuffle()
        word_7 = Word('Entertainment')
        word_8 = Word('Somethingelse')
        self.assertEqual(word_1.is_anagram(word_2), True)
        self.assertEqual(word_3.is_anagram(word_4), False)
        self.assertEqual(word_5.is_anagram(word_6), True)
        self.assertEqual(word_7.is_anagram(word_8), False)


unittest.main(argv=[''], verbosity=1, exit=False)


# ## 2 - We want a program that will read in a dictionary and a list of phrases and determine which words from the dictionary, if any, form anagrams of the given phrases.
#
# The program must find all sets of words in the dictionary which can be formed from the letters in each phrase. We will not include the set consisting of the original words.
#
# If no anagram is present, do not write anything, not even a blank line.
#
# ### Example :
#
# #### Input
#
# ABC
# AND
# DEF
# DXZ
# K
# KX
# LJSRT
# LT
# PT
# PTYYWQ
# Y
# YWJSRQ
# ZD
# ZZXY
# ZZXY ABC DEF
# SXZYTWQP KLJ YRTD
# ZZXY YWJSRQ PTYYWQ ZZXY
#
# #### Output
#
# SXZYTWQP KLJ YRTD = DXZ K LJSRT PTYYWQ
#
# SXZYTWQP KLJ YRTD = DXZ K LT PT Y YWJSRQ
#
# SXZYTWQP KLJ YRTD = KX LJSRT PTYYWQ ZD
#
# SXZYTWQP KLJ YRTD = KX LT PT Y YWJSRQ ZD
#
# Source of this problem :
# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=84

# # 3 - Finally, we will try to create a spell checker
#
# We will study first, the correction of the mistakes in which all the letters of a word are present, but, not in the good order
#
# Example :'Cra' instead of 'Car'
#
# The program must find such mistakes in a sentence or a paragraph knowing a sets of words in a dictionary.
#
# If I have time, I will extends the power of this spell checker in considering the case where some letters are forgotten in a word
#
# Exemple : 'Rom' instead of 'Room'
#
#
# #### Input
#
# - Dictionary = ['Movie','Car','Room','Supermarket','Computer']
# - Sentence = 'Today, I will go to the supemakret because I need a copmuter for my romo'
#
# #### Output
#
# I find 3 errors, I think the correct answer is :
#
# '''Today, I will go to the supermarket because I need a computer for my room'
#
