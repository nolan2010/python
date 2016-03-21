#!/usr/bin/env python

sentence = raw_input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width ) //2

print
print ' ' * left_margin + '+' + '-' * box_width + '+'
print ' ' * left_margin + '|' + ' ' * text_width  + '|'
print ' ' * left_margin + '|' +       sentence    + '|'
print ' ' * left_margin + '|' + ' ' * text_width  + '|'
print ' ' * left_margin + '+' + '-' * box_width  + '+'
print

#check function- use for  verification 
#database = [
#    ['nolan', '0929'],
#    ['jonan', '1053'],
#    ['lydia', '1132'],
#    ['ariel', '0217'] 
#] 
#username = raw_input('User name: ')
#pin = raw_input('PIN_code: ')
#
#if [username, pin] in database: print 'Access granted'
#






