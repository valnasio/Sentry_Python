# 📡 Modelo Base de Integração com Sentry (Python)

Este projeto é um **modelo pronto de integração com o Sentry**, criado para ser reutilizado em outros projetos Python.

Ele já vem configurado para capturar erros automaticamente e enviar para o painel do Sentry, facilitando o monitoramento e rastreamento de falhas em aplicações.

---

## 🎯 Objetivo

Servir como base reutilizável para:

- Monitoramento de erros em produção
- Debug mais rápido
- Observabilidade básica
- Padronização de integração com Sentry

Basta copiar a estrutura para outro projeto e configurar o `.env` com o seu `SENTRY_DSN`.

---

## ⚙️ Como funciona

O projeto:

1. Carrega variáveis de ambiente com `python-dotenv`
2. Inicializa o Sentry usando o `SENTRY_DSN`
3. Ativa integração com OpenTelemetry (OTLP)
4. Captura exceções automaticamente
5. Envia os eventos para o painel do Sentry

---

## 🔐 Configuração

Crie um arquivo `.env`:

```
SENTRY_DSN=sua_url_do_sentry_aqui
```

Depois execute normalmente o script Python.

---

## 🧠 O que é o Sentry?

O **Sentry** é uma plataforma de monitoramento de erros e observabilidade.

Ele permite:

- Visualizar stack traces completos
- Identificar linha exata do erro
- Monitorar aplicações em tempo real
- Agrupar erros semelhantes
- Receber alertas automáticos
- Acompanhar performance da aplicação

É muito usado em ambientes de produção para aumentar confiabilidade e reduzir tempo de resolução de problemas.

---

## 🔎 O que é OpenTelemetry (OTLP)?

**OpenTelemetry** é um padrão aberto para coleta de:

- Logs
- Métricas
- Traces (rastreamento de requisições)

A integração `OTLPIntegration()` permite que o Sentry:

- Capture rastreamento distribuído
- Monitore performance
- Analise fluxo de execução da aplicação
- Integre com outras ferramentas de observabilidade

Isso transforma o Sentry não apenas em um monitor de erros, mas também em uma ferramenta de observabilidade mais completa.

---

## 📦 Dependências

- sentry-sdk
- python-dotenv

---

## 🚀 Como reutilizar em outros projetos

1. Instale as dependências
2. Copie o bloco de inicialização do Sentry
3. Configure o `.env`
4. Execute sua aplicação

Pronto — o monitoramento já estará ativo.

---

## 📌 Indicado para

- APIs (FastAPI, Flask, Django)
- Scripts Python
- Aplicações backend
- Serviços rodando em AWS, Docker ou servidores Linux

---

Projeto criado como base reutilizável para padronizar monitoramento com Sentry em aplicações Python.