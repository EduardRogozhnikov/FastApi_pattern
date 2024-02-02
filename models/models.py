from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Column, Table, JSON, Boolean

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("permission", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(255), nullable=False),
    Column("username", String(255), nullable=False),
    Column("registrated_at", TIMESTAMP, default=datetime.utcnow),    #datetime.utcnow - здесь, чтобы было единое время для всех пользователей
    Column("role_id", Integer, ForeignKey(role.c.id), nullable=False),
    Column("hashed_password", String(255), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
