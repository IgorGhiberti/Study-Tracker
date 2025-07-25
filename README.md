# 📚 Study Tracker

**Study Tracker** é uma ferramenta de linha de comando (CLI) feita em Python para ajudar estudantes a organizarem suas sessões de estudo, visualizarem seu progresso e manterem o foco. A proposta é ser simples, intuitiva e útil para o dia a dia de quem está estudando.

---

## Funcionalidades

- ✅ Adicionar sessões de estudo
- ✅ Registrar tempo dedicado por matéria
- ✅ Gerar logs de estudo
- ✅ Associar matérias entre si (ex: Álgebra relacionada a Matemática)
- ✅ Modo de foco
- ✅ Armazenamento local usando arquivos JSON

---
## 💻 Tecnologias
- Argparse
- Python3

---

## 🚀 Como usar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/study-tracker.git
cd study-tracker
```

### 2. Crie um ambiente virtual
- No Linux/macOS:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- No Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
### 3. Como rodar o projeto?
```
python main.py [command]
```
## Comandos principais

- `add` — Adiciona uma nova matéria ao sistema de estudos.
- `list` — Lista todas as matérias cadastradas.  
- `focus` — Inicia ou finaliza uma sessão de foco para um tópico/matéria.  
- `log` — Exibe o histórico de estudos por dia.   

## Demonstração
![Demonstração do Projeto](https://github.com/IgorGhiberti/Study-Tracker/blob/main/demonstracao.gif)
