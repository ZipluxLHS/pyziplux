msgFormat = '''
@%@
---------------------------------------------
|{}
---------------------------------------------
{}
---------------------------------------------
%@%

'''

class msg:
    def __init__(self):
        self.beat = 0
    def info(self, tagName='', tag='', beat=0):
        if beat!=0:
            self.beat=beat
        print(msgFormat.format(tagName, tag).replace('@%@', '{}:INFO>>>>>>>>>>>>>>>>>>'.format(self.beat)).replace('%@%', '{}:INFO<<<<<<<<<<<<<<<<<<'.format(self.beat)))
        self.beat+=1
    def getBeat():
        return self.beat