entrees_visibles = [(8,[1, 12, 4, 8, 17]),
                    (-3,[1, 12, 4, 8, 17]),                 
                    (1,[1, 12, 4, 8, 17]),
                    (8,[]), 
]
entrees_invisibles = [
                    (8,[8, 12, 4, 8, 17]),
                    (17,[1, 12, 4, 8, 17]),                 
                    (-9999999999,[-9999999999]),
]

@solution
def appartient (nombre, liste) :
  return nombre in liste
