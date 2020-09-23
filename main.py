# coding=utf-8
import time

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ScrapeHTMLPage import scrapHTML
from Search_on_google import get_results
from Search_on_google_WithAPI import google_query
from findUniq import find_uniq
from getMiddle import get_middle
from oppositeNumber import opposite
from square_sum import square_sum


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


def count_sheep(sheep):
    count = 0
    for x in sheep:
        if x:
            count += 1
    return count


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True];
array2 = [1, 2, 2, ];
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(count_sheep(array1))
    print(opposite(-4))
    print(find_uniq(array2))
    print(square_sum(array2))
    #print(get_middle("of"))
    #get_results("dog")
    my_results_list = []
    api_key = "AIzaSyDO3CLtcqRqhAj3zbUGhhjhGd1DCIO3uo4"
    cse_id = "1295ae6f880b36834"
    my_results = google_query("rafael nadal stats",
                              api_key,
                              cse_id,
                              num=10
                              )
    for result in my_results:
        my_results_list.append(result['link'])
        print(result['link'])
    scrapHTML('https://www.ultimatetennisstatistics.com/playerProfile?playerId=4742')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
