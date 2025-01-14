# Boggle Game (Online)
A web-based implementation of the classic Boggle word game using Flask, featuring a 5x5 grid of randomly generated letters.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Technical Documentation](#technical-documentation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Overview

This application implements a digital version of Boggle, presenting players with a 5x5 grid of letters. The letters are generated using authentic Boggle dice configurations, ensuring game authenticity. Players can shuffle the board to start a new game configuration.

## Installation
1. Clone the repository
2. Install the required dependencies:
```bash
pip install flask numpy
```
3. Run the application:
```bash
python main.py
```
4. Access the game at `http://localhost:5000`

## Project Structure
```
boggle/
├── main.py           # Flask application entry point
├── model.py          # Game logic and dice configuration
├── templates/
│   ├── index.html    # Game board template
│   └── template.html # Base template
└── static/
    └── styles.css    # Game styling
```

## Technical Documentation

### Backend Components

#### main.py
The Flask application entry point that handles routing and game initialization.

```python
@app.route("/")
def home():
    # Generates and shuffles letters for the 5x5 grid
    # Returns rendered template with 25 letter positions
```

**Key Features:**
- Initializes Flask application
- Handles route for main game page
- Manages letter distribution to the game board
- Contains commented timer functionality (currently disabled)

#### model.py
Contains the core game logic and dice configurations.

**Functions:**
- `getRandomLetters()`: 
  - Generates a list of 25 random letters based on authentic Boggle dice configurations
  - Returns a list of randomly selected letters from each die
  
- `shuffleDice(letters: list)`: 
  - Takes a list of letters and randomly shuffles their positions
  - Returns the shuffled list

The `dice` list contains 25 authentic Boggle dice configurations, each with 6 possible letters.

### Frontend Components

#### templates/index.html
The game board template, featuring:
- 5x5 grid layout using HTML table
- Letter placement using Flask template variables
- Shuffle button for new game configurations
- Commented-out timer functionality

#### templates/template.html
Base template providing:
- HTML structure
- CSS styling links
- Responsive viewport configuration
- Central alignment for game elements

#### static/styles.css
Styling definitions including:
- Custom font family
- Table and cell styling for the game board
- Responsive layout adjustments
- Board cell dimensions and borders

## Usage
1. Access the game through your web browser
2. View the 5x5 grid of randomly generated letters
3. Click "Shuffle Letters" to generate a new board configuration
4. Use pen and paper to record found words
5. Traditional Boggle rules apply:
   - Words must be formed from adjacent letters
   - Letters must be connected horizontally, vertically, or diagonally
   - Each letter cube can only be used once per word
   - Words must be at least 3 letters long

## Dependencies
- Python 3.x
- Flask
- NumPy
- Modern web browser with JavaScript enabled

<!-- ## Development Notes
Timer functionality is currently commented out but implemented in both frontend and backend. To enable the timer:
1. Uncomment the timer-related code in `main.py`
2. Uncomment the JavaScript timer code in `index.html`
3. Add appropriate styling for timer display in `styles.css` -->

## Future Enhancements
1. Enable timer functionality
2. Add word validation
3. Implement score tracking
4. Add multiplayer support
5. Include dictionary verification