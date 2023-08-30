#!/usr/bin/env python3
"""
task 0. Async Generator
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
Use the random module.
"""
import random
import time


async def async_generator():
    """
    Function that loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10.
    """
    for i in range(10):
        number = random.uniform(0, 10)
        time.sleep(1)
        yield (number)
