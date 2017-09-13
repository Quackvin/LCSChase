# LCSChase
Implementing a basic Learning Classifier System to make an enemy follow a player, visualising in pygame

## TODO
1. implement matchset and action set
2. implement subsumption
3. refine GA
4. refine deletion mechanism

## Status
Game runs, player can move.
AI resets to centre when travelling off screen.
Current behaviour:  If initial rules generated do nothing, nothing ever happens
                    If initial rules make a move, moving rules multiply out of control and because theres no action set or 
                    match set implemented it quickly accelerates and races around like crazy, fill the ruleset with
                    duplicates.
