# tasks.py
import time
from celery import Celery
 
celery = Celery( 'tasks', broker = 'redis://localhost:6379/0' )
print celery
 
@celery.task
def sendmail( mail ):
    print( 'sending mail to %s...' % mail['to'] )
    time.sleep( 2.0 )
    print( 'mail sent.' )
    
    

from matplotlib import pyplot

import numpy as np, numpy.linalg as nplg



rets = np.array( [ 1, 2, 4, 8, 16, 32, 64, 128, 256] )
freqs = np.array( [ 0., 0.69314718, 1.09861229, 1.38629436, 1.60943791,
        1.79175947, 1.94591015, 2.07944154, 2.19722458] )


pyplot.plot( rets, freqs, 'o' )
pyplot.plot( rets, freqs[0] * rets + freqs[1] )
pyplot.show()
