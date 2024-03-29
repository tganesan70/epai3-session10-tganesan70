##########################################################################
# Session10 assignment for EPAi3 - Module PolygonSeq
#
# Ganesan Thiagarajan, 15th July 2021
##########################################################################
#
from functools import wraps
import math
from functools import lru_cache
from Polygon import *

# Timed decorator for all functions - but using a global variable for elapsed time in case we want it at __main__ level
elapsed_time = 0


def timed(fn: 'Function name') -> 'Time for execution of the function':
    """
    A function decorator to compute the execution time for all the functions in this module when called
    from the test script.
    Params:
    fn - Function name
    Returns:
        Time for execution in seconds
    """
    from time import perf_counter
    @wraps(fn)
    def inner(*args, **kwargs):
        global elapsed_time
        start_time = perf_counter()
        result = fn(*args, **kwargs)
        end_time = perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function {fn.__name__}() took {elapsed_time} secs to execute")
        return result

    return inner


# Function decorator for checking the docstring of functions
def check_doc_string(
        fn: 'Function name that needs to be parsed') -> 'Returns True if the function has 50 words of description':
    """
    This function checks whether the function passed on to this has atleast 50 words of
    description.
    :param fn: Function name that is passed to this function
    :return: Returns a closure which allows the free variables can be accessed later
             The inner function Returns True if it has 50 or more words in its docstring description, else False
    Question: Will the docstring include the argument description function as well?  A BIG NO!
    """
    comment_len = 50
    """
    Doc string for inner function
    :param args: Positional arguments for the function
    :param kwargs:Function arguments for the function
    :return: The function output
    """
    if fn.__doc__ is None:
        return False
    else:
        fn_doc_string = fn.__doc__.split(sep=" ")
        # print(f'No. of words in the docstring comment for {fn.__name__}() is : {len(fn_doc_string)}')
        if len(fn_doc_string) < comment_len:
            return False
        else:
            return True

class PolygonSeq(Polygon):
    """
    Polygon sequence class derived from the polygon class object
    """

    def __init__(self, n, r):
        """
        Creates a polygon sequence with the largest polygon with n sides and r radius
        Also computes the maximum efficiency polygon which has the highest area to perimeter ratio
        Args:
            n: Maximum no. of edges or sides
            r: Circum radius of all polygons
        """
        self.n = n  # Maximum no. of polygon available in the sequence
        self.r = r
        self.max_eff_n = 3
        self.max_eff = 0
        self.curr_poly = n  # default polygon index

        max_eff = 0
        for i in range(3, n + 1):
            temp_poly = self._polygon(i, r)
            eff = temp_poly.area / temp_poly.perimeter
            if self.max_eff < eff:
                self.max_eff = eff
                self.max_eff_n = i

    @staticmethod
    @lru_cache(maxsize=100)
    def _polygon(s, r):
        """
        Computes the polygon of given order and radius
        Args:
            s: Polygon order
            r: Circum radius of the polygon
        Returns:
            The polygon class object
        """
        return Polygon(s, r)

    def __repr__(self):
        """
        Gives the description of the PolygonSeq class objects.
        Returns:
            Print statement of the length (maximum order), radius and the maximum efficiency polygon
        """
        print(f'Polygon sequence of length = {self.n} with radius = {self.r}')
        print(f'The maximum efficiency polygon is with edges = {self.max_eff_n}')
        print(f'The maximum efficiency (area/perimeter) is {self.max_eff}')

    def __len__(self):
        """
        Returns the length of the polygon sequence. The length refers to the maximum order in the sequence
        Returns:
            The highest polygon order
        """
        return self.n

    def __getitem__(self, s):
        """
        Gets the polygon of order s
        Args:
            s: The order of the polygon
        Returns:
            The polygon of order s
        """
        if isinstance(s, int):
            if s < 3 or s > self.n:
                raise IndexError
            else:
                return self._polygon(s, self.r)

    def _next(self):
        """
        Return the next polygon in the sequence.
        The polygon class object which is next in the sequence is returned.
        The current sequence number is updated.
        """
        if self.curr_poly < self.n:
            self.curr_poly += 1
            return self.__getitem__(self.curr_poly)
        else:
            print("Reached the end of sequence")
            return self.__getitem__(self.n)
            # raise IndexError

    def _prev(self):
        """
        Return the previous polygon in the sequence
        The polygon class object which is previous in the sequence is returned.
        The current sequence number is updated.
        """
        if self.curr_poly >= 4:
            self.curr_poly -= 1
            return self.__getitem__(self.curr_poly)
        else:
            print("Reached start of sequence")
            return self.__getitem__(3)
            # raise IndexError
