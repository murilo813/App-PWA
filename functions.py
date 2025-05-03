import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def buscar_estoque(tabela):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT nome, estoque, disponivel, preco1, preco2 FROM {tabela}")
    dados = cur.fetchall()

    dados_convertidos = [
        (
            nome,
            estoque,
            disponivel,
            float(preco1) if preco1 not in (None, '') else 0.0,
            float(preco2) if preco2 not in (None, '') else 0.0
        ) 
        for nome, estoque, disponivel, preco1, preco2 in dados
    ]

    cur.close()
    conn.close()
    return dados_convertidos