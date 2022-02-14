from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    email = Column(String)
    answers = relationship("Answers")


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    option1 = Column(String)
    option2 = Column(String)
    option3 = Column(String)
    option4 = Column(String)
    correct = Column(Integer)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    answer = Column(String)

    question_id = Column(Integer, ForeignKey("question.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    question = relationship("Question")
