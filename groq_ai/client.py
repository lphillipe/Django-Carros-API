import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key) if api_key else None

def get_car_ai_bio(model, brand, year):
    """
    Gera uma bio para o carro usando Groq API (Llama model)
    """
    if not client:
        return "Bio não disponível - configure GROQ_API_KEY"
    
    try:
        prompt = (
            f"Crie uma descrição de venda curta e atraente para o carro "
            f"{brand} {model} ano {year}. "
            f"Máximo 250 caracteres. Fale sobre características específicas deste modelo."
        )
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000,
            temperature=0.7,
        )

        return response.choices[0].message.content or "Bio não disponível"
    
    except Exception as e:
        print(f"Erro ao gerar bio com Groq: {e}")
        return "Bios não disponível no momento"