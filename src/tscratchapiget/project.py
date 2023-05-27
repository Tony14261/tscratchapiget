import json
import requests
from tscratchapiget import user

def stats(project_id,type):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/projects/{project_id}/").text)
    return (data['stats'][type])
    #types = views/loves/favorites/remixes
    
def author(project_id, type):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/projects/{project_id}/").text)
    return (data[author][type])
    #type = id/username/scratchteam