from datetime import timedelta

start_time = 1701685759290
end_time = 1701858559290

# Calcula la diferencia en segundos
difference_seconds = (end_time - start_time) / 1000

# Convierte la diferencia a un formato legible
difference_readable = timedelta(seconds=difference_seconds)

print("Diferencia en segundos:", difference_seconds)
print("Diferencia en formato legible:", difference_readable)
