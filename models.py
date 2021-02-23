from typing import List


class Figure(object):
    def __init__(self, current_field: str) -> None:
        self.currentField = current_field

    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass


class King(Figure):
    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass


class Queen(Figure):
    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass


class Rook(Figure):
    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass


class Bishop(Figure):
    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass


class Knight(Figure):
    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass


class Pawn(Figure):
    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass

