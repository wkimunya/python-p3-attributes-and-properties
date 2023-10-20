#!/usr/bin/env python3

from person import Person
import io
import sys

class TestPerson:
    def test_is_class(self):
        guido = Person(name='Guido', job='Sales')
        assert isinstance(guido, Person)

    def test_name_not_empty(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="", job="Sales")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n"

    def test_name_not_string(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name=123, job='Sales')
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n"

    def test_valid_name(self):
        guido = Person(name='Guido', job='Sales')
        assert guido.name == 'Guido'

    def test_valid_job(self):
        guido = Person(name='Guido', job='Sales')
        assert guido.job == 'Sales'

    def test_invalid_job(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name='Alice', job='Engineering')
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Job must be in the list of approved jobs.\n"

if __name__ == '__main__':
    tester = TestPerson()
    tester.test_is_class()
    tester.test_name_not_empty()
    tester.test_name_not_string()
    tester.test_valid_name()
    tester.test_valid_job()
    tester.test_invalid_job()

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="What do Persons do on their day off? Can't lie around - that's their job.",
               job='Sales')
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        guido = Person("Guido")
        assert(guido.name == "Guido")

    def test_valid_name_title_case(self):
        '''converts name to title case and saves if between 1 and 25 characters'''
        guido = Person(name="guido van rossum")
        assert(guido.name == "Guido Van Rossum")

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(job="Benevolent dictator for life")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Job must be in list of approved jobs.\n")

    def test_job_in_list(self):
        '''saves job if in job list.'''
        guido = Person(job="ITC")
        assert(guido.job == "ITC")
