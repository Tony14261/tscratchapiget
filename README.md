# tscratchapiget | THIS IS NOT PUBLISH ON PyPI
A library can get scratch's api
This project gets the scratch api. Everything in this project code by me (except some needed library). Big credit to TimMcCool(Scratcher) for example codes.

#**This can do**
    **User features(v0.2.5)**:
        /n- Get a user unread-message-count ```message_count('[user]')```     EX: ```user.message_count('TimMcCool')```
        - Get a user id ```user_id('[user]')```     EX: ```user.user_id('griffpatch')```
        - Get if a user is a scratchteam ```user_scratchteam('[user]')```     EX: ```user.user_scratchteam('ScratchCat')``` #Return 'True'
        - Get user join date ```user_join('[user]')```     EX: ```user.user_join('Will_Wam')```#Return '2013-11-25T19:52:29.000Z'
        - Get a user pfp(link) ```user_pfp_link('[user]')```     EX: ```user.user_pfp_link('Scratch_Tony_14261')```          +Bonus Feature: Open that pfp link in browser. Change that to ```user_pfp_link_open('[Username]')```
        - Get user About-Me section ```user_aboutme('[user]')``` EX: ```user.user_aboutme('WazzoTV')```
        - Get user What-I'm-Working-On section ```user_wiwo('[username]')```     EX: ```user.user_wiwo('ceebee')```
        - Get user country ```user_country(['user]')```     EX: ```user.user_country(['')```
        - Get user follower count ```user_followers('[user]')```     Ex: ```user.user_followers('sharkyshar')```
        - Get user following count ```user_following('[user]')```     EX: ```user.user_followers('atomicmagicnumber')```
