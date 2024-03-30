import requests
import sys
import json
    # -H "Accept: application/vnd.github+json" \
    # -H "Authorization: Bearer <YOUR-TOKEN>" \
    # -H "X-GitHub-Api-Version: 2022-11-28" \
    # https://api.github.com/orgs/ORG/repos


def main():
    org = sys.argv[1]
    getRepositories(org)



def getRepositories(org):
    token = ""
    with open("token.txt") as my_file:
        token = my_file.read()
    
    headers = {'Authorization': 'token ' + token}

    response = requests.get(f"https://api.github.com/orgs/{org}/repos", headers = headers)
    # print(json.dumps(response.json(),indent=2)) 
    for repo in response.json():
        print(f"Repository name: {repo.get('name')} Secret scanning: {repo.get('security_and_analysis').get('secret_scanning').get('status')}")
    
    # print(f"Repository name: {repo.get('name')} Secret scanning: {repo.get('security_and_analysis').get('secret_scanning').get('status')}")
    # AttributeError: 'NoneType' object has no attribute 'get' -> cannot access other people's organisations
    # SOLUTION: pagination with items per page

if __name__ == '__main__':
    main()