

def progress_bars_maker(portion, total, pb_char, pb_len):
    nbar = round(pb_len*portion/total)
    return pb_char*nbar + ' '*(pb_len - nbar)