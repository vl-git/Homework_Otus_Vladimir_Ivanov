class StartError(Exception):
    def __str__(self):
        return 'You need to start engine first'

