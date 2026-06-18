# Gameplay instructions
Forage potato and daikon seeds in the wilds down to the right. Return to your camp, visit your crops in the top left of your camp, plant your seeds. After some time, they'll have grown, and can be harvested. Go to sleep before it becomes dark and the storm gets you. You can then sell them to the trader who will give you money or rare blueberry seeds in return.

# Gruppemedlemmer
- Skage Lydersen
- Bunyamin Løwer Keser
- Filippa Korodi

# Requirements:
- python 3.14
- pygame-ce
A flake is included, see "# How to develop".

# How to run:
- clone this project or download zip
- `cd` to the root of the copy you downloaded/cloned
- run `python -m src.main`

# How to develop
A nix flake is included, if you have the nix package manager installed (available for linux & macos), you can run `nix develop` to enter a reproducable shell from which you can run the code, and e.g. launch editors from command line.

# Internal notes
Loading happens as follows:
- world object init function runs
  - init function for each scene object runs
- initial transition to loadingscreen
- when loadingscreen is done, transition to main menu

From then on:
- `onFrame` is called for the current scene every frame
- `alwaysTick` is called for every scene every frame

And when a `ctx.transition_scene_to` call happens:
  - fademanager+worldobject performs fade to black
  - fademanager+worldobject call `ctx._actually_transition_scene`
  - `onExit` called for last scene
  - `onEnter` called for new scene
  - `current_scene` variable changed
  - fademanager+worldobvject perform fade in from black
