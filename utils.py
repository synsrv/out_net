
import brian2
from brian2.units import second, ms

def generate_dataref_tex(nsp, prefix, fname, fname_postfix=''):
    '''
    '''

    with open(fname +'_params'+fname_postfix+'.tex', 'w') as tfile:

        params = [{'name'   : 'tau_e',
                   'dim'    : ms,
                   'siunitx': 'ms'},
                  {'name'   : 'N_e',
                   'dim'    : 1,
                   'siunitx': None}]
                  

        for prm in params:

            if isinstance(prm['dim'], brian2.Unit):
                
                tfile.write(r"\drefset[unit=" + prm['siunitx']+r"]{/" +\
                            prm['name']+r"}{"+ \
                            str(nsp[prm['name']]/prm['dim'])+r"}"+"\n")

            else:
                tfile.write(r"\drefset{/" +\
                            prm['name']+r"}{"+ \
                            str(nsp[prm['name']]/prm['dim'])+r"}"+"\n")



                
        # for key,item in nsp.items():
        #     # Example:
        #     #
        #     #   \drefset[unit=ms]{/duration}{5}
        #     #
        #     if type(item) is int:
        #         pass
        #     elif type(item) is float:
        #         pass
        #     elif type(item) is str:
        #         pass
        #     elif type(item) is bool:
        #         pass
        #     elif isinstance(item, brian2.Quantity):
        #         print(item.dim)
        #         print(brian2.in_best_unit(item))

        #     #tfile.write(r"\drefset{/"+key+r"}["+str(item)+r"]"+"\n")
        


