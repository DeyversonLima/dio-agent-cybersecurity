# DIO Agent · Mentor de cibersegurança

Projeto final do bootcamp **Santander - Cibersegurança do Zero a prática**, baseado no [DIO Agent](https://github.com/digitalinnovationone/dio-agent) (revisão `5f5e11d`).

A especialização ajuda o estudante a investigar uma falha, avaliar o risco no cenário apresentado e testar a correção. O comportamento é definido em Markdown e carregado pelo agente durante a conversa.

## Rode no Hermes

1. Instale o Hermes pelo [guia oficial](https://hermes-agent.nousresearch.com/docs/getting-started/installation) e configure seu provedor de modelo com `hermes setup`.
2. Abra no VS Code a pasta que contém `AGENTS.md`. No terminal integrado dessa pasta, execute `hermes`.
3. Siga os prompts do [laboratório local](lab/README.md). Use Python 3 para executar `python -m unittest discover -s lab -v` na raiz.

## Arquivos da especialização

| Arquivo | Papel |
|---|---|
| [Roteiro da skill](skills/vulnerability-analysis/SKILL.md) | Coleta contexto, avalia o risco e orienta a correção e a revalidação. |
| [Guia da skill](skills/vulnerability-analysis/README.md) | Explica como iniciar uma análise e o que esperar. |
| [Fundamentos de segurança](agent/knowledge/security-basics.md) | Define ameaça, vulnerabilidade e risco, explica a tríade de segurança e reúne práticas defensivas. |
| [Persona](agent/persona.md) | Acrescenta a postura de mentor de segurança. |
| [AGENTS.md](AGENTS.md) | Registra a skill e a referência de conhecimento. |
| [Laboratório](lab/README.md) | Reproduz a SQL Injection com dados fictícios e verifica a consulta parametrizada. |

## Melhoria escolhida

O agente usa um formato fixo de análise com escopo, achado e evidência, impacto, probabilidade, severidade, correção e revalidação. A matriz qualitativa permite justificar a prioridade em situações diferentes. Quando faltam dados para classificar o risco, a análise registra a lacuna.

## Evidências no Hermes

As três sessões foram realizadas com Hermes Agent v0.23.0 e o modelo `upstage/solar-mini4:free`. Os PDFs são exportações das conversas e incluem as respostas intermediárias.

| Sessão | O que demonstra |
|---|---|
| [Análise do login vulnerável](images/images%20PDF/Review%20vulnerable%20login%20logic%20in%20lab_app%20py.pdf) | A revisão do `app.py` vulnerável em uma cópia local identifica a concatenação, explica o desvio de autenticação e propõe parâmetros. T1190 é discutido para a hipótese de aplicação exposta publicamente. |
| [Reanálise após a correção](images/images%20PDF/Review%20lab%20app%20py%20test%20app%20py.pdf) | A consulta parametrizada mantém o login válido, rejeita a senha incorreta e bloqueia a entrada que contornava o login vulnerável. Os três testes passaram. |
| [Avaliação do Ubuntu hipotético](images/images%20PDF/Analyze%20laboratory%20Ubuntu%20server%20security.pdf) | Um pedido espontâneo leva o Hermes a abrir a skill local e perguntar sobre autorização antes de sugerir comandos. Após revisão guiada, o agente separa tentativas da probabilidade de comprometimento e registra a severidade como indeterminada. |

Na sessão do Ubuntu, a primeira resposta também perguntou pelo nível de experiência. A avaliação inicial confundiu a frequência de tentativas com a chance de comprometimento e precisou de revisão. A transcrição registra essas limitações e a correção final. Nenhum servidor real foi avaliado.

---


# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/digitalinnovationone/dio-agent.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                Este guia
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── agent/
│   ├── persona.md           A personalidade e o tom do agente
│   └── knowledge/           O que o agente sabe sobre a DIO
├── skills/                  Uma pasta por skill, cada uma com o seu SKILL.md
└── docs/
    ├── glossary.md          Glossário de termos
    └── youcom-mcp.md        Como conectar a busca do You.com
```

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
