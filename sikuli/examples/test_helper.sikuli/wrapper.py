from __future__ import with_statement
from sikuli import *

class Wrapper:

    # If a file with the given filename already exists, the Logger will
    # just keep writing to the end of that file.
    def __init__(self, test_name="", filename="/vagrant/error_log"):
        self.file = filename
        self.test = test_name + ": "
        self.test_failed = False

    #################################
    # Wrappers for click, type, etc
    #################################

    # Return True on success, False on FindFailed error, after
    # logging the error.

    def Click(self, thing, message, time=1):
        try:
            click(thing)
            wait(time)
            return True
        except FindFailed, ff:
            self.write_error(message)
            return False
        except:
            raise
    
    def DoubleClick(self, thing, debug=0, time=1):
        try:
            doubleClick(thing)
            wait(time)
            return True
        except FindFailed, ff:
            self.write_error(message)
            return False
        except:
            raise
    
    def Type(self, text, time=1):
        type(text)
        wait(time)
    
    def Find(self, thing, debug=0, time=1):
        try:
            find(thing)
            wait(time)
            return True
        except FindFailed, ff:
            self.write_error(message)
            return False
        except:
            raise
    
        def offset(self, x, y):
            return offset(Location(x, y))

    ###################
    # Logging methods
    ###################

    # Prepends the test name and appends a newline before writing to file.
    def write(self, line):
        with open(self.file, "a") as f:
            f.write(self.test + line + "\n")

    # Same as write, but internally remembers that the test failed.
    def write_fail(self, line):
        self.test_failed = True
        self.write(line)

    # Returns whether any fails have been logged.
    def has_fail(self):
        return self.test_failed