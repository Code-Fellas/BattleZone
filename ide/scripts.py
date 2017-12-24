import requests
from ide.models import Languages

def f():
    key = 'hackerrank|1477209-1439|5df27efb8aaee3f89aaa2cfd77a809f0c9fd941b'
    url = 'http://api.hackerrank.com/checker/submission.json'
    d = {}

    code = '''
#include<iostream>
using namespace std;

int main(){
	long long a,b;
	long long sum=0;
    cin>>a>>b;
	cout<<a+b
	return 0;
}
    '''
    print code
    d['source'] = code
    testcases = str(['2 3','3 4','10 0','0 0','1000000000 1000000000'])
    d['testcases'] = testcases
    d['api_key']=key
    d['format']='json'
    d['lang']='2'
    re = requests.post(url,data=d)
    print re.json()


def insert_internal_codes():
    url = 'http://api.hackerrank.com/checker/languages.json'
    languages_data = requests.get(url).json()['languages']

    for language, code in languages_data['codes'].iteritems():

        Languages.objects.create(
            display_name = languages_data['names'][language],
            language_code = code,
            hackerrank_name = language
        )
        print(language)
