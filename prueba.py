
import tkinter as tk
from tkinter import scrolledtext
import openai


# Configuración de la clave de API de OpenAI
openai.api_key = "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"

def obtener_respuesta(pregunta):
    # Llama a la API de OpenAI para obtener una respuesta
    respuesta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=pregunta,
        temperature=0.7,
        max_tokens=150
    )
    return respuesta.choices[0].text.strip()

def enviar_mensaje():
    # Obtiene la pregunta del usuario
    pregunta = entrada_texto.get("1.0", tk.END).strip()

    if pregunta:
        # Muestra la pregunta en el área de chat
        chat_area.insert(tk.END, f"Usuario: {pregunta}\n")

        # Obtiene la respuesta de GPT
        respuesta = obtener_respuesta(pregunta)

        # Muestra la respuesta en el área de chat
        chat_area.insert(tk.END, f"ChatGPT: {respuesta}\n")

        # Limpia la entrada de texto
        entrada_texto.delete("1.0", tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("ChatGPT")

# Área de chat (ScrolledText)
chat_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=40, height=10)
chat_area.pack(padx=10, pady=10)

# Entrada de texto para preguntas
entrada_texto = tk.Text(ventana, height=3, width=40)
entrada_texto.pack(padx=10, pady=10)

# Botón para enviar preguntas
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(pady=10)

# Inicia el bucle de la aplicación
ventana.mainloop()