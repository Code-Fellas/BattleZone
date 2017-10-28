import requests

def f():
    key = 'hackerrank|1477209-1439|5df27efb8aaee3f89aaa2cfd77a809f0c9fd941b'
    url = 'http://api.hackerrank.com/checker/submission.json'
    d = {}

    code = '''for kohli in range(input()):
        n, m = map(int,raw_input().split())
        l = map(int,raw_input().split())
        print ([x%m for x in l]).count(0)
    '''

    d['source'] = code
    d['testcases'] = '["1\n2 3\n3 4 5"]'
    d['api_key']=key
    d['format']='json'
    d['lang']='5'
    re = requests.post(url,data=d)
    print re.json()


