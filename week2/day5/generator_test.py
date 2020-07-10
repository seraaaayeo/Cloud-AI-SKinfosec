from __future__ import division
import os
import random
import time
import psutil

names = ['여다솔', '이준혁', '정소영', '이소연', '성지현']
major = ['정통', '전자', '디컨', '컴공', '소웨']

process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss / 1024 / 1024

def people_list(num_people):
    res = []
    for i in range(num_people):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(major)
        }
        res.append(person)
    return res

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(major)
        }
        yield person

def main():
    t1 = time.process_time()
    #people_list(1000000)
    people_generator(1000000)
    t2 = time.process_time()
    mem_after = process.memory_info().rss / 1024 / 1024
    total_time = t2 - t1

    print(f"시작 전 메모리 사용량: {mem_before}MB")
    print(f"종료 후 메모리 사용량: {mem_after}MB")
    print("총 소요된 시간: {:.6f} 초".format(total_time))

if __name__ =="__main__":
    main()