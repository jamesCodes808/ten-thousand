# LAB - Class 06
## Project: Ten Thousand
## Author: Diontre Sanders, James Ian Solima

### Links and Resources
[ChatGPT](https://chat.openai.com/chat)

### Setup
- pip install -r requirements.txt

### How to initialize/run your application (where applicable)
- source .venv/bin/activate

### How to use your library (where applicable)
NA

### Tests
How do you run tests? 
- pytest

- Any tests of note?
calculate_score: 50 passed, 6 failed
roll_dice: 6 passed

- Describe any tests that you did not complete, skipped, etc:
Skipped the 6 out of 56 tests in calculate_score, because of the realization that there were core tests that allowed most to pass.

### Features

- 3/27: 
  - Created Game Logic and Dice Roll
  
- 3/28: 
  - Application should implement all features from previous version (dice_roll, calculate_score)
  - Application should allow user to set aside dice each roll
  - Application should allow “banking” current score or rolling again.
  - Application should keep track of total score
  - Application should keep track of current round