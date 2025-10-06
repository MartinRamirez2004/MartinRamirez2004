from datetime import datetime
import pytz

# Zona horaria de Colombia
zona = pytz.timezone("America/Bogota")
ahora = datetime.now(zona)

hora = ahora.hour
hora_str = ahora.strftime("%I:%M %p")

# Determinar saludo
if 5 <= hora < 12:
    saludo = "☀️ ¡Buenos días!"
elif 12 <= hora < 18:
    saludo = "🌤️ ¡Buenas tardes!"
else:
    saludo = "🌙 ¡Buenas noches!"

# Contenido del README
contenido = f"""# Hola, soy Martin 👋

{saludo}

🕓 Hora inicial: {hora_str} (Colombia)
(El reloj sera actualizado automaticamente cada hora)

---

🎓 Estudiante de **Tecnología en Desarrollo de Software**  
💻 Apasionado por el **desarrollo web**, la **optimización de sistemas** y la **creación de aplicaciones prácticas y escalables**.  
🚀 Mi meta es seguir mejorando como desarrollador y construir proyectos que realmente aporten valor.  

---

📊 Este perfil se actualiza automáticamente cada hora con un mensaje dinámico.

---

¡Gracias por visitar mi perfil! 💻
"""

# Sobrescribir el README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(contenido)
