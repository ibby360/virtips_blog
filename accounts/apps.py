from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # Starts signals to create author profile.
    def ready(self):
        import accounts.signals
