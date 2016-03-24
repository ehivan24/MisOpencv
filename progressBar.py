'''
Created on Mar 19, 2015

@author: edwingsantos
'''

import sys

class progressbar(object):
    
    def __init__(self, finalCount, blockChar = '.'):
        self.finalCount = finalCount
        self.blockCount = 0
        self.block = blockChar
        self.f = sys.stdout
        if not self.finalCount: return
        self.f.write('\n ------------------ % Progress ------------------ \n')
        self.f.write('    1    2     3     4    5    6    7    8    9    0\n')
        self.f.write('---0---0---0---0---0---0---0---0---0---0---0---0---0\n')
    def progress(self, count):
        count = min(count, self.finalCount)
        if self.finalCount:
            percentcomplete =  int(round(100.0*count/self.finalCount))
            if percentcomplete < 1: 
                percentcomplete = 1
            else:
                percentcomplete = 100
            blockCount = int(percentcomplete//2)
            if blockCount <= self.blockCount:
                return
            for i in range(self.blockCount,  blockCount):
                self.f.write(self.block)
            self.f.flush()
            self.blockCount = blockCount
            if percentcomplete == 100:
                self.f.write('\n')


if __name__ == '__main__':
    
    from time import sleep
    import sys as SYS
    
    print " % Percent"
    
    for i in range(20):
        SYS.stdout.write('|')
        sleep(0.3)
    sleep(0.3)
    SYS.stdout.write(' complete')
        
    
    
    
    
    