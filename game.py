import Queue


def experiment(game, challenger, adversary):
  queue_c_to_a = Queue.Queue()
  queue_a_to_c = Queue.Queue()
  challenger(game, queue_a_to_c, queue_c_to_a)
  return adversary(game, queue_c_to_a, queue_a_to_c)


def advantage(challenger, adversary):
  num_experiments = 10000
  W_0 = sum([experiment(0, challenger, adversary) for i in range(num_experiments)]) / float(num_experiments)
  W_1 = sum([experiment(1, challenger, adversary) for i in range(num_experiments)]) / float(num_experiments)
  return abs(W_0 - W_1)
