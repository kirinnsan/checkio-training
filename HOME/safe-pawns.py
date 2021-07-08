def safe_pawns(pawns: set) -> int:
    safe_pawnn_counter = 0
    for paw in pawns:
        file, lank = paw[0], paw[1]
        # ord():1文字の Unicode 文字を表す文字列に対し、
        # その文字のUnicode コードポイントを表す整数を返します。chrの逆
        # chr():Unicode コードポイントが整数 i である文字を表す文字列を返します。ordの逆
        expect_pawn_left = chr(ord(file)-1) + str(int(lank)-1)
        expect_pawn_right = chr(ord(file)+1) + str(int(lank)-1)
        if expect_pawn_left in pawns or expect_pawn_right in pawns:
            safe_pawnn_counter += 1

    return safe_pawnn_counter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
