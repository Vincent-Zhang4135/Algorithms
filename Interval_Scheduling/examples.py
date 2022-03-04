################################
#
# How should we go about storing our jobs? I suggest that it is important for us
# to also have a way to "id" the jobs. For instance, there could also be two jobs that
# have the same start and end time. having an id would allow us to better see what our
# solution actually looks like
# 
# Thus: J will be a list of lists, each list have three entries:
# index 0: ID
# index 1: start_time
# index 2: end_time
################################


J1 = [[0, 8, 12], 
      [1, 11, 13],
      [2, 9, 11],
      [3, 16, 19],
      [4, 14, 19],
      [5, 14, 19]]

J2 = [[0, 1, 5],
      [1, 3, 4],
      [2, 10, 12],
      [3, 2, 7],
      [4, 4, 5],
      [5, 5, 6],
      [6, 9, 13],
      [7, 5, 10],
      [8, 7, 9],
      [9, 6, 7],
      [10, 12, 13]]