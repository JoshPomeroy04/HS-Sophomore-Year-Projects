def add_em_up(a, b, c):
   """
     >>> add_em_up(1, 1, 1)
     3
     >>> add_em_up(3, 8, 5)
     16
     >>> add_em_up(-2, -2, 4)
     0
     >>> s = add_em_up(3, 5, 9)
     >>> s
     17
   """
   return a + b + c


if __name__ == '__main__':
   import doctest
   doctest.testmod()

