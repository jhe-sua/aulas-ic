import numpy as np
import pandas as pd

#np.loadtxt("/home/fgv/code/env_prog/arc/dados.csv",delimiter=",",skiprows=4,dtype=str)
# pandas por defeito pula as linas em branco

data = pd.read_csv("/home/fgv/code/env_prog/arc/dados.csv",header=2, sep=",")
data[:10].to_csv("/home/fgv/code/env_prog/arc/aula06.csv", index=False)
print(data[:10])

#instalamos a extensão de jupyter do vscode, instalamos jupyter, pandas, pyarrow, com uv