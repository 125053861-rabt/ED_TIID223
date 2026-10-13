print("-----------Pilas-------------")
historial = []

historial.append("chatgpt.com")
historial.append("gemini.com")
historial.append("claude.com")

print("Historial: ", historial)

pagina_actual = historial[2]
print("Pagina Actual: ", pagina_actual)
pagina_salida = historial.pop()
print("Pagina salida: ", pagina_salida)