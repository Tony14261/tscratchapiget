This project gets the scratch api. Everything in this project code by me (except some needed library). Big credit to TimMcCool(Scratcher) for example codes. (This project is not related to TimMcCool)<br>
The basics are done. I think i have to use https://scratchdb.lefty.one/v3/ (ScratchDB by Lefty One).<br>
Install: `pip install tscratchapiget`<br>
Change log: https://github.com/Tony14261/tscratchapiget/blob/main/changelog.md<br>
Report bugs or request new features here: https://github.com/Tony14261/tscratchapiget/issues<br>
Contact me (Discord): Tony14261#2089<br>
<br>
Note: I fixed many bugs in this version. There are some new beta features. If anything goes wrong, contact me or report bugs on github page.<br>
Remember to import everything in tscratchapiget: ```from tscratchapiget import user, project, studio```<br>

**User features(v0.2.7 to v0.3.0)** (New commands are at the top):<br>
    - Get if a username exists  ```exists([username])```     EX: ```user.exists('Scratch_Tony_14261')``` if yes: Return 'User exists'     if not: Return 'User does not exist'<br>
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
    <br>
**Project features(v0.3.6)**<br>
    Fill in the [Project ID] with the ID of a project<br>
    - Get a project title ```title('[Project_ID]')```     EX: ```project.title('105500895')```<br>
    - Get a project description ```description('[Project_ID]')```     EX: ```project.description('105500895')```<br>
    - Get a project views ```views('[Project_ID]')```     EX: ```project.views('105500895')```<br>
    - Get a project loves ```loves('[Project_ID]')```     EX: ```project.loves('105500895')```<br>
    - Get a project favorites ```favorites('[Project_ID]')```    EX: ```project.favorites('105500895')```<br>
    - Get a project remixes ```remixes('[Project_ID]')```     EX:   ```project.remixes('105500895')```<br>
    - Get if a project exists ```exists('[Project_ID]')```     EX: ```project.exists('105500895')``` This check returns to your terminal<br>
    - Open a project in a web browser ```open('[Project_ID]')```     EX: ```project.open('105500895')```<br>
    <br>
**Studio features(v0.4.1 to v0.4.5)**<br>
    Fill in the [Studio ID] with the ID of a studio<br>
    - Get a studio title ```studio.title("[Studio ID]")```<br>
    - Get a studio description ```studio.description("[Studio ID]")```<br>
    - Get if comments are allowed in the studio ```studio.comments_allowed([Studio ID])```<br>
    - Get studio create date ```studio.created([Studio ID])```<br>
    - Get studio number of followers ```studio.followers([Studio ID])```<br>
    - Get studio number of projects ```studio.projects([Studio ID])```<br>
More comming soon!
