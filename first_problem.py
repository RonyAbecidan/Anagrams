#!/usr/bin/env python
# coding: utf-8

import random as rd
import unittest
import numpy as np


class Word:
    def __init__(self, word):
        self.string = word

    def is_anagram(self, word):
        ''' To check if two words are anagram of each other we will procede like this :

        First, we check if they have the same length. If it's the case...

        We take the first letter of the first word and we check if it's present in the second one.

        If it's not, we can conclude that the two words aren't anagrams

        If it's the case, we delete the first occurence of the letter considered in the second word and we continue with the

        next letter of the first word.

        Finally, we continue like that until the end of the first word considered.

        Note : We will not take in account the uppercase for this exercise and so we will consider that
        two words made of the exact same letters (even if some of them are maybe uppercase) are anagrams
        '''

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
        return self.string


# In[53]:


class Dictionary:
    def __init__(self, list_of_words):
        self.low = list_of_words

    def remove(self, word):
        list_of_words = self.low
        d_list = [w.string for w in list_of_words]
        if word.string in d_list:
            index = d_list.index(word.string)
            del list_of_words[index]
            self.low = list_of_words

    def is_in_the_dictionary(self, word):
        list_of_words = self.low
        d_list = [w.string for w in list_of_words]
        if word.string in d_list:
            return True
        else:
            return False

    def groups_of_anagrams(self):
        ''' To find the group of anagrams we will procede like this :

         First, we create a copy of our dictionary.
         Then, for every word w of the initial dictionary,
             we are looking for all the words of the copied dictonary which are anagrams of the word w
             then,we put them into a list and we print them as wanted.

         In order to not have doublons at the end, we consider at each loop a list which we will contain,
         all the words which are anagrams of the current word w. At the end of the research of anagrams for
         this word, we erase their existence in the copied dictionary.

         And, in order to not considered an anagram of a word already treated, we execute the loop only if
         the word for which we are looking for anagrams is in the copied dictionary.

         Furthemore, at the end, we have to return only the 5 largest groups of anagrams.

        '''

        groups = []
        copy_low = self.low.copy()
        copy = Dictionary(copy_low)
        for word in self.low:
            if copy.is_in_the_dictionary(word):
                group = []
                to_remove = []
                for other_word in copy.low:
                    if other_word.is_anagram(word):
                        group.append(other_word)
                        to_remove.append(other_word)
                groups.append(group)
            for word_to_remove in to_remove:
                copy.remove(word_to_remove)

        groups_length = np.array([len(group) for group in groups])
        # 5 biggest elements of groups_length
        indexes = groups_length.argsort()[::-1][:5]
        str = ''
        for index in indexes:
            str = str + \
                f"Group of size {groups_length[index]} : {groups[index]} \n"
        return str

    def __repr__(self):
        return str(self.low)


class Problem:
    def __init__(self, filename):
        self.filename = filename

    def parse(self, path='Oracles_1'):
        try:
            file = open(f"{path}/{self.filename}.txt", "r")
            number_of_words = len(file.readlines())
            file.seek(0)
            list_of_strings = []
            for i in range(0, number_of_words):
                list_of_strings.append(file.readline().replace('\n', ''))
            file.close()
            return Dictionary([Word(i) for i in list_of_strings])
        except BaseException:
            print("Please check the file (even it's name) , there is something wrong")

    def resolve_str(self, path='Oracles_1'):
        dictionary = self.parse(path)
        if dictionary is not None:
            return dictionary.groups_of_anagrams()  # for the unittest

    def resolve(self, path='Oracles_1'):
        if self.resolve_str(path) is not None:
            print(self.resolve_str(path))


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

    def test_groups_of_ancagrams(self):
        l = [
            "trace",
            "tea",
            "singleton",
            "eta",
            "eat",
            "displayed",
            "crate",
            "cater",
            "carte",
            "caret",
            "beta",
            "beat",
            "bate",
            "ate",
            "abet"]
        dictionary = Dictionary([Word(i) for i in l])
        s = 'Group of size 5 : [trace, crate, cater, carte, caret] \nGroup of size 4 : [beta, beat, bate, abet] \nGroup of size 4 : [tea, eta, eat, ate] \nGroup of size 1 : [displayed] \nGroup of size 1 : [singleton] \n'
        self.assertEqual(dictionary.groups_of_anagrams() == s, True)

    def test_resolve(self):
        example = Problem('Oracle1')
        self.assertEqual(example.resolve_str(
        ) == 'Group of size 5 : [trace, crate, cater, carte, caret] \nGroup of size 4 : [beta, beat, bate, abet] \nGroup of size 4 : [tea, eta, eat, ate] \nGroup of size 1 : [displayed] \nGroup of size 1 : [singleton] \n', True)


unittest.main(argv=[''], verbosity=1, exit=False)
