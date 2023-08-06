def switch_gravity(l):
    return [list(k) for k in zip(*['-'*(j[1]-j[0])+'#'*j[0] for j in [[list(i).count('#'),len(i)] for i in zip(*l)]])]

print(switch_gravity([
  ["-", "#", "#", "-"],
  ["-", "-", "#", "-"],
  ["-", "-", "-", "-"],
]))