#!/usr/bin/env python3

def return_evens(num_list):
    #interesting that n is needed at the start, and if without par
    new_list = [n for n in num_list if n % 2 == 0]
    return new_list

def make_exclamation(sentence_list):
    new_list = [n + "!" for n in sentence_list if n != None]
    return new_list