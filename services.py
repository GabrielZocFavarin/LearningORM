from database import SessionLocal
from models import Valor

def salvar_valor(valor_input):
    db = SessionLocal()
    try:
        novo = Valor(valor=valor_input)
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo
    finally:
        db.close()