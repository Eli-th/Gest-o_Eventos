import sqlite3

# Criar banco e conexão
conn = sqlite3.connect("eventos.db")
cursor = conn.cursor()

# Dropar tabelas se existirem para evitar erros
cursor.execute("DROP TABLE IF EXISTS Inscricao")
cursor.execute("DROP TABLE IF EXISTS Evento")
cursor.execute("DROP TABLE IF EXISTS Usuario")


# Criar tabelas
cursor.execute("""
CREATE TABLE Usuario (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  email TEXT NOT NULL,
  tipo TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE Evento (
  id INTEGER PRIMARY KEY,
  titulo TEXT,
  data TEXT,
  local TEXT,
  descricao TEXT
)
""")

cursor.execute("""
CREATE TABLE Inscricao (
  id INTEGER PRIMARY KEY,
  usuario_id INTEGER,
  evento_id INTEGER,
  confirmado BOOLEAN,
  FOREIGN KEY(usuario_id) REFERENCES Usuario(id),
  FOREIGN KEY(evento_id) REFERENCES Evento(id)
)
""")

# Inserir dados
cursor.execute("INSERT INTO Usuario (nome, email, tipo) VALUES (?, ?, ?)", ("João", "joao@email.com", "participante"))
cursor.execute("INSERT INTO Evento (titulo, data, local, descricao) VALUES (?, ?, ?, ?)",
               ("Peça Infantil", "2025-06-01", "SESC Nova Iguaçu", "Teatro para crianças"))

# Consultar dados
cursor.execute("""
SELECT Usuario.nome, Evento.titulo FROM Inscricao
JOIN Usuario ON Inscricao.usuario_id = Usuario.id
JOIN Evento ON Inscricao.evento_id = Evento.id
""")

print(cursor.fetchall())
conn.commit()
conn.close()
