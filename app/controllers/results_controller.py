"""Archivo de controlador para manejar lógica de gestión de datos de los resultados de las carreras."""

from app.database import db, Resultado
import uuid

class ResultController:
    """Controlador para manejar la lógica de gestión de resultados de carreras."""
    @staticmethod
    def commit_or_rollback():
        """Intenta hacer commit a la base de datos, o hace rollback en caso de error."""
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_or_create(
        piloto_id: str,
        carrera_id: str,
        posicion: int,
        vueltas: int,
        tiempo: str,
        intervalo: str,
        velocidad_promedio: str,
        paradas: int,
        retiro: str = None,
        motor: str = None
    ) -> Resultado:
        """Obtiene un resultado existente o crea uno nuevo si no existe."""
        resultado = Resultado.query.filter_by(
            piloto_id=piloto_id, carrera_id=carrera_id, posicion=posicion
        ).first()
        
        if resultado:
            return resultado

        resultado = Resultado(
            id=str(uuid.uuid4()),
            piloto_id=piloto_id,
            carrera_id=carrera_id,
            posicion=posicion,
            vueltas=vueltas,
            tiempo=tiempo,
            intervalo=intervalo,
            velocidad_promedio=velocidad_promedio,
            paradas=paradas,
            retiro=retiro,
            motor=motor
        )
        
        db.session.add(resultado)
        ResultController.commit_or_rollback()
        return resultado