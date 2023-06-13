# алгоритм подсчета символов в строке
 
def strcounter(s: str):
    symbols_dict = {}
    for symbol in s:
        if symbol in symbols_dict:
            symbols_dict[symbol] += 1
        else:
            symbols_dict[symbol] = 1
    print(symbols_dict)

    # O(N)
strcounter("ооооооооооооббббббббббббббааааааааааааааа")
