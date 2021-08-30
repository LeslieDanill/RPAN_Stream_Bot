# --- PRANbot Functionality Notes --- #

import praw

# Define variables from Sticky Posts
oauth = ""
# GET

# Get our databeauxs (all) from the subreddit wiki and assign to dict
data = {}
#Get all wikipages using API [/r/subreddit]/wiki/pages
# dataraw = None
dataraw = {"kind": "wikipagelisting", "data": ["config/description", "config/sidebar", "index", "pranbot", "pranbot/r", "pranbot/u", "pranbot/u/ladymoirai", "pranbot/u/meltmore"]}
#For toplevelsubpage in pranbot 
for page in dataraw["data"]:
    toplevel = "pranbot/"
    # get list of all next top level of subpages
    if page.startswith(toplevel):
        subpage = page[len(toplevel):]
        if "/" in subpage:
            key = subpage[:subpage.index("/")+1]
            value = subpage[subpage.index("/")+1:]
            # this whole 'if' statement could potentially be handle by DEFAULTDICT (ali)
            if key not in data:
                data[key] = []
            data[key].append(value)
print(data)
            


    


    #append to dict databeauxs key=toplevelsubpage(ex:"/r") value=all subpages (sort in hierarchy somehow)

    # All comments which have triggered the bot (only on a livestream) !discord
    # livestream loid info https://www.reddit.com/r/redditdev/comments/lqcxqu/rpan_stream_api_disallows_connection/
    # Remember - individual commands should have a cooldown time in case called multiple times in a short period
    # Careful of limits (request limit, total wiki pages - maybe no limit...? wiki page size DOES have a limit)

    ##Potential Subpages
    #Streamer Custom Commands
    #Opted-in notification users
    #Streamer stats

#Functionality Notes:
"""
1. Custom Commands
    - There are some built-in commands
    - Streamers can set up their own custom commands by running a built-in command !add !mycommand text for the command (!remove !mycommand) (only streamers themselves can add custom commands and all customs are by default open to all viewers)
    - All comments can run commands (depending on permissions / is the streamer or mod or viewer)
2. Moderation (Streamer-Level)
    - streamer or their mods can use built-in commands to:
        - !ban / !timeout
3. Moderation (Subreddit-Level)
    - If a viewer has been banned from >=3 streamers content, then issue a subreddit-level ban (this is only on our subreddit RPRAN)
4. Notifications (Opt-In per viewer) 
    - built-in command where anyone can opt-in to get going-live notifications for the streamer
"""