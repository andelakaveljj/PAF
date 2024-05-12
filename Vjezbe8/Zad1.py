import matplotlib.pyplot as plt
import numpy as np
import modul as m

cestica1 = m.Cestica(0.3, 1, (0, 0, 0), (0.1, 0.1, 0.1), (0, 0, 0), (0, 0, 1), 0.01)
cestica2 = m.Cestica(0.3, -1, (0, 0, 0), (0.1, 0.1, 0.1), (0, 0, 0), (0, 0, 1), 0.01)
pozitron = cestica1.gibanje(5)
elektron = cestica2.gibanje(5)

graf = plt.axes(projection = "3d")
graf.plot(pozitron[:, 0], pozitron[:, 1], pozitron[:, 2], label = "pozitron")
graf.plot(elektron[:, 0], elektron[:, 1], elektron[:, 2], label = "elektron")
graf.legend()
plt.show()