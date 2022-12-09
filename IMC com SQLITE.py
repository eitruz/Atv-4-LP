import sqlite3
import os

connection = sqlite3.connect('imc.db')
cursor = connection.cursor()


def criartabela():
  # Não consegui identificar porque não ta aceitando dados float no codigo abaixo
  # cursor.execute("""CREATE TABLE IF NOT EXISTS dados (nome TEXT NOT NULL, pesopaciente REAL, alturapaciente REAL, resultadoimc REAL)""")
  cursor.execute("""CREATE TABLE IF NOT EXISTS dados (nome TEXT NOT NULL, resultadoimc REAL)""")


def dadostabela():
  # Não consegui identificar porque não ta aceitando dados float no codigo abaixo
  # cursor.execute('INSERT INTO dados (nome, pesopacente, alturapaciente, resultadoimc) VALUES (?,?,?,?)', (paciente, peso, altura, imcpaciente))

  cursor.execute('INSERT INTO dados (nome, resultadoimc) VALUES (?,?)', (paciente, imcpaciente))
  connection.commit()
  print("\n\nOS DADOS FORAM SALVOS\n")
  connection.close()
  os.system("pause")

paciente = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso em Kg: "))


imcpaciente = peso / (altura ** altura)

criartabela()
dadostabela()