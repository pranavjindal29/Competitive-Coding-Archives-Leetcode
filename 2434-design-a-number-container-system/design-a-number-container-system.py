from collections import defaultdict
from sortedcontainers import SortedSet

class NumberContainers(object):

    def __init__(self):
        self.map={}
        self.valIdx=defaultdict(SortedSet)

    def change(self, index, number):
        if index in self.map:
            if self.map[index]==number: 
                return 
            preVal=self.map[index]
            self.valIdx.get(preVal).remove(index)
        
        self.valIdx[number].add(index)
        self.map[index]=number


    def find(self, number):
        if number not in self.valIdx or not self.valIdx[number]:
            return -1
        return self.valIdx[number][0]
