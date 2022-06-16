import collections

from typing import Counter


FILENAME = "dummy-acces.txt"
# def main(filename):
fp = open(FILENAME, encoding="UTF-8")
text_lines = fp.readlines()
fp.close()
    
counter = collections.Counter()

for line in text_lines:
    words = line.split()
    for ip in words:
        filtered_ip = ip.strip(" - - ")
        if filtered_ip:
             counter[filtered_ip] += 1
    # return counter

for cnt, ip in counter.most_common(10):
    print("{}  -- {}".format(ip, cnt))
