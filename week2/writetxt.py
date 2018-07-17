date = input('輸入日期:')
event = input('輸入事件:')
description = input('輸入心得:')

with open("note.txt", "a+") as f:
    f.writelines("日期 : %s\n" %date)
    f.writelines("事件 : %s\n" %event)
    f.writelines("心得 : %s\n\n" %description)
    f.close()