def main():
    import time
    import os

    TWtime = time.strftime("%Y.%m.%d", time.localtime())
    fo = open(f'txt\\{TWtime}.txt', 'r', encoding='utf-8-sig')
    fontsize = 28
    timecolor = '#DAA520'
    testcolor = '#d32c64'
    warningcolor = '#f60600'
    HWcolor = '#2577da'
    Bringcolor = '#059400'
    Handoutcolor = '#c90ef1'
    Dailycolor = '#7c7e83'

    def change_color(linesp, stringplace):
        if linesp[0] == 'a' or linesp[0] == 'A' or linesp[0] == '完成':
            return f'<span style="color:{HWcolor};">' + '完成' + '</span>' + ' ' + "".join(linesp[1:stringplace+1])
        elif linesp[0] == 'b' or linesp[0] == 'B' or linesp[0] == '考試':
            return f'<span style="color:{testcolor};">' + '考試' + '</span>' + ' ' + "".join(linesp[1:stringplace+1])
        elif linesp[0] == 'c' or linesp[0] == 'C' or linesp[0] == '帶':
            return f'<span style="color:{Bringcolor};">' + '帶' + '</span>' + ' ' + "".join(linesp[1:stringplace+1])
        elif linesp[0] == 'd' or linesp[0] == 'D' or linesp[0] == '交':
            return f'<span style="color:{Handoutcolor};">' + '交' + '</span>' + ' ' + "".join(linesp[1:stringplace+1])
        elif linesp[0] == 'e' or linesp[0] == 'E' or linesp[0] == '週記':
            return f'<span style="color:{Dailycolor};">' + '週記: ' + '</span>' + ' ' + "".join(linesp[1:stringplace+1])
        else:
            return linesp[0] + "".join(linesp[1:stringplace+1])

    with open(f'output.txt', 'w', encoding='utf-8') as ot:
        #ot.write('<html><head><meta charset =\"utf-8\"></head><body>')
        ot.write('<ol>\\\n')
        for line in fo:
            ot.write(f'<li><span style="font-size:{fontsize}px;"><strong>')
            linesp = line.split()
            print (linesp[:])
            for i in range(0, len(linesp)):
                try:
                    struct_time = time.strptime(linesp[i], "%m%d%Y")
                    new_timeString = time.strftime("%m/%d(%a)", struct_time)
                    #print (new_timeString)
                    stringplace = i - 1
                except:
                    stringplace = i
                    continue
            ot.write(change_color(linesp, stringplace))
            if stringplace == len(linesp) - 2:
                ot.write(f'<span style="color:{timecolor};">[{new_timeString}]</span>')  
            ot.write('</strong></span></li>')
            ot.write('\\\n')
        if time.strftime("%w", time.localtime()) == 1 or time.strftime("%w", time.localtime()) == 3:
            ot.write(f'<li><span style="font-size:{fontsize}px;"><strong><span style="color:{warningcolor};">穿制服(皮鞋)</span></strong></span></li>\\\n')
        ot.write('</ol>')
       # ot.write('</body></html>')
    fo.close()
main()