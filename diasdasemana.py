import datetime

dias_da_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
hoje = datetime.date.today()
numero_do_dia = hoje.weekday()
nome_dia_semana = dias_da_semana[numero_do_dia]
print(f"hoje é {nome_dia_semana}")