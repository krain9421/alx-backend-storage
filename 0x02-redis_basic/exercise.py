#!/usr/bin/env python3
"""Module for writing strings to Redis"""

import redis
import uuid
from typing import TypeVar, Union, Callable
from functools import wraps

T = TypeVar('T', str, bytes, int, float, None)


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times
    a method is called
    """

    @wraps(method)
    def wrapper(self, data: T) -> Callable:
        """
        Wrapper function
        """

        key = method.__qualname__
        # try/catch block
        try:
            self._redis.incr(key)
        except Exception as e:
            pass
        finally:
            # Call the original method
            return method(self, data)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the input
    and output parameters of a function
    """
    @wraps(method)
    def wrapper(self, data: T) -> Callable:
        """
        Inner wrapper function
        """

        key = method.__qualname__
        input_arg = data

        # Append the input arguments to the list
        self._redis.rpush(f"{key}:inputs", input_arg)

        # Execute the wrapped method
        output = method(self, data)

        # Convert output to a normalized string
        output_arg = str(output)

        # Append the output to another list
        self._redis.rpush(f"{key}:outputs", output_arg)

        return output

    return wrapper


class Cache:
    """
    Cache class to store instance of the Redis client
    _redis as a private variable using redis.Redis()
    and flush the instance using flushdb
    """

    def __init__(self):
        """
        __init__ method to initialize a
        Cache object
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method takes a data argument and
        returns a string.
        The method should generate a random key,
        store the input data in Redis using the key
        and return the key.
        """

        # Convert the uuid to string
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None) -> T:
        """
        method that take a key string argument
        and an optional Callable argument named fn
        """

        if fn is None:
            value = self._redis.get(key)
        else:
            value = fn(self._redis.get(key))
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """
        Convenience method that automatically parametrizes
        Cache.get() with the correct conversion
        function fn=str
        """

        return self.get(key, fn=str)

    def get_int(self, key: int) -> Union[int, None]:
        """
        Convenience method that automatically parametrizes
        Cache.get() with the correct conversion
        function fn=int
        """

        return self.get(key, fn=int)

    def replay(self, method: Callable) -> str:
        """
        Replay function that displays the history
        of calls of a particular function
        """

        # Get the Redis object
        r = self._redis

        # Get the qualified name of the method
        qualname = method.__qualname__

        # Get the input and output lists
        inputs = r.lrange(f"{qualname}:inputs", 0, -1)
        outputs = r.lrange(f"{qualname}:outputs", 0, -1)

        # Get the method call count
        count = self.get_int(qualname)

        # Print history of calls
        print("{} was called {} times:".format(qualname, count))
        for i in count:
            pass
