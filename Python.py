import matplotlib.pyplot as plt

# Datos de la tabla real
resistencia_real = [0.015, 0.487, 0.985, 1.472, 1.965, 2.461, 2.958, 3.449, 3.942, 4.432, 4.925]  # En kΩ
voltaje_real = [0.000, 0.493, 0.986, 1.479, 1.972, 2.465, 2.958, 3.451, 3.944, 4.437, 4.930]  # En V

# Convertir resistencia a ohmios para consistencia en el gráfico
resistencia_real_ohm = [r * 1000 for r in resistencia_real]

# Crear el gráfico
plt.figure(figsize=(8, 5))
plt.plot(resistencia_real_ohm, voltaje_real, marker='s', linestyle='--', color='blue', label='Valores reales')

# Añadir etiquetas a cada punto
for x, y in zip(resistencia_real_ohm, voltaje_real):
    plt.text(x, y, f'({x:.0f}, {y:.3f})', fontsize=8, ha='left')

# Configurar el gráfico
plt.title('Relación Real entre Resistencia y Voltaje')
plt.xlabel('Resistencia ($\Omega$)')
plt.ylabel('Voltaje (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Guardar el gráfico
plt.savefig('grafico_valores_reales.png', dpi=300)

# Mostrar el gráfico
plt.show()
