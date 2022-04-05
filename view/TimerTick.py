''' Class TimerTick '''

class TimerTick:
    def __init__(self, text_box):
        self.text_box = text_box

    def ticker(self):
        self.text_box.value = int(self.text_box.value) + 1
        self.text_box.value.rjust(40)

    def get_tick_count(self):
        return self.text_box.value

# Reference for testing a class with python's DOCTEST
class TestMe:
    """ TEST CASES
    >>> a = TestMe()
    >>> a.sum_me(1,2)
    3
    >>> a.sum_me(1,0)
    1
    >>> a.sum_me(1,-1)
    0
    """            
    def sum_me(self, in_a, in_b):
        out = in_a + in_b
        return out
    
# import doctest # enable doctest
# doctest.testmod()