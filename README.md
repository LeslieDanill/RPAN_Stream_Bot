# Pranbot

Pranbot is an open source tool to help Reddit streamers moderate their streams.<br /> 
We work on it live on stream while learning the ins and outs of Python.


Join us on the stream! [Twitch](https://www.twitch.tv/moderator/lesliedanill)<br />
Join our discord! ( Not a cult ) [Discord](https://discord.gg/PJftM5kGTQ)<br />



# Functionality
* Custom streamer commands.
* View streamer stats.
* Opt-in users for notifications.

<br />

# Built in commands:
Banning a user:
```shell
!ban <username>
```
Time out a user:
```shell
!timeout <username>
```

# Custom Commands
Streamers will be able to setup their own custom commands by running a built-in command. Only the streamer themselves can add custom commands and all customs are by default open to all viewers.


Adding a command:
```shell
!add !<command>
```
Removing a command:
```shell
!remove !<command>
```



Notes
* All comments can run commands depending on permissions set by the streamer. This is based on the viewer being added as a moderator. 
* Moderation (Subreddit-Level)
  - If a viewer has been banned from >=3 streamers content, then issue a subreddit-level ban (this is only on our subreddit RPRAN)
* Notifications (Opt-In per viewer) 
  - Built-in command where anyone can opt-in to get going-live notifications for the streamer





