import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Aprende Python: Bucles", layout="centered")

# Título e introducción
st.title("🧠 Aprende Python: while, for e if")
st.markdown("""
Esta aplicación interactiva te ayudará a entender los fundamentos de los bucles `while`, `for` y la instrucción `if` en Python.  
Responde las 10 preguntas y presiona **Calcular puntaje** al final. ¡Buena suerte!
""")

# Lista de preguntas y respuestas
questions = [
    {
        "question": "¿Qué hace un bucle `while` en Python?",
        "options": [
            "Ejecuta un bloque un número fijo de veces.",
            "Ejecuta el bloque mientras una condición sea verdadera.",
            "Repite un bloque si un valor es verdadero.",
            "Detiene el programa."
        ],
        "answer": 1
    },
    {
        "question": "¿Cuál es la forma correcta de recorrer una lista `frutas` usando un bucle `for`?",
        "options": [
            "for frutas in fruta:",
            "while fruta in frutas:",
            "for fruta in frutas:",
            "loop fruta in frutas:"
        ],
        "answer": 2
    },
    {
        "question": "¿Qué imprimirá este código?\n```python\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1\n```",
        "options": [
            "1 2 3",
            "0 1 2",
            "0 1 2 3",
            "Error de sintaxis"
        ],
        "answer": 1
    },
    {
        "question": "¿Qué hace la función `range(4)` en un bucle `for`?",
        "options": [
            "Genera los números 0, 1, 2, 3",
            "Genera los números 1, 2, 3, 4",
            "Genera los números -1 a 3",
            "Genera una lista vacía"
        ],
        "answer": 0
    },
    {
        "question": "¿Qué hace la instrucción `if`?",
        "options": [
            "Ejecuta código condicionalmente",
            "Itera sobre una lista",
            "Imprime valores",
            "Asigna variables"
        ],
        "answer": 0
    },
    {
        "question": "¿Qué hace este código?\n```python\nfor i in range(3):\n    if i == 1:\n        print(\"Uno\")\n```",
        "options": [
            "Imprime 0 1 2",
            "Imprime Uno",
            "Imprime 1 Uno",
            "Error"
        ],
        "answer": 1
    },
    {
        "question": "¿Cuál es el error en este código?\n```python\nx = 0\nwhile x < 5:\nprint(x)\nx += 1\n```",
        "options": [
            "Falta un paréntesis",
            "Error de indentación",
            "Uso incorrecto de while",
            "x no está definida"
        ],
        "answer": 1
    },
    {
        "question": "¿Qué imprime este código?\n```python\nfor i in range(1, 4):\n    print(i)\n```",
        "options": [
            "0 1 2",
            "1 2 3",
            "1 2 3 4",
            "0 1 2 3"
        ],
        "answer": 1
    },
    {
        "question": "¿Qué hace la instrucción `break` en un bucle?",
        "options": [
            "Sale inmediatamente del bucle",
            "Salta a la siguiente iteración",
            "Reinicia el bucle",
            "Ignora errores"
        ],
        "answer": 0
    },
    {
        "question": "¿Qué imprime este código?\n```python\nfor i in range(3):\n    if i == 1:\n        continue\n    print(i)\n```",
        "options": [
            "0 1 2",
            "0 2",
            "1 2",
            "2"
        ],
        "answer": 1
    }
]

# Captura de respuestas
user_answers = []

with st.form("quiz_form"):
    for i, q in enumerate(questions):
        st.write(f"**{i+1}. {q['question']}**")
        selected = st.radio("Selecciona una opción:", q["options"], key=f"q{i}")
        user_answers.append(selected)
    submit = st.form_submit_button("Calcular puntaje")

# Lógica de puntuación
if submit:
    score = 0
    for i, q in enumerate(questions):
        if user_answers[i] == q["options"][q["answer"]]:
            score += 1

    st.subheader(f"Tu puntaje: {score}/10")
    
    if score == 10:
        st.balloons()
        st.success("🎉 ¡Excelente! Has respondido todas las preguntas correctamente.")
    elif score >= 7:
        st.success("✅ Buen trabajo. Puedes seguir practicando para mejorar.")
    else:
        st.warning("⚠️ Revisa tus respuestas e inténtalo nuevamente.")
