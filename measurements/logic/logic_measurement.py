from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(identificador: int):
    measurement= Measurement.objects.filter(pk= identificador)
    return measurement

def delete_measurement(identificador: int):
    measurement= get_measurement(identificador)
    measurement.delete()
    return measurement

def update_measurement(identificador: int, propiedad:str, valor):
    measurement= get_measurement(identificador)
    measurement.update(value=valor)
    return measurement