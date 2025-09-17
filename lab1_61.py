t = int(input("Скільки хвилин Оленка має спати: "))
h = int(input("О котрій годині Оленка лягає спати: "))
m = int(input("О котрій хвилині Оленка лягає спати: "))

start_minutes = h * 60 + m
wake_minutes = start_minutes + t

wake_h = wake_minutes // 60
wake_m = wake_minutes % 60 

print(f"Оленка прокинеться о: {wake_h} годині, {wake_m} хвилині")
