import math
from pydoc import getpager


def solution(x, y):
    answer = 0

    return answer


def get_parent(parent, x):
    if parent[x] == x:
        return x

    parent[x] = get_parent(parent, parent[x])

def union_parent(parent,a,b):
  a = get_parent(parent,a)
  b = get_parent(parent,b)
  if a < b:
    parent[b] = a
  else :
    parent[a] = b