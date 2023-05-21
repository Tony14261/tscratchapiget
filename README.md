# tscratchapiget | THIS IS PUBLISH ON PyPI 
https://pypi.org/project/tscratchapiget/ <br>
A library can get scratch's api<br>
This project gets the scratch api. Everything in this project code by me (except some needed library). Big credit to TimMcCool(Scratcher) for example codes. <br>
Install: `pip install tscratchapiget`

#**This can do**<br>
    **User features(v0.2.5 to v0.2.7)**:<br>
        - Get a user unread-message-count ```message_count('[user]')```     EX: ```user.message_count('TimMcCool')```<br>
        - Get a user id ```user_id('[user]')```     EX: ```user.user_id('griffpatch')```<br>
        - Get if a user is a scratchteam ```user_scratchteam('[user]')```     EX: ```user.user_scratchteam('ScratchCat')``` #Return 'True'<br>
        - Get user join date ```user_join('[user]')```     EX: ```user.user_join('Will_Wam')```#Return '2013-11-25T19:52:29.000Z'<br>
        - Get a user pfp(link) ```user_pfp_link('[user]')```     EX: ```user.user_pfp_link('Scratch_Tony_14261')```          +Bonus Feature: Open that pfp link in browser. Change that to ```user_pfp_link_open('[Username]')```<br>
        - Get user About-Me section ```user_aboutme('[user]')``` EX: ```user.user_aboutme('WazzoTV')```<br>
        - Get user What-I'm-Working-On section ```user_wiwo('[username]')```     EX: ```user.user_wiwo('ceebee')```<br>
        - Get user country ```user_country(['user]')```     EX: ```user.user_country(['')```<br>
        - Get user follower count ```user_followers('[user]')```     Ex: ```user.user_followers('sharkyshar')```<br>
        - Get user following count ```user_following('[user]')```     EX: ```user.user_followers('atomicmagicnumber')```<br>
