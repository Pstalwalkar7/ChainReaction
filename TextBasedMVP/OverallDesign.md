## Flow of Program

1. Main Menu
    a. Welcome player to game
    b. Input the size of the grid (small, med, large)
    c. Input the number of players
    d. Which player is which color (Options should be mutually exclusive)
    e. Other selections (say: Background Music)
    f. Instantiate the Game with given specifications

2. Game Play
    a. Display Board at all times.
    b. Go turn by turn, prompting player's move.
    b. Detect if a player is no longer eligible to move (not their first move and their_count = 0)
    c. Detect the winner if any.
    d. Once played, run the chain reaction (increment neighbours and so on) - BFS.
        i. Challenge: Animations and vibration, to be dealt with later, once we see the core algo is working
    e. If the game has ended, ask if want to play again in same specs, else redirect to main menu (1)  

