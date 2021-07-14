from typing import List


def checkio(game_result: List[str]) -> str:
    # 勝利パターン
    # 各リストのインデックスが同じ（縦のパターン）
    # インデックスの値が0,1,2か2,1,0のパターン（斜めのパターン）

    players = ['X', 'O']
    winner = 'D'

    for player in players:
        # 1つの文字列が全て同じ(横のパターン)
        for row in game_result:
            if row.count(player) == 3:
                winner = player
                return winner
        # 各リストのインデックスが同じ（縦のパターン）
        column_index_list = []
        for i, row in enumerate(game_result):
            if player not in row:
                break
            if i == 0:
                column_index_list = [
                    i for i, char in enumerate(row) if char == player]
                continue
            if row.index(player) not in column_index_list:
                break
            if i == 2:
                winner = player
                return winner
        # インデックスの値が0,1,2か2,1,0のパターン（斜めのパターン）
        for i, row in enumerate(game_result):
            if player not in row:
                break
            if row[i] != player:
                break
            if i == 2:
                winner = player
                return winner
        index = 0
        for i, row in zip([2, 1, 0], game_result):
            if player not in row:
                break
            if row[i] != player:
                break
            if index == 2:
                winner = player
                return winner
            index += 1
    return winner


if __name__ == '__main__':
    print("Example:")
    print(checkio([
        "OOX",
        "XXO",
        "OXX"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
