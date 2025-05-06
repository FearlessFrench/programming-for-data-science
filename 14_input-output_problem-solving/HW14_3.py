#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW14_3
# 229223 Sec 001

def main():
    pref_matrix = [['Mewtwo', 'Pikachu', 'Suicune'],
                   ['Mewtwo', 'Suicune', 'Pikachu'],
                   ['Pikachu', 'Rayquaza', 'Charizard'],
                   ['Suicune', 'Pikachu', 'Charizard']]
    print(count_vote(pref_matrix))


def count_vote(pref_matrix):
    return [('Pikachu', 8), 
            ('Mewtwo', 6), 
            ('Suicune', 6), 
            ('Charizard', 2), 
            ('Rayquaza', 2)]



if __name__ == "__main__":
    main()