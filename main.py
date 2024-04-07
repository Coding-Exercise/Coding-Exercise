import requests
import sys
import json
import re

def main():
    org = sys.argv[1]
    getRepositories(org)

def getRepositories(org):
    token = ""
    try:
        with open("token.txt") as my_file:
            token = my_file.read()
    except:
        print('token.txt not found')
    results = []
    
    if len(token) > 0:
        headers = {'Authorization': 'token ' + token}
    else:
        print('API token not found in token.txt')
        headers = ''
    link = f"https://api.github.com/orgs/{org}/repos?per_page=1000"
    while link:
        response = requests.get(link, headers = headers)
        for repo in response.json():
                results.append({
                    "repository": repo.get('name'),
                    "secret_scanning": repo.get('security_and_analysis').get('secret_scanning').get('status') if repo.get('security_and_analysis') else "Unavailable"
                })
        link = None
        if response.headers.get("Link"):
            match = re.search('(?<=<)([\S]*)(?=>; rel="Next")', response.headers.get("Link"), re.IGNORECASE)
            if match:
                link = match.group()
        
            

    # print(json.dumps(response.json(),indent=2)) 
    # print(response.json())
    
    
        # print(f"Repository name: {repo.get('name')} Secret scanning: {repo.get('security_and_analysis').get('secret_scanning').get('status')}")
    print(json.dumps(results, indent=4))
 
    # Writing to sample.json
    
        
    
    # print(f"Repository name: {repo.get('name')} Secret scanning: {repo.get('security_and_analysis').get('secret_scanning').get('status')}")
    # AttributeError: 'NoneType' object has no attribute 'get' -> cannot access other people's organisations
    # SOLUTION: pagination with items per page

'''
    What would you do when using the tool to extract data for lots of organisations without hitting the rate limit?
    
    How would you good runtime performance when extracting data for lots of organisations
    
    How would you schedule such a tool to monitor a set of organisations on regular basis
'''

if __name__ == '__main__':
    main()
