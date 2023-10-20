#!/usr/bin/env python3

from dog import Dog
import io
import sys

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog".'''
        fido = Dog()
        assert isinstance(fido, Dog)
        
    def test_name_not_empty(self):
        '''raises ValueError with message "Name must be string between 1 and 25 characters." if empty string.'''
        try:
            Dog(name="")
        except ValueError as e:
            assert str(e) == "Name must be a string between 1 and 25 characters."

    def test_name_string(self):
        '''raises ValueError with message "Name must be string between 1 and 25 characters." if not string.'''
        try:
            Dog(name=123)
        except ValueError as e:
            assert str(e) == "Name must be a string between 1 and 25 characters."

    def test_name_under_25(self):
        '''raises ValueError with message "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        try:
            Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")
        except ValueError as e:
            assert str(e) == "Name must be a string between 1 and 25 characters."

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        fido = Dog(name="Fido")
        assert fido.name == "Fido"

    def test_breed_not_in_list(self):
        '''raises ValueError with message "Breed must be in the list of approved breeds." if not in breed list.'''
        try:
            Dog(breed="Human")
        except ValueError as e:
            assert str(e) == "Breed must be in the list of approved breeds."

    def test_breed_in_list(self):
        '''saves breed if in breed list.'''
        fido = Dog(breed="Pug")
        assert fido.breed == "Pug"
