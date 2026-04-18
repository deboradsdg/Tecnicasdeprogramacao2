import json
import xml.etree.ElementTree as ET

class SistemaXML:
    def get_dados_xml(self):
        return "<usuario><nome>João</nome><idade>30</idade></usuario>"

class InterfaceJSON:
    def get_dados(self):
        pass

class XMLparaJSONAdapter(InterfaceJSON):
    def __init__(self, sistema_xml):
        self.sistema_xml = sistema_xml

    def get_dados(self):
        xml_data = self.sistema_xml.get_dados_xml()
        
      
        root = ET.fromstring(xml_data)

        dados = {}
        for child in root:
            dados[child.tag] = child.text

       
        return json.dumps(dados, ensure_ascii=False)


sistema_legado = SistemaXML()

adaptador = XMLparaJSONAdapter(sistema_legado)


print("Saída do Adaptador (JSON):")
print(adaptador.get_dados())