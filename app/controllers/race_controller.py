"""Archivo de controlador para manejar lógica de gestión de datos de las carreras."""

from app.database import db, Carrera
import uuid

class RaceController:
    """Controlador para manejar la lógica de gestión de carreras."""

    @staticmethod
    def commit_or_rollback():
        """Intenta hacer commit a la base de datos, o hace rollback en caso de error."""
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_or_create(nombre: str, fecha: str, ubicacion: str = None) -> Carrera:
        carrera = Carrera.query.filter_by(nombre=nombre, fecha=fecha).first()
        if carrera:
            return carrera

        carrera = Carrera(
            id=str(uuid.uuid4()),
            nombre=nombre,
            fecha=fecha,
            ubicacion=ubicacion
        )
        db.session.add(carrera)
        RaceController.commit_or_rollback()
        return carrera