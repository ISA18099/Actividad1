import streamlit as st

st.set_page_config(page_title="Aprende Python: Bucles", layout="centered")

# --- Encabezado ---
st.title("🧠 Aprende Python: BUCLES y CONDICIONALES")
st.markdown("""
Bienvenido a esta página interactiva para aprender cómo funcionan los bucles `while`, `for` y la estructura condicional `if` en Python.

### 🧪 ¿Cómo funcionan?

- **while:** ejecuta un bloque de código mientras una condición sea verdadera.
- **for:** recorre elementos de una secuencia (como listas o rangos).
- **if:** evalúa condiciones para decidir qué bloque ejecutar.

---

### ✅ Responde el siguiente test y aprende más en el proceso:
""")

# --- Lista de preguntas ---
questions = [
    {
        "question": "1. ¿Qué hace un bucle `while` en Python?",
        "options": [
            "Ejecuta un bloque de código un número fijo de veces.",
            "Ejecuta el bloque mientras una condición sea verdadera.",
            "Detiene el programa.",
            "Imprime los elementos de una lista."
        ],
        "answer": 1
    },
    {
        "question": "2. ¿Cuál es la sintaxis correcta de un bucle `for` para recorrer una lista `numeros`?",
        "options": [
            "for numero in numeros:",
            "while numero in numeros:",
            "for numeros in numero:",
            "loop numero in numeros:"
        ],
        "answer": 0
    },
    {
        "question": "3. ¿Cuál es el resultado de este código?\n```python\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1\n```",
        "options": [
            "1 2 3",
            "0 1 2",
            "0 1 2 3",
            "x x x"
        ],
        "answer": 1
    },
    {
        "question": "4. En un bucle `for`, ¿qué hace `range(5)`?",
        "options": [
            "Genera números del 1 al 5.",
            "Genera números del 0 al 5 (inclusive).",
            "Genera números del 0 al 4.",
            "Genera una lista infinita."
        ],
        "answer": 2
    },
    {
        "question": "5. ¿Cuál es el propósito de `if` en Python?",
        "options": [
            "Crear bucles.",
            "Comparar listas.",
            "Ejecutar un bloque de código si se cumple una condición.",
            "Declarar funciones."
        ],
        "answer": 2
    },
    {
        "question": "6. ¿Qué imprimirá este código?\n```python\nfor i in range(3):\n    if i == 1:\n        print('uno')\n```",
        "options": [
            "0 1 2",
            "uno",
            "1 uno",
            "0 uno 2"
        ],
        "answer": 1
    },
    {
        "question": "7. ¿Cuál es el error en este código?\n```python\nx = 0\nwhile x < 5:\nprint(x)\nx += 1\n```",
        "options": [
            "Falta de paréntesis.",
            "Indentación incorrecta.",
            "Uso incorrecto de while.",
            "Variable mal definida."
        ],
        "answer": 1
    },
    {
        "question": "8. ¿Cuál es la salida de este código?\n```python\nfor i in range(1, 4):\n    print(i)\n```",
        "options": [
            "0 1 2",
            "1 2 3",
            "1 2 3 4",
            "0 1 2 3"
        ],
        "answer": 1
    },
    {
        "question": "9. ¿Qué hace `break` en un bucle?",
        "options": [
            "Finaliza el bucle inmediatamente.",
            "Reinicia el bucle.",
            "Continúa con la siguiente iteración.",
            "Ignora el código del if."
        ],
        "answer": 0
    },
    {
        "question": "10. ¿Cuál es la salida de este código?\n```python\nfor i in range(3):\n    if i == 1:\n        continue\n    print(i)\n```",
        "options": [
            "0 1 2",
            "0 2",
            "1 2",
            "2"
        ],
        "answer": 1
    },
]

# --- Mostrar formulario interactivo ---
st.markdown("### 📝 Test de 10 Preguntas")

user_answers = []
with st.form("quiz_form"):
    for i, q in enumerate(questions):
        user_choice = st.radio(q["question"], q["options"], key=f"q{i}")
        user_answers.append(user_choice)
    submitted = st.form_submit_button("Calcular Puntaje")

# --- Resultado ---
if submitted:
    score = 0
    for i, q in enumerate(questions):
        if q["options"].index(user_answers[i]) == q["answer"]:
            score += 1
    st.success(f"🎯 Tu puntaje final es: {score} / 10")
    if score == 10:
        st.balloons()
        st.success("🎉 ¡Perfecto! Has dominado los conceptos de bucles y condicionales en Python.")
    elif score >= 7:
        st.info("✅ ¡Muy bien! Sigue practicando para perfeccionarte.")
    else:
        st.warning("🔄 Puedes repasar los conceptos y volver a intentarlo.")

# --- Instrucciones de despliegue (para tu GitHub) ---
st.markdown("""---  
#### ¿Cómo desplegar esta app desde GitHub en Streamlit?
1. Crea un repositorio en GitHub y sube este archivo como `app.py`.  
2. Añade un `requirements.txt` con el siguiente contenido:  
