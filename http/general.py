class cURL:
    def __init__(self, url_='.'):
        self.url = url_
        
    def replace(self, replaceURL_, start_, end_):
        '''
        example: 'https://www.google.com/search'
        https:// -> -1
        www.google.com -> 0
        search -> 1
        '''
        if start_ == -1:
            start_ = 0
        else:
            start_ +=2
        end_ += 2
        
        urllist = self.url.split('/')
        wrongURL = '/'.join(urllist[start_:end_])
        
        newURL= self.url.replace(wrongURL,replaceURL_)
        return newURL
    