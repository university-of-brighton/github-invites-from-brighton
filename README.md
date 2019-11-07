# Github org invites   

Python code using pygithub to create invites to brighton org.

## Example of code. 
There's a simple test script so far.  

~~~~
from github import Github

access_token ="xyz1234ffdfkfdkfletcetc"
g = Github(access_token)

organisationName ='university-of-brighton'
orgObj = g.get_organization(organisationName)

invite = orgObj.invite_user( email="someone@uni.brighton.ac.uk" )
~~~~





