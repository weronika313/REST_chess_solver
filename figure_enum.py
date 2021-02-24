from enum import Enum


class FigureEnum(Enum):
    QUEEN = "queen"
    KING = "king"
    BISHOP = "bishop"
    KNIGHT = "knight"
    ROOK = "rook"
    PAWN = "pawn"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
