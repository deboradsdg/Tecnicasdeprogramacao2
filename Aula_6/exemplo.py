class ConfigManager:  # Corrigido o nome de Mananger para Manager
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Criando nova instância de ConfigManager...")
            # Corrigido: __new__ (minúsculo) e chamada super() correta
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._config = {}
        else:
            print("Usando instância existente do ConfigManager...")
        return cls._instance

    def set_config(self, key, value):
        self._config[key] = value
    
    def get_config(self, key):
        # Corrigido: ponto (.) em vez de ponto e vírgula (;)
        return self._config.get(key, None)

    def show_all(self):
        # Corrigido: 'key' em vez de 'kay'
        for key, value in self._config.items():
            print(f'{key}: {value}')

# Testando o funcionamento
config1 = ConfigManager()
config2 = ConfigManager()

config1.set_config("app_name", "Sistema Financeiro")
config1.set_config("version", "1.0")
config1.set_config("mode", "produção")

print(f"\nApp Name via config2: {config2.get_config('app_name')}")
print(f"Mode via config2: {config2.get_config('mode')}\n")

config2.show_all()

# Corrigido: 'is' para verificar se são o mesmo objeto
print(f"\nAs instâncias são iguais? {config1 is config2}")