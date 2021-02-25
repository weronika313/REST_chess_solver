import models


class FiguresSwitcher(object):
    def indirect(self, figure_name: str, current_field: str):
        method_name = "get_" + figure_name  # type: str
        method = getattr(self, method_name, lambda: "Invalid")
        return method(current_field)

    def get_rook(self, current_field: str) -> models.Rook:
        return models.Rook(current_field)

    def get_queen(self, current_field: str) -> models.Queen:
        return models.Queen(current_field)

    def get_bishop(self, current_field: str) -> models.Bishop:
        return models.Bishop(current_field)

    def get_king(self, current_field: str) -> models.King:
        return models.King(current_field)

    def get_pawn(self, current_field: str) -> models.Pawn:
        return models.Pawn(current_field)

    def get_knight(self, current_field: str) -> models.Knight:
        return models.Knight(current_field)
