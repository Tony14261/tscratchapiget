This project gets the scratch api. Everything in this project code by me (except some needed library). Big credit to TimMcCool(Scratcher) for example codes. <br>
Install: `pip install tscratchapiget`

#**This can do**<br>
    **User features(v0.2.5 to v0.2.7)(Update commands in v0.3.0)**:<br>
        user.<br>
        - Get a user unread-message-count ```message_count('[user]')```     EX: ```user.message_count('TimMcCool')```<br>
        - Get a user id ```user_id('[user]')```     EX: ```user.user_id('griffpatch')```<br>
        - Get if a user is a scratchteam ```scratchteam('[user]')```     EX: ```user.scratchteam('ScratchCat')``` #Return 'True'<br>
        - Get user join date ```join('[user]')```     EX: ```user.join('Will_Wam')```#Return '2013-11-25T19:52:29.000Z'<br>
        - Get a user pfp(link) ```pfp_link('[user]')```     EX: ```user.pfp_link('Scratch_Tony_14261')```          +Bonus Feature: Open that pfp link in browser. Change that to ```pfp_link_open('[Username]')```<br>
        - Get user About-Me section ```aboutme('[user]')``` EX: ```user.aboutme('WazzoTV')```<br>
        - Get user What-I'm-Working-On section ```wiwo('[username]')```     EX: ```user.wiwo('ceebee')```<br>
        - Get user country ```user_country(['user]')```     EX: ```user.user_country(['')```<br>
        - Get user follower count ```user_followers('[user]')```     Ex: ```user.user_followers('sharkyshar')```<br>
        - Get user following count ```user_following('[user]')```     EX: ```user.user_followers('atomicmagicnumber')```<br>
