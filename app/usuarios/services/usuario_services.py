from app.usuarios.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    @staticmethod
    def get_all():
        return UsuarioRepository.get_all()

    @staticmethod
    def get_by_id(id):
        return UsuarioRepository.get_by_id(id)

    @staticmethod
    def create(data):
        return UsuarioRepository.create(data)

    @staticmethod
    def update(id, data):
        return UsuarioRepository.update(id, data)

    @staticmethod
    def delete(id):
        return UsuarioRepository.delete(id)

