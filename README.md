This project gets the scratch api. Everything in this project code by me (except some needed library). Big credit to TimMcCool(Scratcher) for example codes. (This project is not related to TimMcCool)<br>
Install: `pip install tscratchapiget`
Change log: https://github.com/Tony14261/tscratchapiget/blob/main/change.log

**This can do**<br>
    **User features(v0.2.7)(Updated commands in v0.3.0)** (New commands are at the top):<br>
        Note: Remeber to ```from tscratchapiget import user```
        - Get if a username exists  ```exists([username])```     EX: ```user.exists('Scratch_Tony_14261')``` if yes: Return 'User exists'     if not: Return 'User does not exist'
        - Get a user unread-message-count ```message_count('[user]')```     EX: ```user.message_count('TimMcCool')```<br>
        - Get a user id ```id('[user]')```     EX: ```user.id('griffpatch')```<br>
        - Get if a user is a scratchteam ```scratchteam('[user]')```     EX: ```user.scratchteam('ScratchCat')``` #Return 'True'<br>
        - Get user join date ```join('[user]')```     EX: ```user.join('Will_Wam')```#Return '2013-11-25T19:52:29.000Z'<br>
        - Get a user pfp(link) ```pfp_link('[user]')```     EX: ```user.pfp_link('Scratch_Tony_14261')```          +Bonus Feature: Open that pfp link in browser. Change that to ```pfp_link_open('[Username]')```<br>
        - Get user About-Me section ```aboutme('[user]')``` EX: ```user.aboutme('WazzoTV')```<br>
        - Get user What-I'm-Working-On section ```wiwo('[username]')```     EX: ```user.wiwo('ceebee')```<br>
        - Get user country ```country(['user]')```     EX: ```user.country(['')```<br>
        - Get user follower count ```followers('[user]')```     Ex: ```user.followers('sharkyshar')```<br>
        - Get user following count ```following('[user]')```     EX: ```user.followers('atomicmagicnumber')```<br>
