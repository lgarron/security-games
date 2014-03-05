import random

import game


def challenger(game, input, output):
  if game == 0:
    output.put(random.choice(["HEADS", "TAILS"]))
  if game == 1:
    output.put("TAILS")


def A1(challenger, input, output):
    return 1


def A2(challenger, input, output):
    return random.choice([0, 1])


def A3(challenger, input, output):
  m = input.get()
  if m == "HEADS":
    return 0
  if m == "TAILS":
    return 1


def A4(challenger, input, output):
  m = input.get()
  if m == "HEADS":
    return 1
  if m == "TAILS":
    return 0


def A5(challenger, input, output):
  m = input.get()
  if m == "HEADS":
    return 0
  if m == "TAILS":
    return random.choice([0, 1])

print game.advantage(challenger, A1)
print game.advantage(challenger, A2)
print game.advantage(challenger, A3)
print game.advantage(challenger, A4)
print game.advantage(challenger, A5)
