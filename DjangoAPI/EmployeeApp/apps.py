from django.apps import AppConfig


class EmployeeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EmployeeApp'
    
    def ready(self):
        from ConsumerRunner import updater
        updater.start()