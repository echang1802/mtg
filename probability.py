
class distribution:

    def __init__(self):
        self._events = []
        self._counts = []
        self._probs = []
        self._points = 0

    def add_data(self, point):
        if point in self._events:
            pos = [x for x in range(len(self._events)) if self._events[x] == point][0]
            self._counts[pos] += 1
        else:
            self._events.append(point)
            self._counts.append(1)
        self._points += 1

    def _order_data(self):
        pos = sorted(range(len(self._events)), key = lambda x: self._events[x])
        self._events = [self._events[x] for x in pos]
        self._counts = [self._counts[x] for x in pos]

    def _update_probs(self):
        self._probs = [x / self._points for x in self._counts]

    def show(self):
        self._order_data()
        self._update_probs()
        for pos in range(len(self._events)):
            print(self._events[pos],":")
            print("\tCount:",self._counts[pos])
            print("\tProb:",self._probs[pos])
