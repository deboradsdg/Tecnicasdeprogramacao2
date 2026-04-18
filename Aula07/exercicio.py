import csv
import json
import io


class SistemaCSV:
    def get_dados_csv(self):
     
        return "nome,idade,profissao\nJoão,30,Engenheiro\nMaria,25,Designer"

class InterfaceJSON:
    def get_dados(self):
        pass

class CSVparaJSONAdapter(InterfaceJSON):
    def __init__(self, sistema_csv):
        self.sistema_csv = sistema_csv

    def get_dados(self):
     
        csv_data = self.sistema_csv.get_dados_csv()
        
      
        f = io.StringIO(csv_data)
        leitor_csv = csv.DictReader(f)
        
        lista_dados = [linha for linha in leitor_csv]

       
        return json.dumps(lista_dados, ensure_ascii=False, indent=4)

# --- Execução ---


api_legada = SistemaCSV()

adaptador = CSVparaJSONAdapter(api_legada)

print("Dados convertidos pelo Adaptador:")
print(adaptador.get_dados())