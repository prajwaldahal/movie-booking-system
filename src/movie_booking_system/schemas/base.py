from pydantic import BaseModel, ConfigDict


class ORMModel(BaseModel):
    # lets Pydantic read attributes straight off SQLAlchemy objects
    model_config = ConfigDict(from_attributes=True)
