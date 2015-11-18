#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """
    Simple logger class
    """
    def __init__(self, logfilename):
        """
        Constructor
        Args:
            logfilename (String): Full path of log file
        Returns:
            None
        Examples:
            >>> myvar = CustomLogger('/a/b/c/d/mylog.txt')
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """
        Log messages buffer
        Args:
            msg (String): Message to append to the log
            timestamp (Time): Unix timestamp
        Returns:
            None
        Examples:
            >>> my_inst = CustomLogger('/p/a/t/h/t/o/log.txt')
            >>> my_inst.log('Who\'s your daddy?')
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """
        Flushes log buffer to storage
        Args:
            self: Instance object
        Returns:
            None
        Examples:
            >>> my_inst = CustomLogger('/p/a/t/h/t/o/log.txt')
            >>> my_inst.log('Luke, I\'m your father.')
            >>> my_inst.flush()
        """
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                except Exception:
                    self.log('Could not write to ' + self.logfilename)
                    raise IOError('File write error')
                else:
                    handled.append(index)
        except Exception:
            self.log('Could not open ' + self.logfilename)
            raise IOError('File open error')
        else:
            fhandler.close()
            for index in handled[::-1]:
                del self.msgs[index]
