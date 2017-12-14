# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:07:10 2017

@author: Lorango

"""

import pygame
import natrix


def kobila(a, b=1):
    pygame.mouse.set_pos([0, 0])
    print(a, b)


class StringVar():
    """Docstring
        kokoša **je mala**
    """
    def __init__(self, value='stringvar'):
        self.value = str(value)
        self._set(value)

    def _set(self, value='stringvar'):
        self.value = str(value)

    def get(self):
        return self.value


class Label(natrix.predmet.Predmet):
    """Docstring

    """
    def __init__(self, rect=(0, 0, 80, 80), text='label', string_var=None):
        natrix.predmet.Predmet.__init__(self, rect, None)

        self.text = str(text)
        self.string_var = string_var

        self.image = natrix.font_def.render(text, False,
                                            natrix.blue)

        self.rect.size = self.image.get_rect().size

    def step(self):
        """Docstring

        """
        if self.string_var is not None:
            self.image = natrix.font_def.render(self.string_var.get(), False,
                                                natrix.blue)
            self.rect.size = self.image.get_rect().size


class Button(natrix.predmet.Predmet):
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
    def __init__(self, rect=(0, 0, 80, 80), function=print, args={}, image_name=None):

        natrix.predmet.Predmet.__init__(self, rect, image_name)

        self.function = function
        self.args = args

        self.disabled = False

    def lmb_up(self):
        """Docstring

        """
        print('button')
        if not self.disabled:
            self.function(**self.args)
