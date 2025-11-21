from database import SessionLocal
from models import valor

def salvar_valor(valor_input):
    db = SessionLocal()
    try:
        new_value = valor_input
        db.add(new_value)
        db.commit()
        db.refresh(new_value)
        return new_value
    finally:
        db.close()

