import json
import requests
import webbrowser

global message_count
global user_id
global user_scratchteam
global user_join
global user_pfp_link
global user_pfp_link_open
global user_aboutme
global user_wiwo
global user_country
global user_followers
global user_following

def message_count(username):
    return (json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/messages/count/", headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3c6 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',}).text)["count"])

def user_id(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data["id"])

def user_scratchteam(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data["scratchteam"])

def user_join(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['history'])

def user_pfp_link(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['profile']['images']['90x90'])

def user_pfp_link_open(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    webbrowser.open_new(data['profile']['images']['90x90'])

def user_aboutme(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['status'])

def user_wiwo(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['bio'])

def user_country(username):
    data = json.loads(requests.get(f"https://api.scratch.mit.edu/users/{username}/").text)
    return (data['country'])

def user_followers(username):
    data = json.loads(requests.get(f"https://scratchdb.lefty.one/v3/user/info/{username}/").text)
    return (data['statistics']['followers'])

def user_following(username):
    data = json.loads(requests.get(f"https://scratchdb.lefty.one/v3/user/info/{username}/").text)
    return (data['statistics']['following'])