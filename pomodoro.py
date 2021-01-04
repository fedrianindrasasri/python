import time


def countDownTimer(start_minute, start_second):
    total_second = start_minute*60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
    print("Done!")


if __name__ == '__main__':
    countDownTimer(25, 00)
