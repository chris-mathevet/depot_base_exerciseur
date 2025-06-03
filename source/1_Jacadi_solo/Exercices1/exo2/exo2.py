entrees_visibles = [[12,4,5,6,17],
                    [],
                    [-2,24,14,8,19,-7],
]
entrees_invisibles = [
                    [202,24,14,8,19,-7],
                    [-9999999999],
                    [-9999999999, -555555555555],
]

@solution
def maximum(liste) :
  if liste==[]:
    return None
  else:
    return max(liste)
