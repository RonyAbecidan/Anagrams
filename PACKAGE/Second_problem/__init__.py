#!/usr/bin/env python
# coding: utf-8

import random as rd
import unittest
import itertools
import numpy as np


class Sentence:
    def __init__(self, list_of_words):
        self.low = list_of_words

    def shuffle(self):
        low = self.low.copy()
        rd.shuffle(low)
        new_sentence = Sentence(low)
        return new_sentence

    def tuple_to_sentence(self, tup):
        low = []
        for i in range(len(tup)):
            low.append(tup[i])
        self.low = low

    def to_string(self):
        if len(self.low) == 0:
            print('your sentence is the empty sentence')
        else:
            string = ''
            for word in self.low:
                # note that the final string will have a blank at the end (but
                # it's not a probleme here)
                string += word + ' '
            return string

    def to_sentence(self, string):
        self.low = string.split(sep=" ")

    def is_equivalent(self, sentence):
        low1 = self.low.copy()
        low2 = sentence.low.copy()
        low1.sort()
        low2.sort()
        return (low1 == low2)

    def in_common(self, word):
        sentence = self.to_string().lower()
        word = word.lower()  # we don't consider the uppercase
        bool = True
        for i in range(0, len(word)):
            bool = bool and (word[i] in sentence)
        return bool

    def is_anagram(self, Sentence2):
        ''' To check if two sentences are anagram of each other we will procede like this :

        First, we tranform them into string but, we replace the spaces with nothing : The words are attached to each other.

        Example : Sentence("hello world") becomes "Helloworld"

        Then, we procede just as the first problem with the two strings generated before.

        We check if they have the same length. If it's the case...

        We take the first letter of the first string and we check if it's present in the second one.

        If it's not, we can conclude that the two sentences aren't anagrams

        If it's the case, we delete the first occurence of the letter considered in the second string and we continue with the

        next letter of the first string.

        Finally, we continue like that until the end of the first string considered.

        Note : We will not take in account the uppercase for this exercise and so we will consider that
        two sentences made of the exact same letters (even if some of them are maybe uppercases) are anagrams
        '''

        first = self.to_string().replace(" ", "")
        second = Sentence2.to_string().replace(" ", "")
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

    def __repr__(self):
        return f"Sentence({str(self.low)})"


# In[2]:


class Dictionary:
    def __init__(self, list_of_words):
        self.low = list_of_words

    def alphabetic(self):
        self.low.sort()

    def find_sentences(self):
        ''' To find all the sentences we can built with the words (ordered in alphabetic order) from the dictionary,
         we start to order alphabeticly the dictionary we consider.

         Then, we create all the subsets of words ordered alphabeticly of our dictionary.

         For that, we will use list(itertools.combinations(dictionary, i)) which returns,
         all the subsets of words of size i of the dictionary, while preserving the order of the words existing within it.

         This subsets are returned as tuples so we will have to use our function tuple_to_sentence in order to tranform them to sentences.

        '''
        Sentences = []
        self.alphabetic()
        dictionary = self.low
        for i in range(1, len(dictionary)):
            subsets = list(itertools.combinations(dictionary, i))
            for j in range(len(subsets)):
                sentence = Sentence([''])
                sentence.tuple_to_sentence(subsets[j])
                Sentences.append(sentence)
        return Sentences

    def all_anagrams(self, sentence):
        '''In order to find all the anagrams of a sentence, we will proceed like this :

        - First we create a dictionary made of all the words from our initial dictionary which share all their letters
        present in the sentence that we consider

        -Then, we create all the possible sentence from this new dictionary

        - At last, we create a list of anagrams which will contains all the sentences generated before which are anagrams of
        the sentence we entered and, which not share the same words with that sentence

        '''

        dictionary = self.low
        final_dictionary = []
        anagrams = []
        for word in dictionary:
            if sentence.in_common(
                    word):  # if the word share all its letters with the sentence
                final_dictionary.append(word)

        final_dictionary = Dictionary(final_dictionary)
        sentences = final_dictionary.find_sentences()

        for s in sentences:
            if s.is_anagram(sentence) and not(s.is_equivalent(
                    sentence)):  # we don't want to return the same words in the output
                anagrams.append(s.to_string())
        anagrams.sort()
        return anagrams

    def __repr__(self):
        return str(self.low)


class Problem:
    def __init__(self, filename):
        self.filename = filename

    def parse(self, path='Oracles_2'):
        try:
            file = open(f"{path}/{self.filename}.txt", "r")
            number_of_lines = len(file.readlines())
            file.seek(0)
            list_of_words = []
            sentences = []
            cpt = 0
            current_word = file.readline().replace('\n', '')
            while not ('#' in current_word):
                list_of_words.append(current_word)
                current_word = file.readline().replace('\n', '')
                cpt += 1

            # when we start to have the symbol "#"...
            for j in range(cpt, number_of_lines - 1):
                sentence = Sentence([''])  # ...we start considering sentences
                string = file.readline().replace('\n', '')
                sentence.to_sentence(string)
                sentences.append(sentence)
            file.close()
            return Dictionary(list_of_words), sentences
        except BaseException:
            print("Please check the file (even its name) , there is something wrong")

    def resolve_str(self, path='Oracles_2'):
        dictionary, sentences = self.parse(path)
        final_result = ''
        if dictionary is not None:
            for i in range(len(sentences)):
                all_anagrams = dictionary.all_anagrams(sentences[i])
                for j in range(len(all_anagrams)):
                    final_result = final_result + \
                        f"{sentences[i].to_string()} =  {all_anagrams[j]}" + "\n"
        return final_result

    def resolve(self, path='Oracles_2'):
        if self.resolve_str(path) is not None:
            print(self.resolve_str(path))


class TestMethods(unittest.TestCase):

    def test_to_string(self):
        first_sentence = Sentence(['Hello', 'my', 'name', 'is', 'john'])
        self.assertEqual(first_sentence.to_string(), "Hello my name is john ")

    def test_to_sentence(self):
        string = 'Hello my name is john'
        sentence = Sentence([''])
        sentence.to_sentence(string)
        self.assertEqual(sentence.to_string(), string + ' ')

    def test_in_common(self):
        first_sentence = Sentence(['Hello', 'my', 'name', 'is', 'john'])
        word_1 = "hello"
        word_2 = "abracadabra"
        self.assertEqual(first_sentence.in_common(word_1), True)
        self.assertEqual(first_sentence.in_common(word_2), False)

    def is_equivalent(self):
        sentence_1 = Sentence(['Hello', 'my', 'name', 'is', 'john'])
        sentence_2 = Sentence(['Hello', 'my', 'name', 'is', 'barbara'])
        self.assertEqual(sentence_1.is_equivalent(sentence_2), False)
        self.assertEqual(sentence_1.is_equivalent(sentence_1.shuffle()), False)

    def test_is_anagram(self):
        sentence_1 = Sentence(["SXZYTWQP", "KLJ", "YRTD"])
        sentence_2 = Sentence(["DXZ", "K", "LJSRT", "PTYYWQ"])
        sentence_3 = Sentence(['Hello', 'my', 'name', 'is', 'john'])
        sentence_4 = Sentence1.shuffle()
        self.assertEqual(sentence_1.is_anagram(sentence_2), True)
        self.assertEqual(sentence_2.is_anagram(sentence_3), False)
        self.assertEqual(sentence_2.is_anagram(sentence_4), True)

    def test_all_anagrams(self):
        example = Dictionary(["ABC",
                              "AND",
                              "DEF",
                              "DXZ",
                              "K",
                              "KX",
                              "LJSRT",
                              "LT",
                              "PT",
                              "PTYYWQ",
                              "Y",
                              "YWJSRQ",
                              "ZD",
                              "ZZXY"])
        sentence = Sentence(["SXZYTWQP", "KLJ", "YRTD"])
        self.assertEqual(example.all_anagrams(sentence),
                         ['DXZ K LJSRT PTYYWQ ',
                          'DXZ K LT PT Y YWJSRQ ',
                          'KX LJSRT PTYYWQ ZD ',
                          'KX LT PT Y YWJSRQ ZD '])

    def test_resolve_str(self):
        problem_2 = Problem('example')
        self.assertEqual(
            problem_2.resolve_str(),
            'SXZYTWQP KLJ YRTD  =  DXZ K LJSRT PTYYWQ \nSXZYTWQP KLJ YRTD  =  DXZ K LT PT Y YWJSRQ \nSXZYTWQP KLJ YRTD  =  KX LJSRT PTYYWQ ZD \nSXZYTWQP KLJ YRTD  =  KX LT PT Y YWJSRQ ZD \n')


unittest.main(argv=[''], verbosity=1, exit=False)
