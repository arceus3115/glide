# glide
Go where you want. Efficiently, without headaches.

Plan 
- set up ruff lint and formatting pre-commits 
- set up uv management 
- tech stack: backend python, fast-api, google maps, reddit, k nearest neighborrs (type vibes). front end typescript, tailwind css.

- Data Structure
    - location: id, name, address, <list [open, close]> time,  type?, anchor?
    - path: id, name, location 1, locations 2, distance, time elapsed, relationship 
    - itinerary: id, name, total elapsed time, <list> locations (or graph unsure what to use here it needs to express weights of path between locations and the locations need to be easily acessible)
- Core Functionality
    - Selection of Origin (City) (probides a origin point for the maps search to make it more efficient)
    - Anchoring & Planning: select x number of anchoring spots to plan ininerary 
        - planning: query maps api to get the spots in a x time radius -> provide to user a list of locations to select from, can choose them as regular or anchor locations -> add to db 
            - anchor locations are not replaceable
            - finding complientatry locations is replacable, eg: running planning a second time after the frist, there will be locations that are regular, if the alogrithm thinks timewise or quality wise there is a better option if will ask the user if they would like to replace a location and why (quality (lower ratings), quantity (already have a lot of a certian genre or catgory), time (closer and similar on the other scores))
    - bonus spots: recommend complimentary spots based off of the anchors (if an anchor is a resturant, it will recommend a drinks places after if its late, if b)
    - time parameters: bound by operating hours, when planning itineraries take into account timming (how long the travel will be +/- 5-10 min situationally)
    - Exporting: 
        - calendar invites
        - trimmed map: greyed out map of just the locations and paths (anchors and regular locations with differentiating logos, time on top of each feature to indicate durration rather than strict start/stop)
