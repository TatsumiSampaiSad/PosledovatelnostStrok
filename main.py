def easy_otkrytia(gg: list) -> list:
    
    l = [0, 2, -2]
    
    ss = [gg[i] for i in l]
    
    return ss


if __name__ == '__main__':

    assert easy_otkrytia([1, 2, 3, 4, 5, 6, 7, 9]) == [1, 3, 7]
    assert easy_otkrytia([1, 1, 1, 1]) == [1, 1, 1]
    assert easy_otkrytia([6, 3, 7]) == [6, 7, 3]
    print('Done! Go Check!')
