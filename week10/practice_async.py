from collections import deque
import time
import asyncio

async def runner_1():
    track = deque()
    for i in range(19):
        track.append("_")
    track.append("T")

    items = list(range(0, 10))
    for i, item in enumerate(items):
        print(f" {track}",end="\r")
        time.sleep(.3)
        temp = track.popleft()
        track.append(temp)
    
    await asyncio.sleep(1)

    items2 = list(range(0, 11))
    for i, item in enumerate(items2):
        print(f" {track}",end="\r")
        time.sleep(.3)
        temp1 = track.pop()
        track.appendleft(temp1)

async def runner_2():
    track1 = deque()
    for i in range(9):
        track1.append("_")
    track1.append("t")
    for i in range(10):
        track1.append("_")

    items1 = list(range(0, 9))
    for i, item in enumerate(items1):
        print(f" {track1}",end="\r")
        time.sleep(.3)
        temp1 = track1.popleft()
        track1.append(temp1)
    
    items2 = list(range(0, 10))
    for i, item in enumerate(items2):
        print(f" {track1}",end="\r")
        time.sleep(.3)
        temp1 = track1.pop()
        track1.appendleft(temp1)
    await asyncio.sleep(1)

async def main():
    print()
    print("=======================================================================================")
    print("                                     RELAY RACE                                        ")
    print("=======================================================================================")
    print()
    
    batch = asyncio.gather(runner_1(),runner_2())
    await batch

if __name__ == '__main__':
    asyncio.run(main())
    print()
    print("DONE!")