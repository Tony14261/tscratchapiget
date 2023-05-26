import json
import requests
import webbrowser

global message_count
global id
global scratchteam
global join
global pfp_link
global pfp_link_open
global aboutme
global wiwo
global country
global followers
global following

def message_count(username):
    return (json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/messages/count/", headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3c6 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',}).text)["count"])

def id(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data["id"])

def scratchteam(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data["scratchteam"])

def join(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['history'])

def pfp_link(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['profile']['images']['90x90'])

def pfp_link_open(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    webbrowser.open_new(data['profile']['images']['90x90'])

def aboutme(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['status'])

def wiwo(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['bio'])

def country(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['country'])

def followers(username):
    data = json.loads(requests.get(f"https://scratchdb.lefty.one/v3/user/info/{username}/").text)
    return (data['statistics']['followers'])

def following(username):
    data = json.loads(requests.get(f"https://scratchdb.lefty.one/v3/user/info/{username}/").text)
    return (data['statistics']['following'])