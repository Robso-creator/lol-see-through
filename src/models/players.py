from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.models import Base


class Players(Base):
    __tablename__ = 'players'
    table_description = 'Created to store all data about players'
    __table_args__ = {'info': {'description': table_description}}

    puuid = Column(
        String, index=True, primary_key=True, comment='Player unique Id',
    )
    name = Column(String, comment='Player name')
    tag = Column(String, comment='Player tag')