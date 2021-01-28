
#pytest test_pdb.py

import pdb

#pdb.set_trace()

def test_Hi2():
    print('hi1..')
    pdb.set_trace()
    print('hi2..')
    assert(0==1)

print('end.')

