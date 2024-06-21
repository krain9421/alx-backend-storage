#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)
cache.replay(cache.store)
