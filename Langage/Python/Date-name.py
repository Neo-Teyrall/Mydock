import datetime
import time


def get_date_name():
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#    stre = now.strftime("%Y-%m-%d-%H-%M-%S")
    print(now)

    pass


if __name__ == "__main__":
    get_date_name()
    time.sleep(2)
    get_date_name()
