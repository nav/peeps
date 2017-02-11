import uuid
import datetime
from pony import orm

db = orm.core.Database()


class Users(db.Entity):
    id = orm.core.PrimaryKey(int, auto=True)
    uuid = orm.core.Optional(uuid.UUID, default=uuid.uuid4)
    username = orm.core.Required(str)
    token = orm.core.Optional(str)
    access_token = orm.core.Optional(str)
    refresh_token = orm.core.Optional(str)
    expiry = orm.core.Optional(datetime.datetime)


class Employee(db.Entity):
    id = orm.core.PrimaryKey(int, auto=True)
    uuid = orm.core.Optional(uuid.UUID, default=uuid.uuid4)
    given_name = orm.core.Required(str)
    family_name = orm.core.Required(str)
    email = orm.core.Required(str, unique=True)
    manager = orm.core.Optional("Employee", reverse="manager")
    role = orm.core.Optional(str)

