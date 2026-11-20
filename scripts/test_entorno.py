import torch
import os

print("=== VERIFICANDO ENTORNO EN LA NUBE ===")
if torch.cuda.is_available():
    print(f"GPU detectada con éxito: {torch.cuda.get_device_name(0)}")
else:
    print("AVISO: No hay GPU activa. Actívala en Colab (Entorno de ejecución > Cambiar tipo de entorno > T4 GPU).")

os.makedirs("outputs", exist_ok=True)
print("Carpetas listas para generar contenido.")
