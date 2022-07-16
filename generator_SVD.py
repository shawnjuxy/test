#_*_ coding:utf-8 _*_

import pandas as pd
import numpy as np
import scipy.sparse.linalg

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

class SVDGenerator(object):

    def __init__(self):

        self.A = np.array([[1, 0, 0], [0, 0, 5], [0, 3, 6]])

    def run(self):

        # 求解矩阵 S
        V1, S = np.linalg.eigh(self.A.dot(self.A.T))
        print("矩阵 S")
        print(S)

        # 求解矩阵 D
        V2, D = np.linalg.eigh(self.A.T.dot(self.A))
        print("矩阵 D")
        print(D)

        # 求奇异值 V
        V1 = np.sqrt(V1)
        print("奇异值 V")
        print(V1)


if __name__ == '__main__':


    svd = SVDGenerator()

    svd.run()



   











