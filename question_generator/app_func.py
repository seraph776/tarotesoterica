#!/usr/bin/env python3
"""
created:10-22-2023 20:17:11
author:seraph★776
email:seraph776@gmail.com
project: Tarot Question Generator
"""
import random
import datetime
import random



def open_file(filename):
    with open(filename) as fo:
        res = [i.strip() for i in fo]
        res = sorted(res)
        return res


def color_text(t):
    return f"\033[33m{t}\033[0m"
    

def get_three_card_spread():
    s1 = ('past', 'present', 'future')
    s2 = ('create', 'sustain', 'destroy')
    s3 = ('mind', 'body', 'spirit')
    s4 = ('situation', 'problems', 'solutions')
    s5 = ('stop', 'start', 'continue')
    s6 = ('strengths', 'weaknesses', 'opportunities')
    s7 = ('situation', 'action', 'outcome')
    s8 = ('option #1', 'option #2', 'option #3')
    s9 = ('the good', 'the bad', 'the ugly')
    result = random.choice([s1, s2, s3, s4, s5, s6, s7, s8, s9])
    return result

def get_five_card_spread():
    s1 = ('the problem', 'mental resolve', 'emotional resolve', 'physical resolve', 'spirtual resolve')
    s2 = ('siutation', 'expectations ', 'what is hidden', ' near future', 'far future')
    s3 = ('siuation', 'positive energy', 'negative energy', 'what must be done', 'outcome')
    s4 = ('past', 'present', 'future', 'negative energy', 'positive energy')
    s5 = ('past', 'pesent', 'future', 'action', 'outcome')
    s6 = ('the good', 'the bad', 'the ugly', 'advice', 'outcome')
    result = random.choice([s1, s2, s3, s4, s5, s6])
    return result

def get_question():
    result = random.choice(open_file('questions.txt'))
    return result


def get_results():
    date_result = datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S')
    question = get_question()

    # three-card spread
    raw_three_card_spead = get_three_card_spread()
    three_card_1 = raw_three_card_spead[0].upper()
    three_card_2 = raw_three_card_spead[1].upper()
    three_card_3 = raw_three_card_spead[2].upper()

    
    # Alternate five-card spread
    raw_five_card_spead = get_five_card_spread()
    five_card_1 = raw_five_card_spead[0].upper()
    five_card_2 = raw_five_card_spead[1].upper()
    five_card_3 = raw_five_card_spead[2].upper()
    five_card_4 = raw_five_card_spead[3].upper()
    five_card_5 = raw_five_card_spead[4].upper()

    
   # Create spreads:
    three_card_spread = f'{three_card_1} | {three_card_2} | {three_card_3}'
    five_card_spread = f'{five_card_1} | {five_card_2} | {five_card_3} | {five_card_4} | {five_card_5}'
    

    result = f"""
    Date: {date_result}
    Question: {question}
    
    >>> Three-card spread: {three_card_spread}
    >>> Five-card spread: {five_card_spread}  
    """

    return result
