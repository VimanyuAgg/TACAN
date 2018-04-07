class States:
  Free, Busy, Active, Sleep = range(4)

# Can be one of {free, busy} if i is
# a clusterhead, or one of {active, sleep} if i is not a
# clusterhead
