#!/usr/bin/env python3
"""
task 1. Let's execute multiple coroutines at the same time with async.
Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""
import random
import asyncio
import time
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    function that executes multiple coroutines at the same time with async
    and return a list of the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
