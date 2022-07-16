import time
import random
from datetime import datetime


class Id(object):
    """
    discord ID generator, that is accurate
    """
    EPOCH = 142007040000
    __worker_increments = {i: 0 for i in range(32)}

    @classmethod
    def new(cls):
        # number of seconds discord was born
        id   = time.time_ns() // 10_000_000
        id  -= cls.EPOCH
        id <<= 5

        # internal worker id simulation
        worker_id = random.randrange(0, 32)  # 5 bits
        id  += worker_id
        id <<= 5

        # internal process id simulation
        id  += random.randrange(0, 32)       # 5 bits
        id <<= 12

        # for every ID that is generated on a process, this number is incremented
        id  += cls.__worker_increments[worker_id] % 4096
        cls.__worker_increments[worker_id] += 1

        return id

    @classmethod
    def created_at(cls, id: int) -> datetime:
        ts = ((id >> 22) + cls.EPOCH) // 100
        return datetime.fromtimestamp(ts)
