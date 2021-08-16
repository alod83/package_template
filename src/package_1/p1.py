from numpy.random import seed
from numpy.random import rand

def p1_sum(a, s = 1):
    """
    Add a random number to the number passed as parameter

    Parameters
    ----------
    a : float or int
        the first number to be summed
    s : int
        the seed used to generate the random number
    
    Returns
    -------
    int or float
        The sum of a and and a random number
    """
    # seed random number generator
    seed(s)

    b = rand(1)

    return a + b

