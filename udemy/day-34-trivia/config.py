import os

THEME_COLOR = "#375362"
DISPLAY_COLOR = "#FFFFFF"
RIGHT_COLOR = "#27FF00"
WRONG_COLOR = "#FF7B7B"

TRIVIA_URL = 'https://opentdb.com/api.php'

Q_FONT = ('Arial', 16, 'italic')
S_FONT = ('Arial', 12, 'bold')

CURRENT_DIR = os.path.dirname(__file__)

TRUE_IMG = os.path.join(CURRENT_DIR, './images/true.png')
FALSE_IMG = os.path.join(CURRENT_DIR, './images/false.png')