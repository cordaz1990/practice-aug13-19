#Global Variables

verbose = True

def examples():
    if verbose:
      print('Running example')
      
been_called = False

def example2():
    been_called = True
    
been_called = False 

def example2():
    global been_called
    been_called = True
