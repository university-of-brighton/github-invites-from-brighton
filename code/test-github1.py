'''
Github testing api
2 factor authentication etc.

20191107 jason initial basic https://pygithub.readthedocs.io/en/latest/introduction.html
https://pygithub.readthedocs.io/en/latest/
https://pygithub.readthedocs.io/en/latest/github_objects/Invitation.html

'''

from github import Github
# using username and password
#g = Github("user", "password")

# 2FA so... using an access token
# needs: "org" scope.
# generate here: https://github.com/settings/tokens/new

access_token ="<removed>"
g = Github(access_token)

organisationName ='university-of-brighton'
orgObj = g.get_organization(organisationName)

# invite by email:
# https://github.com/PyGithub/PyGithub/issues/851
# invite_user(user=NotSet, email=NotSet, role=NotSet, teams=NotSet)
invite = orgObj.invite_user( email="someone@uni.brighton.ac.uk" )

# The end.

# tests....
#for repo in g.get_user().get_repos():
#    print(repo.name)
#    repo.edit(has_wiki=False)
#    # to see all the available attributes and methods
#    #print(dir(repo))
# https://pygithub.readthedocs.io/en/latest/github_objects/Organization.html
#for member in orgObj.get_members():
#	print member