from app.tarjetas.repositories.tarjetas_repository import TarjetasRepository

class TarjetasService:
    @staticmethod
    def get_all(id):
        return TarjetasRepository.get_all(id)

    @staticmethod
    def get_by_id(id):
        return TarjetasRepository.get_by_id(id)

    @staticmethod
    def create(data):
        return TarjetasRepository.create(data)

    @staticmethod
    def update(id, data):
        return TarjetasRepository.update(id, data)

    @staticmethod
    def delete(id):
        return TarjetasRepository.delete(id)
