import random


def med():
  mediasAlunos = []
  mediaTurma = 0

  for i in range(5):
    notaTotal = 0
    for j in range(4):
      notaTotal += random.randint(0, 10)
    mediasAlunos.append(notaTotal / 4)

  for g in range(len(mediasAlunos)):
    mediaTurma += mediasAlunos[g]
  print(mediaTurma)
  mediaTurma = mediaTurma / len(mediasAlunos)

  print(f"As médias dos alunos sao: {mediasAlunos}")
  print(f"A média da turma e: {mediaTurma}")