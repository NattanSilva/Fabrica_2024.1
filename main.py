from atividades.idade import age
from atividades.maior import maturity
from atividades.media import med
from atividades.par_ou_impar import par_ou_impar
from atividades.primo import prim
from atividades.times import teams

if __name__ == '__main__':
  # 1 - mostrar idade
  print("-----------------------")
  age()
  # 2 - calcular media de 5 alunos
  print("-----------------------")
  med()
  # 3 - mostrar times
  print("-----------------------")
  teams()
  # 4 - calcular maior idade
  print("-----------------------")
  maturity()
  # 5 - par ou impar
  print("-----------------------")
  par_ou_impar()
  # 6 - número primo ou não
  print("-----------------------")
  print(prim())