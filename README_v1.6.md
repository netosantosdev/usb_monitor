# Guia de Instalação e Documentação - Serviço de Monitoramento USB (v1.6)

## Novidades da v1.6
- Os arquivos de log agora são salvos em:
  ```
  C:\ProgramData\USBMonitorService\logs
  ```
  - Diretório seguro, persistente e invisível a usuários comuns
  - Permissões concedidas ao sistema para evitar falhas em ambientes com AD

## Instalação
- Python deve estar instalado em: `C:\Program Files\Python311\python.exe`
- Copie os arquivos para `C:\usb_monitor_service`
- Execute `service_launcher.bat` como administrador

## Documentação Técnica
- `file_logger.py`: atualiza os logs em ProgramData
- `usb_handler.py`: detecta e monitora arquivos em pendrives dinamicamente
- `monitor.py`: integra os módulos e inicia a execução
- `service_launcher.bat`: instala dependências, cria e reinicia o serviço via NSSM