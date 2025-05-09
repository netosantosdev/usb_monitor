## USB Monitor Service

**Versão Atual:** 1.6  
**Autor:** Neto Santos  
**Última atualização:** 2025-05-09

---

### 📌 Descrição

Este projeto tem como objetivo monitorar dispositivos USB conectados ao sistema operacional Windows. Ele registra eventos de inserção, remoção e ações relacionadas à movimentação de arquivos. Ideal para ambientes corporativos com foco em segurança da informação.

---

### 🆕 Novidades na Versão 1.6

- Novo script `service_laucher.py` para instalação via `NSSM`.
- Logs agora são armazenados em `C:\ProgramData\USBMonitor\Logs` (mais seguro e compatível com permissões).
- Classe `Logger` separada (`file_logger.py`) para padronização e reaproveitamento.
- Melhorias gerais na estrutura e clareza do código.
- Preparação para ambientes corporativos com controle por AD (usuário local compatível com execução global do serviço).

---

### 📁 Estrutura do Projeto

```
usb_monitor_service/
├── monitor.py              # Loop principal de monitoramento
├── usb_handler.py          # Lógica de detecção de eventos USB
├── file_logger.py          # Classe Logger responsável por gerar logs CSV
├── service_launcher.py     # Instalador do serviço usando NSSM
├── <u>requirements.txt</u> # Substituido pelo service_launcher
├── README.md               # Documentação do projeto
```

---

### ⚙️ Requisitos

- Python 3.10 ou superior
- Sistema Operacional: Windows 10/11
- Permissões de administrador para instalação do serviço
- [NSSM - Non-Sucking Service Manager](https://nssm.cc/) instalado e no PATH

---

### 🚀 Instalação do Serviço

1. **Clone o repositório**

```bash
git clone https://github.com/netosantosdev/usb_monitor.git
cd usb_monitor
```

2. **Instale as dependências**

```bash
pip install -r requirements.txt
```

3. **Instale o serviço via NSSM**

```bash
python service_launcher.py
```

> O script detecta o caminho do Python, define o serviço com o nome `USBMonitorService`, e utiliza o `monitor.py` como script principal. Os logs serão gerados automaticamente em `C:\ProgramData\USBMonitor\Logs`.

4. **Inicie o serviço (ou reinicie o computador)**

```bash
nssm start USBMonitorService
```

---

### 📄 Sobre os Logs

Os arquivos CSV são gerados por mês com o seguinte padrão de nome:

```
C:\ProgramData\USBMonitor\Logs\2025-05-USBLog.csv
```

Cada linha contém:

```
DataHora, Ação, Detalhes
```

Exemplo:
```
2025-05-09 10:23:41, USB Inserted, Kingston DataTraveler 32GB
```

---

### 🧪 Testes e Validação

- Conecte e remova um dispositivo USB para gerar eventos de teste.
- Verifique os logs em `C:\ProgramData\USBMonitor\Logs`.
- Confirme se o serviço está ativo com:

```bash
sc query USBMonitorService
```

---

### 📦 Roadmap Futuro

- Monitoramento de arquivos copiados e removidos
- Envio remoto de logs para servidor seguro
- Painel de visualização dos eventos (Dashboard Web)
- Modo silencioso com stealth logging

---

### 🔐 Segurança e Privacidade

- Este projeto é destinado a ambientes corporativos autorizados.
- Deve ser utilizado com consentimento explícito dos usuários conforme leis locais (LGPD/GDPR).
- Evite uso indevido para fins de espionagem ou vigilância sem autorização legal.