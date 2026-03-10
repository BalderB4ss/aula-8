from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    idade = Column(Integer)
    curso = Column(String(150))

    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def __repr__(self):
        return f"Aluno (id={self.id}, nome={self.nome}, idade={self.idade}, curso={self.curso})"

engine = create_engine("sqlite:///escola.db", echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

aluno1 = Aluno("Cassio", 16, "Dev. Sistemas")
aluno2 = Aluno("Balder", 17, "Dev. Sistemas")
aluno3 = Aluno("Emilly", 16, "Dev. Sistemas")
aluno4 = Aluno("Vitória", 16, "Dev. Sistemas")
aluno5 = Aluno("Raul", 17, "Dev. Sistemas")
aluno6 = Aluno("Guilherme", 16, "Dev. Sistemas")
aluno7 = Aluno("Sérgio", 45, "Culinária")
aluno8 = Aluno("João", 27, "Boy band")
# session.add(aluno1)
# session.add(aluno2)
# session.add(aluno3)
# session.add(aluno4)
# session.add(aluno5)
# session.add(aluno6)
# session.add(aluno7)
# session.add(aluno8)
# session.commit()

# alunos = session.query(Aluno).all()
# for i in alunos:
#     print(f"Nome: {i.nome} | Idade: {i.idade} | Curso: {i.curso}")

aluno_id = session.query(Aluno).filter(Aluno.id == 1).first()
print(aluno_id)

atualizar_aluno = session.query(Aluno).filter_by(id=1).first()