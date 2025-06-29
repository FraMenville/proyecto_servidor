"""Archivo de controlador para manejar lógica de gestión de datos de pilotos."""

from app.database import db, Piloto
import uuid

class PilotController:
    """Controlador para manejar la lógica de gestión de pilotos."""

    @staticmethod
    def commit_or_rollback():
        """Intenta hacer commit a la base de datos, o hace rollback en caso de error."""
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_or_create(nombre: str, equipo: str, numero: str) -> Piloto:
        """Obtiene un piloto existente o crea uno nuevo si no existe."""
        piloto = Piloto.query.filter_by(nombre=nombre).first()
        if piloto:
            return piloto

        piloto = Piloto(
            id=str(uuid.uuid4()),
            nombre=nombre,
            equipo=equipo,
            numero=numero
        )
        db.session.add(piloto)
        PilotController.commit_or_rollback()
        return piloto