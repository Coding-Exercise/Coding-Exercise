# Instructions

## How to run

1. Clone the repository
2. Install requirements.txt
```
pip3 install -r requirements.txt
```
3. Create token.txt and add GitHub API token to it
4. Run main.py and pass your desired organisation
```
python3 main.py eclipse-cbi
```

 
### Note: 
[Per the documentation,](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-organization-repositories) in order to see the security_and_analysis block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository.
