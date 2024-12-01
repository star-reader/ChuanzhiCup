from typing import List, Optional, Any
from sqlalchemy import DateTime, Engine, ForeignKey, String, create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.orm import DeclarativeBase

from Common import SingletonClass

DB_URL = ""



# SQLAlchemy User model
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    password = mapped_column(String(100), nullable=False)  # 存储加密后的密码
    email = mapped_column(String(100), unique=True)
    created_at = mapped_column(DateTime)
    updated_at = mapped_column(DateTime)
    token: Mapped["Token"] = relationship(back_populates="user")

    def __repr__(self):
        return f"User<id={self.id},username={self.username},password={self.password}>"
class Token(Base):
    __tablename__ = 'tokens'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userId = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="token")


class DBHelper(metaclass=SingletonClass):
    def __init__(self) -> None:
        self._engine: Engine = create_engine(DB_URL, echo=True)

        Base.metadata.create_all(bind=self._engine)
        self.SessionLocal = sessionmaker(bind=self._engine)

    def insert(self, data: Base) -> None:
        session = self.SessionLocal()
        try:
            session.add(data)  # 将数据添加到会话中
            session.commit()   # 提交会话
        except Exception as e:
            session.rollback()  # 回滚会话
            raise e  # 抛出异常
        finally:
            session.close()  # 关闭会话

    def select(self, table: Base, **filters) -> Optional[List[Base]]:
        session = self.SessionLocal()
        try:
            return session.query(table).filter_by(**filters).all()  # 根据过滤条件查找
        finally:
            session.close()  # 关闭会话

    def update(self, table: Base, key: str, key_value: Any, **updates) -> None:
        session = self.SessionLocal()
        try:
            # 根据键值查找记录
            record = session.query(table).filter(getattr(table, key) == key_value).first()
            if record:
                for attr, value in updates.items():
                    setattr(record, attr, value)  # 更新记录的属性
                session.commit()  # 提交更改
            else:
                raise ValueError("Record not found")  # 如果未找到记录，抛出异常
        except Exception as e:
            session.rollback()  # 回滚会话
            raise e  # 抛出异常
        finally:
            session.close()  # 关闭会话

    def deleteRecord(self, table: Base, key: str, key_value: Any) -> None:
        session = self.SessionLocal()
        try:
            # 根据键值查找记录
            record = session.query(table).filter(getattr(table, key) == key_value).first()
            if record:
                session.delete(record)  # 删除记录
                session.commit()  # 提交更改
            else:
                raise ValueError("Record not found")  # 如果未找到记录，抛出异常
        except Exception as e:
            session.rollback()  # 回滚会话
            raise e  # 抛出异常
        finally:
            session.close()  # 关闭会话



if __name__ == "__main__":
    DB_URL = "sqlite:///test.db"
    helper:DBHelper = DBHelper()
    bob = User(username="Bob",password="123")
    #test insert
    helper.insert(bob)
    print(helper.select(User,username="Bob"))
    helper.update(User,"username","Bob",password="456")
    print(helper.select(User,username="Bob"))
    helper.deleteRecord(User,"id",1)

