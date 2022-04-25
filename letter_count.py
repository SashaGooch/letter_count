# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 01:51:16 2022

@author: gocan
"""

dostoevsky = 'It’s not worth the tears of that one tortured child who beat itself on the breast with its little fist and prayed in its stinking outhouse, with its unexpiated tears to “dear, kind God”! It’s not worth it, because those tears are unatoned for. They must be atoned for, or there can be no harmony. But how? How are you going to atone for them? Is it possible? By their being avenged? But what do I care for avenging them? What do I care for a hell for oppressors? What good can hell do, since those children have already been tortured? And what becomes of harmony, if there is hell? I want to forgive. I want to embrace. I don’t want more suffering. And if the sufferings of children go to swell the sum of sufferings which was necessary to pay for truth, then I protest that the truth is not worth such a price. I don’t want the mother to embrace the oppressor who threw her son to the dogs! She dare not forgive him! Let her forgive him for herself, if she will, let her forgive the torturer for the immeasurable suffering of her mother’s heart. But the sufferings of her tortured child she has no right to forgive; she dare not forgive the torturer, even if the child were to forgive him! And if that is so, if they dare not forgive, what becomes of harmony? Is there in the whole world a being who would have the right to forgive and could forgive? I don’t want harmony. From love for humanity I don’t want it. I would rather be left with the unavenged suffering. I would rather remain with my unavenged suffering and unsatisfied indignation, even if I were wrong. Besides, too high a price is asked for harmony; it’s beyond our means to pay so much to enter on it. And so I hasten to give back my entrance ticket, and if I am an honest man I am bound to give it back as soon as possible. And that I am doing. It’s not God that I don’t accept, Alyosha, only I most respectfully return him the ticket.'

letter_count = {}

for letter in dostoevsky:
    letter_count[letter.lower()] = letter_count.get(letter,0)+1
    print(letter_count)
    
letter_count.items()

import matplotlib.pyplot as plt

letter_count_clean = {}

for k,v in letter_count.items():
    if k.isalpha():                     # letters only no symbols punctuation
        letter_count_clean[k] = v
        print(letter_count_clean)

x,y = zip(*letter_count.items())
plt.bar(x,y)
plt.show()

from collections import Counter
print(Counter(dostoevsky.lower()))

new_dict = dict(Counter(dostoevsky.lower()))

new_dict = {k:v for k,v in new_dict.items() if k.isalpha()}
print(new_dict)

x,y = zip(*new_dict.items())
plt.bar(x,y)
plt.show()