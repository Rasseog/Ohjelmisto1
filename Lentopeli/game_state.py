# game_state.py
from dataclasses import dataclass

@dataclass
class GameState:
    current_icao: str
    goal_icao: str

    money: int
    fuel: int
    moves: int
    points: int

    last_event: str = ""
    last_hint: str = ""
    game_over: bool = False
    win: bool = False