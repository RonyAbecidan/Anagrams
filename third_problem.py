#!/usr/bin/env python
# coding: utf-8

import random as rd
import unittest
import numpy as np
import textdistance


class Word:
    def __init__(self, string):
        self.string = string.lower()

    def shuffle(self):
        # random.shuffle works on list so we decompose our word in a list of
        # letters
        s_list = list(self.string)
        rd.shuffle(s_list)
        string = "".join(s_list)
        word = Word(string)  # and then we recompose the word
        return word

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

        first = self.string
        second = word.string
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

    def levenshtein(self, word):
        return textdistance.levenshtein(self.string, word.string)

    def correct(self, Dictionary):
        '''

        :param Dictionary: a reference Dictionary which can help us to find some suggestions if our word is incorrect.

        This function return a list of propositions of correction for the word considered, given a reference Dictionary

        We want to correct a word in two specific case:
        1 - The word looks like a real one, but, there is a problem in the order of the letters
        2 - The word looks like a real one, but some letters seem to be missing

        Here, we will try to see if we are in the first case using is_anagram. If it's the case,
        we will propose all the words from the dictionary which can be a correction for our mispelled word.

        If we are not in the first_case, we will see if at least, we can find words which are close to
        our mispelled word using the levenshtein distance.

        Else, we will return an empty list in order to mean that we didn't succeed in correcting the word given the dictionary
        '''

        word = self.string
        anagrams = []
        close_words = []
        dictionary = Dictionary.low
        for w in dictionary:
            if self.is_anagram(
                    w):  # if we find anagrams of our word which is actually in the reference dictionary
                anagrams.append(w)  # we add it to our list of anagrams
            if self.levenshtein(
                    w) <= 2:  # if we find a word in the dictionary which has at most 2 letters of difference than the incorrect word
                close_words.append(w)  # we add it to our list of close words
        if len(anagrams) != 0:
            return anagrams
        else:
            return close_words

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.string


# In[96]:


class Sentence:
    def __init__(self, list_of_words):
        self.low = list_of_words

    def to_string(self):
        if len(self.low) == 0:
            print('your sentence is the empty sentence')
        else:
            string = ''
            for word in self.low:
                # note that the final string will have a blank at the end (but
                # it's not a probleme here)
                string += word.string + ' '
            return string

    def list_of_strings(self):
        return [w.string for w in self.low]

    def correct(self, Dictionary):
        '''
        :param Dictionary: a Dictionary made of word which are uses as a reference for the correction

        This function try to correct the sentence considered, given a reference Dictionary.

        First, we see if there is a problem with some words in the sentence.

        If it's the case, we try to propose a correction of each incorrect word thanks to our previous work.

        If we don't succeed in finding corrections, the sentence is unchanged and the user is alerted
        '''

        # list of words which are incorrect and their positions in the sentence
        incorrect_words = np.array(Dictionary.incorrect_words(self))
        if len(incorrect_words) != 0:
            bool = True
            for i, word in incorrect_words:  # for each incorrect word
                # we try to find corrections
                correction = word.correct(Dictionary)
                number_of_corrections = len(correction)
                if number_of_corrections != 0:
                    proposition = ''
                    for correct_word in correction:
                        # we consider all the propositions
                        proposition = proposition + '/' + correct_word.string
                    # we remplace the incorrect word with our propositions
                    self.low[i] = Word(proposition[1:])
                # this boolean check if we didn't succeed in correcting any
                # single incorrect word.
                bool = bool and (number_of_corrections == 0)
            if bool:
                print("I can't correct this sentence, I am sorry")

    def to_sentence(self, string):
        list_of_strings = string.split(sep=" ")
        low = [Word(string) for string in list_of_strings]
        self.low = low

    def __repr__(self):
        return f"Sentence({str(self.low)})"


class Dictionary:
    def __init__(self, list_of_words):
        self.low = list_of_words

    def list_of_strings(self):
        return [w.string for w in self.low]

    def incorrect_words(self, sentence):
        '''
        :param sentence: a Sentence composed of words maybe different from the dictionary considered

        This function returns the words from the sentence entered which are not present in the dictionary considered.

        '''

        dictionary = self.list_of_strings()
        stce = sentence.list_of_strings()
        incorrect_words = []

        for i in range(len(stce)):  # for each word in the sentence
            current_word = stce[i]
            if not (
                    current_word in dictionary):  # is the current word in the dictionary ?
                # if not, we add it to a list with his position in the sentence
                incorrect_words.append((i, Word(current_word)))
        return incorrect_words

    def __repr__(self):
        return str(self.low)


# In[138]:


class Problem:
    def __init__(self, filename):
        self.filename = filename

    def parse(self, path='Oracles_3'):
        try:
            file = open(f"{path}/{self.filename}.txt", "r")
            number_of_lines = len(file.readlines())
            file.seek(0)
            list_of_words = []
            sentences = []
            cpt = 0
            current_word = file.readline().replace('\n', '')
            while not ('#' in current_word):
                list_of_words.append(Word(current_word))
                current_word = file.readline().replace('\n', '')
                cpt += 1

            # when we start to have the symbol "#"...
            for j in range(cpt, number_of_lines - 1):
                sentence = Sentence('')  # ...we start considering sentences
                string = file.readline().replace('\n', '')
                sentence.to_sentence(string)
                sentences.append(sentence)
            file.close()
            return Dictionary(list_of_words), sentences
        except BaseException:
            print("Please check the file (even its name) , there is something wrong")

    def resolve_str(self, path='Oracles_3'):
        dictionary, sentences = self.parse(path)
        final_result = ''
        if dictionary is not None:
            for i in range(len(sentences)):
                final_result += f"Sentence {i+1} : {sentences[i].to_string()} \n"
                sentences[i].correct(dictionary)
                final_result += f"Correction : {sentences[i].to_string()} \n \n"
        return final_result

    def resolve(self, path='Oracles_3'):
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

    def test_hamming(self):
        word_1 = Word('Rom')
        word_2 = Word('Room')
        word_3 = Word('Lucky')
        word_4 = Word('Luke')
        self.assertEqual(word_1.levenshtein(word_2), 1)
        self.assertEqual(word_1.levenshtein(word_3), 5)
        self.assertEqual(word_3.levenshtein(word_4), 2)

    def test_incorrect_words(self):
        example = [
            "Today",
            "I",
            ",",
            "will",
            "to",
            "the",
            "because",
            "am",
            "need",
            "a",
            "for",
            "my",
            "go",
            "watching",
            "from",
            "movie",
            "car",
            "room",
            "supermarket",
            "computer"]
        dictionary = Dictionary([Word(i) for i in example])
        list_1 = [
            "Today",
            ",",
            "I",
            "will",
            "go",
            "to",
            "the",
            "supermarket",
            "because",
            "I",
            "need",
            "a",
            "computer",
            "for",
            "my",
            "romo"]
        list_2 = ["I", "am", "watching", "a", "movie", "from", "my", "cra"]
        sentence_1 = Sentence([Word(i) for i in list_1])
        sentence_2 = Sentence([Word(i) for i in list_2])
        self.assertEqual(dictionary.incorrect_words(
            sentence_1)[0][1].string, 'romo')
        self.assertEqual(dictionary.incorrect_words(
            sentence_2)[0][1].string, 'cra')

    def test_correct_words(self):
        example = ["movie", "car", "room", "supermarker", "computer"]
        dictionary = Dictionary([Word(i) for i in example])
        word_1 = Word('Cra')
        word_2 = Word('Rom')
        self.assertEqual(word_1.correct(dictionary)[0].string, 'car')
        self.assertEqual(word_2.correct(dictionary)[0].string, 'room')

    def test_correct_sentence(self):
        example = [
            "Today",
            "I",
            ",",
            "will",
            "to",
            "the",
            "because",
            "am",
            "need",
            "a",
            "for",
            "my",
            "go",
            "watching",
            "from",
            "movie",
            "car",
            "room",
            "supermarket",
            "computer"]
        dictionary = Dictionary([Word(i) for i in example])
        list_1 = [
            "Today",
            ",",
            "I",
            "wll",
            "go",
            "to",
            "the",
            "supermarket",
            "becse",
            "I",
            "needl",
            "a",
            "computer",
            "for",
            "my",
            "romo"]
        list_2 = ["I", "am", "watchign", "a", "mvie", "from", "my", "cra"]
        sentence_1 = Sentence([Word(i) for i in list_1])
        sentence_2 = Sentence([Word(i) for i in list_2])
        sentence_1.correct(dictionary)
        sentence_2.correct(dictionary)
        self.assertEqual(
            sentence_1.to_string(),
            'today , i will go to the supermarket because i need a computer for my room ')
        self.assertEqual(
            sentence_2.to_string(),
            'i am watching a movie from my car ')


unittest.main(argv=[''], verbosity=1, exit=False)
