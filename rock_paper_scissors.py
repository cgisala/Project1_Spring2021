"""
The data class will store the choices of each game and will store the data
"""

from dataclasses import dataclass

@dataclass
class RockPaperScissor:
    player: str
    computer: str
    winner: str

