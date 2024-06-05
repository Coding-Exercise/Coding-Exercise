import requests
import sys
import json
import re

def main():
    org = sys.argv[1]
    get_repositories(org)

def get_repositories(org):
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
                    "secret_scanning": repo.get('security_and_analysis').get('secret_scanning').get('status') if repo.get('security_and_analysis') else "unavailable"
                })
        link = None
        if response.headers.get("Link"):
            match = re.search('(?<=<)([\S]*)(?=>; rel="Next")', response.headers.get("Link"), re.IGNORECASE)
            if match:
                link = match.group()

    print(json.dumps(results, indent=4))

if __name__ == '__main__':
    main()
