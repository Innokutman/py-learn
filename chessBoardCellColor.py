# https://app.codesignal.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi
def chessBoardCellColor(cell1, cell2):
    cell1_ord = ord(cell1[0])+int(cell1[1])
    cell2_ord = ord(cell2[0])+int(cell2[1])
    return (cell1_ord + cell2_ord)%2 == 0

    # def chessBoardCellColor(cell1, cell2):
    # return (sum(map(ord,cell1+cell2)))%2 == 0