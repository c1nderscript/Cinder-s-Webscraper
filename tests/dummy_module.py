"""Dummy module for schedule manager tests."""

calls = []


def dummy_task(x=None):
    calls.append(x)
    return x
