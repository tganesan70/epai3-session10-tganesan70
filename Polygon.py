##########################################################################
# Session10 assignment for EPAi3 - Module Polygon
#
# Ganesan Thiagarajan, 15th July 2021
##########################################################################
#
from functools import wraps
import math
from functools import lru_cache

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


class Polygon:
    """
    Class definition for a n-Polygon: creating a regular polygon of equal sides with n sides
    """

    @timed
    def __init__(self, s: 'No. of sides (int)' = 3, r: 'Circum radius' = 1):
        """
        Init for polygon class
        Args:
            s: No. of edges or vertices (integer) - default 3
            r: Circum radius, i.e., distance between the center and one of the vertices - default 1
        Returns: None - Initializes the object
            The class object with the following parameters initialized
                int_angle = (s-2) * 180.0/s  --> Interior angle
                edge_len = 2 * r * math.sin(math.pi/s)  --> length of one edge
                apothem = r * math.cos(math.pi/s)   --> distance between the center and line joining two vertices
                area = 0.5 * s * self.edge_len * self.apothem  --> area of the polygon
                perimeter = s * edge_len  --> Perimeter
                vertices = No. of vertices = no. of edges --> No of vertices
        """
        if s < 3:
            raise TypeError("No. of edges cannot be less than 3")

        self.edges = s
        self.radius = r
        self.int_angle = (s - 2) * 180.0 / s
        self.edge_len = 2 * r * math.sin(math.pi / s)
        self.apothem = r * math.cos(math.pi / s)
        self.area = 0.5 * s * self.edge_len * self.apothem
        self.perimeter = s * self.edge_len
        self.vertices = s

    def __repr__(self):
        print(f'Regular polygon with {self.edges} sides and circum radius = {self.radius}')
        print(f'The class object with the following parameters initialized')
        print(f'edges     --> No. of edges = {self.edges}')
        print(f'radius    --> circum radius = {self.radius}')
        print(f'int_angle --> Interior angle = {self.int_angle}')
        print(f'edge_len  --> length of one edge = {self.edge_len}')
        print(f'apothem   --> distance between the center and line joining two verticesi = {self.apothem}')
        print(f'area      --> area of the polygon = {self.area}')
        print(f'perimeter --> perimeter  = {self.perimeter}')
        print(f'vertices  --> No of vertices = {self.vertices}')

    def __eq__(self, other):
        """
        Checks whether two polygons are equal or not. The first polygon is self
        Args:
            other: The second polygon
        Returns:
            True if no. of sides and radius are equal else False
        """
        return True if (self.edges == other.edges and self.radius == other.radius) else False

    def __gt__(self, other):
        """
        Checks whether one of two polygons is greater than the other. The first polygon is self
        Args:
            other: The second polygon
        Returns:
            True if no. of sides of first is more than the second's
        """
        return True if (self.edges > other.edges) else False

# End of file