import streamlit as st
import random

st.set_page_config(page_title="Aprende Python: Bucles", layout="centered")

# ----- Título e Introducción -----
st.title("Aprende Python: Bucles While, For e If")
st.markdown("""
Este cuestionario interactivo te ayudará a aprender y practicar el uso de los bucles `while`, `for` y la condición `if` en Python. 🧰

Selecciona la respuesta correcta para cada pregunta. Al finalizar, haz clic en **Calcular Puntaje**.
""")

# ----- Preguntas y alternativas -----
questions = [
    {
        "question": "1. ¿Qué hace un bucle `while` en Python?",
        "options": [
            "Ejecuta un bloque de código un número fijo de veces.",
            "Ejecuta el bloque de código mientras una condición sea verdadera.",
            "Detiene el programa inmediatamente.",
            "Imprime solo los elementos de una lista"
        ],
        "answer": 1
    },
    {
        "question": "2. ¿Cuál es la sintaxis correcta de un bucle `for` para recorrer una lista llamada `numeros`?",
        "options": [
            "for numero in numeros:",
            "while numero in numeros:",
            "for numeros in numero:",
            "loop numero in numeros:"
        ],
        "answer": 0
    },
    {
        "question": "3. ¿Cuál es el resultado de este código?"
```python
x = 0
while x < 3:
    print(x)
    x += 1
```",
        "options": [
            "1 2 3", "0 1 2", "0 1 2 3", "x x x"
        ],
        "answer": 1
    },
    {
        "question": "4. En un bucle `for`, ¿qué hace la función `range(5)`?",
        "options": [
            "Genera los números del 1 al 5.",
            "Genera los números del 0 al 5 (inclusive).",
            "Genera los números del 0 al 4.",
            "Genera una lista infinita."
        ],
        "answer": 2
    },
    {
        "question": "5. ¿Cuál es el propósito de la instrucción `if` en Python?",
        "options": [
            "Crear bucles.", "Comparar listas.", "Ejecutar condicionalmente un bloque de código.", "Declarar variables."
        ],
        "answer": 2
    },
    {
        "question": "6. ¿Qué imprimirá este código?
```python
for i in range(3):
    if i == 1:
        print("uno")
```",
        "options": ["0 1 2", "uno", "1 uno", "0 uno 2"],
        "answer": 1
    },
    {
        "question": "7. ¿Cuál es el error en este código?
```python
x = 0
while x < 5:
print(x)
x += 1
```",
        "options": [
            "Falta de paréntesis.", "Indentación incorrecta.", "Uso incorrecto del while.", "Variable mal definida."
        ],
        "answer": 1
    },
    {
        "question": "8. ¿Cuál es la salida de este código?
```python
for i in range(1, 4):
    print(i)
```",
        "options": ["0 1 2", "1 2 3", "1 2 3 4", "0 1 2 3"],
        "answer": 1
    },
    {
        "question": "9. ¿Qué hace `break` en un bucle?",
        "options": [
            "Finaliza el bucle inmediatamente.", "Reinicia el bucle.", "Continúa con la siguiente iteración.", "Ignora el código."
        ],
        "answer": 0
    },
    {
        "question": "10. ¿Cuál es la salida de este código?
```python
for i in range(3):
    if i == 1:
        continue
    print(i)
```",
        "options": ["0 1 2", "0 2", "1 2", "2"],
        "answer": 1
    }
]

# ----- Lógica para capturar respuestas -----
user_answers = []

with st.form("quiz_form"):
    for i, q in enumerate(questions):
        user_answer = st.radio(q["question"], q["options"], key=i)
        user_answers.append(user_answer)
    submitted = st.form_submit_button("Calcular Puntaje")

# ----- Evaluar y mostrar resultados -----
if submitted:
    score = 0
    for i, q in enumerate(questions):
        if q["options"].index(user_answers[i]) == q["answer"]:
            score += 1
    st.success(f"Tu puntaje final es: {score}/10")

    if score == 10:
        st.balloons()
    elif score >= 7:
        st.info("🌟 ¡Muy bien! Estás dominando los bucles.")
    else:
        st.warning("❌ Revisa tus respuestas y vuelve a intentarlo.")
