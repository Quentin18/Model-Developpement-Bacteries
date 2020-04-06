"""
Gestion des axes
"""


class Axis:
    """Représente un axe"""
    def __init__(self, start, end, size_subdiv, label=""):
        self._start = start
        self._end = end
        self._size_subdiv = size_subdiv
        self._label = label

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    @property
    def size_subdiv(self):
        return self._size_subdiv

    @size_subdiv.setter
    def size_subdiv(self, value):
        self._size_subdiv = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
