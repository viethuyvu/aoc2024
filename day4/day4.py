with open ("input.txt","r") as file:
    lines = [line.strip() for line in file.readlines()]

linelength = len(lines[0])


def d4p1():
    # join() is used to concatenate the list of characters obtained from the previous part into a single string.
    columns = [''.join([line[i] for line in lines]) for i in range(linelength)] 

    diag_tr = []
    diag_tl = []
    diag_br = []
    diag_bl = []

    for i in range(linelength):
        diag = []
        x,y = 0,i
        while x < linelength and y < linelength:
            diag.append(lines[x][y])
            x += 1
            y += 1
        diag_tr.append(''.join(diag))

    for i in range(linelength):
        diag = []
        x,y = 0,i
        while x < linelength and y >= 0:
            diag.append(lines[x][y])
            x += 1
            y -= 1
        diag_tl.append(''.join(diag))

    for i in range(linelength):
        diag = []
        x,y = linelength-1,i
        while x >= 0 and y < linelength:
            diag.append(lines[x][y])
            x -= 1
            y += 1
        diag_br.append(''.join(diag))

    for i in range(linelength):
        diag = []
        x,y = linelength-1,i
        while x >= 0 and y >= 0:
            diag.append(lines[x][y])
            x -= 1
            y -= 1
        diag_bl.append(''.join(diag))
        big_diag_tl = ""
        big_diag_tr = ""

    for i in range(linelength):
        big_diag_tl += (lines[i][i])

    for i in range(linelength):
        big_diag_tr += (lines[i][linelength-1-i])

    total_sum = 0 
    for line in lines:
        total_sum += line.count("XMAS")
        total_sum += line.count("SAMX")

    for column in columns:
        total_sum += column.count("XMAS")
        total_sum += column.count("SAMX")

    for diag in diag_tr:
        total_sum += diag.count("XMAS")
        total_sum += diag.count("SAMX")

    for diag in diag_tl:
        total_sum += diag.count("XMAS")
        total_sum += diag.count("SAMX")

    for diag in diag_br:
        total_sum += diag.count("XMAS")
        total_sum += diag.count("SAMX")
    
    for diag in diag_bl:
        total_sum += diag.count("XMAS")
        total_sum += diag.count("SAMX")

    total_sum -= big_diag_tl.count("XMAS")
    total_sum -= big_diag_tl.count("SAMX")
    total_sum -= big_diag_tr.count("XMAS")
    total_sum -= big_diag_tr.count("SAMX")

    return total_sum

def d4p2():
    total_sum = 0
    for i in range (1,linelength-1):
        for j in range (1,linelength-1):
            if lines[i][j] == "A":
                cross1 = lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1]
                cross2 = lines[i-1][j+1] + lines[i][j] + lines[i+1][j-1]
                if cross1 == "MAS" or cross1 == "SAM":
                    if cross2 == "MAS" or cross2 == "SAM":
                        total_sum += 1

    return total_sum

if __name__ == "__main__":
    print(d4p1())
    print(d4p2())

