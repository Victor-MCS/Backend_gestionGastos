from app.auth.repositories.auth_repository import AuthRepository

class AuthService:
    @staticmethod
    def create_user(email, name, password):
        return AuthRepository.create_user(email, name, password)

    @staticmethod
    def get_user(email, password):
        return AuthRepository.get_user(email, password)
