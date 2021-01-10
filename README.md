#### Collaborators: Logan Jones, Bhagirath Bhatt, Karlo Mangubat,  Sean Hawkins
# Road Map:
## 1st Milestone
### Features
- Define a GameLogic class.
- Handle calculating score for dice roll
  1. Add calculate_score static method to GameLogic class.
  2. The input to calculate_score is a tuple of integers that represent adice roll.
  3. The output from calculate_score is an integer representing the roll’s score according to rules of game.
- Handle rolling dice
  1. Add roll_dice static method to GameLogic class.
  2. The input to roll_dice is an integer between 1 and 6.
  3. The output of roll_dice is a tuple with random values between 1 and 6.
  4. The length of tuple must match the argument given to roll_dice method.
- Handle banking points
  1. Define a Banker class
  2. Add a shelf instance method 
     - Input to shelf is the amount of points (integer) to add to shelf.
     - shelf should temporarily store unbanked points.
  3. Add a bank instance method
     - bank should add any points on the shelf to total and reset shelf to 0.
     - bank output should be the amount of points added to total from shelf.
  4. Add a clear_shelf instance method
     - clear_shelfshould remove all unbanked points.

Latest PR: https://github.com/okayjones/game-of-greed/pull/5

# 2nd Milestone
## Features
- Application should implement all features from previous version
- Application should simulate rolling between 1 and 6 dice
- Application should allow user to set aside dice each roll
- Application should allow “banking” current score or rolling again.
- Application should keep track of total score
- Application should keep track of current round
- Application should have automated tests to ensure proper operation

Latest PR:

# 3rd Milestone
## Features
- Application should implement features from versions 1 and 2
- Should handle when cheating occurs.
  - Or just typos.
  - E.g. roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1
- Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- Handle zilch
  - No points for round, and round is over ensure proper operation
Latest PR