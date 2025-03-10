from openai import OpenAI  # pip install openai
from dotenv import load_dotenv
load_dotenv()

modelo = "gpt-4o-mini"

client = OpenAI()

lista_modelos = client.models.list()
for indice, modelo_listado in enumerate(lista_modelos):
    # print(modelo_listado.id)
    pass

def generate_answer(messages, modelo="gpt-4o-mini"):
    try:
        response = client.chat.completions.create(
            model=modelo,
            messages=[{"role": "user", "content": messages}],
            # seed=42,
        )

        return response
    except Exception as e:
        print("Erro", e)
        return e


pergunta = """Qual a capital do Brasil?"""

print("Enviando")

print("\nPergunta:")
print(pergunta)

resposta = generate_answer(pergunta, modelo=modelo)

print(f"\nResposta original({modelo}):")
print(resposta)

print(f"\nResposta ({modelo}):")
print(resposta.choices[0].message.content)