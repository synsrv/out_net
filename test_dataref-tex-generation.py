
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as pl
from matplotlib import rc

matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath',
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}'
]  

import sys, os, itertools, pickle, utils



def test_dataref_gen():

    dpath = "./data/test/" +\
            "200410_140103_test_standard_net/" +\
            "builds/0000/raw"

    with open(dpath+'/namespace.p', 'rb') as pfile:
        nsp=pickle.load(pfile)


    fname = os.path.splitext(os.path.basename(__file__))[0]
    
    utils.generate_dataref_tex(nsp, '', fname)
 

    # fig.savefig("{}".format(fname)+'.pdf', dpi=300,
    #             bbox_inches='tight')




if __name__ == "__main__":

    test_dataref_gen()
    
