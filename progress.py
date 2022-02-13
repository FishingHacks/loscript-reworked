import sys
import time


def print_percent_done(index, total, bar_len=50, title='Please wait', donetitle='Done!'):
    '''
    index is expected to be 0 based index. 
    0 <= index < total
    '''
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/bar_len))
    togo = bar_len-done

    done_str = '█'*int(done)
    togo_str = '░'*int(togo)
    titleskip = " "*int(len(title) - len(donetitle))

    print(f'\t⏳ {title} {done_str}{togo_str} {percent_done}% done', end='\r')

    if round(percent_done) == 100:
        print(
            f'\t✅ {donetitle} {titleskip}{done_str}{togo_str} {percent_done}% done')


def createprogress(len, wtime=.08, title='Please wait', donetitle='Done!'):
    r = len
    if (isinstance(wtime, float)):
        wtime = wtime
    else:
        wtime = 0.08
    for i in range(r):
        print_percent_done(i, r, r, title, donetitle)
        time.sleep(float(wtime))
