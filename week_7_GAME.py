#!user/bin/env python
# -*- coding: utf-8 -*-
"""
This module shows the creation of a simple game called Pig.
"""

import random


class Die(object):
    """the die which has 6 sides"""
    def __init__(self):
        self.die = 0

    def roll(self):
        self.die = random.randint(1, 6)
        return self.die


class Player(object):
    """constructor for the players"""
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.turns_score = 0
        self.turn = 0
    
    
class Game(object):
    """Constructor for Pig Game"""
    def __init__(self, player1, player2):  
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.die = Die()
        self.turn(self.player1)
    
    def turn(self, player):
        """A players turn"""
        player.turn = 1
        print '\nit is Player {}\'s turn'.format(player.name)
        while player.turn == 1 and player.total_score < 100:
            r = self.die.roll()
            print '\nyou rolled a {}\n'.format(r)
            if r == 1:
                player.turns_score = 0
                print ('oops! you rolled a 1, '
                       'next player.\n').format(player.name, player.total_score)
                print '-' * 60, '\n'
                self.next_player()
            else:
                player.turns_score += r
                print 'your total this turn is {}\n'.format(player.turns_score)
                self.player_ans(player)
        print ('{} is the winner '
               'with a score of {}!').format(player.name, player.total_score)
               
    def player_ans(self, player):
        """players answer to his roll"""
        ans = raw_input('would you like to roll again? '
                        'r = roll h = hold ').lower()
        if ans == 'h':
            player.total_score += player.turnscore
            print '\nyour turn is now over.\n'
            if player.total_score >= 100:
                print ('{} wins.').format(player.name, player.total_score)
            else:
                player.turns_score = 0
                print ('{}\'s total score is'
                       ' now {}.\n\n').format(player.name, player.total_score)
                print '-' * 60, '\n'
                self.next_player()
        elif ans == 'r':
            self.turn(player)
        else:
            print 'Invalid option, r = roll h = hold '
            self.player_ans(player)     
                
    def next_player(self):
        """initiates next players turn"""
        if self.player1.turn == 1:
            self.player1.turn = 0
            self.turn(self.player2)
        else:
            self.player2.turn_status = 0
            self.turn(self.player1)
            
def main():
    """initiates the program"""
    print 'welcome to pig'
    raw_input('press enter to begin rolling!')

main()
Game('player 1', 'player 2')
