# Guia de Instalação e Documentação - Serviço de Monitoramento USB (v1.5)

## 📘 Versão 1.5 - Alterações Recentes
- 🚀 Agora o serviço detecta **novos dispositivos USB** automaticamente, mesmo após o boot.
- 🔁 Implementada varredura contínua a cada **3 segundos** com `psutil.disk_partitions()`
- ✅ Serviço mais robusto, não exige mais reinício manual após conectar pendrives.

## 📘 Versão 1.0 - Primeira versão
| Situação                          | Resultado atual                         |
| --------------------------------- | --------------------------------------- |
| **Reiniciar o computador**        | ✅ Serviço inicia automaticamente        |
| **Nenhum usuário logado**         | ✅ Serviço funciona normalmente          |
| **Pendrive já conectado no boot** | ✅ Monitorado                            |
| **Pendrive conectado depois**     | ❌ Não será monitorado (limitação atual) |
---

## 📘 Guia de Instalação

### 🔧 Requisitos
- Windows 10 ou 11
- Python 3.10 ou 3.11 instalado para **todos os usuários**
- Permissão de administrador
- NSSM (Non-Sucking Service Manager)

### 📁 Etapas

1. **Instale o Python** para todos os usuários
   - Exemplo de caminho: `C:\Program Files\Python311\python.exe`

2. **Extraia os arquivos** do serviço para:
   ```
   C:\usb_monitor_service
   ```

3. **Instale o NSSM**
   - Copie `nssm.exe` para `C:\Windows\System32`

4. **Configure o serviço**
```cmd
nssm install USBMonitorService
```
- Application Path: `C:\Program Files\Python311\python.exe`
- Arguments: `C:\usb_monitor_service\monitor.py`
- Startup Directory: `C:\usb_monitor_service`

5. **Inicie o serviço**
```cmd
nssm start USBMonitorService
```

6. **Logs gerados** em:
```
C:\LogsUSBMonitor\AAAA-MM-USBLog.csv
```

---

## 🧠 Documentação do Código (v1.5)

### Estrutura
```
usb_monitor_service/
├── monitor.py
├── usb_handler.py  ← atualizado para v1.5
├── file_logger.py
```

### `monitor.py`
- Inicia o Logger e o USBWatcher

### `usb_handler.py` (v1.5)
- Detecta pendrives com `psutil.disk_partitions()`
- Realiza varredura contínua a cada 3 segundos
- Inicia monitoramento automático de novos dispositivos

### `file_logger.py`
- Gera logs mensais por evento (criação, modificação, exclusão)

---
### Exemplo:
# Logs de Monitoramento

Abaixo estão os logs organizados por data, hora, status e local:

| Data               | Hora     | Status                | Local                                               |
|--------------------|----------|-----------------------|-----------------------------------------------------|
| 2025-05-01         | 20:08:18 | Monitoramento iniciado em | F:\                                                 |
| 2025-05-01         | 20:08:18 | Monitoramento iniciado em | E:\                                                 |
| 2025-05-01         | 20:11:44 | Monitoramento iniciado em | F:\                                                 |
| 2025-05-01         | 20:11:44 | Monitoramento iniciado em | E:\                                                 |
| 2025-05-01         | 20:11:57 | Arquivo deletado       | E:\Novo(a) Documento de Texto.txt                   |
| 2025-05-01         | 20:11:59 | Arquivo modificado     | E:\setup.exe                                        |
| 2025-05-02         | 22:16:36 | Monitoramento iniciado em | F:\                                                 |
| 2025-05-02         | 22:16:36 | Monitoramento iniciado em | E:\                                                 |
| 2025-05-02         | 22:16:37 | Arquivo modificado     | E:\System Volume Information\WPSettings.dat         |
| 2025-05-02         | 22:16:42 | Arquivo modificado     | E:\System Volume Information\IndexerVolumeGuid      |

## 📌 Comandos úteis
- Reiniciar serviço:
```cmd
nssm restart USBMonitorService
```
- Remover serviço:
```cmd
nssm remove USBMonitorService confirm
```
