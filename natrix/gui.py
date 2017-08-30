# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:07:10 2017

@author: Lorango

"""

import natrix

def kobila(a, b=1):
    print(a, b)

class Button(natrix.sprite.Sprite):
    """Služi kao gui objekt čijom se aktivacijum izvršava zadana funkcija.

    .. note:: Deprecated in NumPy 1.6.0
          `ndobj_old` will be removed in NumPy 2.0.0, it is replaced by
          `ndobj_new` because the latter works also with array subclasses.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    Examples
    --------
    >>> func(1, "a", x , `x` )
    True

        dff
    See Also
    --------
    average : Weighted average

    a : asd
    """
    def __init__(self, rect=(0, 0, 80, 80), function=print, args={}):

        natrix.sprite.Sprite.__init__(self, rect, None)

        self.function = function
        self.args = args

        self.disabled = False

    def lmb_up(self):
        """Docstring

        """
        print('button')
        if not self.disabled:
            self.function(**self.args)
