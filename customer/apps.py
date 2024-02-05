from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'

<<<<<<< HEAD
=======
    def ready(self):
        import customer.signals
>>>>>>> 7070e5a295172cad305ebd9d2995a29407b1bbad
