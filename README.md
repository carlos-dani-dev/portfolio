# Portfolio Pessoal - Carlos Daniel Portela

Portfólio profissional desenvolvido em **Vue 3** com foco em apresentar experiências como Desenvolvedor Fullstack e Pesquisador de Machine Learning. O projeto inclui internacionalização (pt-BR/en-USA), tema claro/escuro, e deploy automático no GitHub Pages.

## 🌐 Live Demo

[https://carlos-dani-dev.github.io/portfolio/](https://carlos-dani-dev.github.io/portfolio/)

## ✨ Funcionalidades

- 🌍 **Internacionalização (i18n)**: Suporte a português (pt-BR) e inglês (en-USA)
- 🎨 **Tema Claro/Escuro**: Alternância de tema com persistência no localStorage
- 📱 **Design Responsivo**: Layout adaptado para desktop e mobile com menu hamburger
- 📄 **Página de Currículo**: Versão para impressão/download do currículo em PDF
- 🎯 **Navegação SPA**: Single Page Application com Vue Router
- 💻 **Componentes Modulares**: Arquitetura baseada em componentes reutilizáveis
- 🚀 **Deploy Automático**: CI/CD via GitHub Actions para GitHub Pages
- 📝 **Markdown Rendering**: Renderização de conteúdo Markdown com markdown-it
- 🎨 **TailwindCSS v4**: Estilização utility-first moderna

## 🛠️ Stack Tecnológica

### Frontend

| Tecnologia | Versão | Propósito |
|---|---|---|
| [Vue 3](https://vuejs.org/) | ^3.5.38 | Framework JavaScript com Composition API e `<script setup>` |
| [Vite](https://vite.dev/) | ^8.0.16 | Build tool, dev server e HMR |
| [Vue Router](https://router.vuejs.org/) | ^5.1.0 | Roteamento client-side |
| [Pinia](https://pinia.vuejs.org/) | ^3.0.4 | Gerenciamento de estado (tema, idioma) |
| [Vue I18n](https://vue-i18n.intlify.dev/) | ^11.4.6 | Internacionalização |
| [TailwindCSS](https://tailwindcss.com/) | ^4.3.2 | Framework CSS utility-first |
| [markdown-it](https://github.com/markdown-it/markdown-it) | ^14.3.0 | Renderização de Markdown |
| [@vitejs/plugin-vue](https://github.com/vitejs/vite-plugin-vue) | ^6.0.7 | Plugin Vue para Vite |
| [vite-svg-loader](https://github.com/jpkleemans/vite-svg-loader) | ^5.1.1 | Importação de SVG como componentes |
| [vite-plugin-vue-devtools](https://github.com/vuejs/devtools-next) | ^8.1.2 | Vue DevTools para desenvolvimento |

### DevOps

| Tecnologia | Propósito |
|---|---|
| [GitHub Actions](https://github.com/features/actions) | CI/CD para deploy automático |
| [GitHub Pages](https://pages.github.com/) | Hospedagem estática |

## 📁 Estrutura do Projeto

```
portfolio/
├── frontend/                    # Aplicação Vue.js
│   ├── src/
│   │   ├── assets/           # Arquivos estáticos
│   │   │   ├── main.css      # Estilos globais
│   │   │   ├── base.css      # Variáveis CSS e temas
│   │   │   ├── icons/        # Ícones SVG (tecnologias, redes sociais)
│   │   │   ├── images/       # Imagens (foto de perfil)
│   │   │   └── videos/       # Vídeos de demonstração
│   │   ├── components/       # Componentes Vue
│   │   │   ├── Header.vue    # Navegação principal
│   │   │   ├── AboutMe.vue   # Seção sobre mim
│   │   │   ├── Me.vue        # Apresentação pessoal
│   │   │   ├── Stacks.vue    # Stack tecnológica
│   │   │   ├── Projects.vue  # Projetos destacados
│   │   │   ├── Experiences.vue # Experiência profissional
│   │   │   ├── Contact.vue   # Formulário de contato
│   │   │   └── MarkdownText.vue # Componente de renderização Markdown
│   │   ├── views/            # Páginas principais
│   │   │   ├── Home.vue      # Página inicial (landing page)
│   │   │   └── Resume.vue    # Página de currículo
│   │   ├── router/          # Configuração de rotas
│   │   │   └── router.js     # Definição das rotas SPA
│   │   ├── stores/           # Pinia stores (estado global)
│   │   │   ├── themeStore.js # Gerenciamento de tema claro/escuro
│   │   │   └── langStore.js  # Gerenciamento de idioma
│   │   ├── locales/          # Arquivos de tradução i18n
│   │   │   ├── pt-br.js      # Tradução português
│   │   │   └── en-usa.js     # Tradução inglês
│   │   ├── main.js           # Entry point da aplicação
│   │   └── App.vue           # Componente raiz
│   ├── public/               # Arquivos públicos
│   │   └── me.png            # Foto de perfil
│   ├── index.html            # Template HTML
│   ├── vite.config.js        # Configuração do Vite
│   ├── package.json          # Dependências e scripts
│   └── jsconfig.json         # Configuração JavaScript
├── .github/
│   └── workflows/
│       └── deploy.yml       # Workflow CI/CD para GitHub Pages
└── README.md                 # Esta documentação
```

## 🚀 Como Rodar Localmente

### Pré-requisitos

- [Node.js](https://nodejs.org/) `^22.18.0` ou `>=24.12.0`
- npm ou yarn

### Instalação e Execução

```bash
# Clone o repositório
git clone https://github.com/carlos-dani-dev/portfolio.git
cd portfolio/frontend

# Instale as dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

A aplicação estará disponível em `http://localhost:5173`.

### Build para Produção

```bash
# Crie o build de produção
npm run build

# Preview do build de produção
npm run preview
```

## 🎨 Temas e Personalização

### Tema Claro/Escuro

O projeto implementa dois temas:
- **Light**: Tema claro para ambientes iluminados
- **Dark-Default**: Tema escuro para ambientes com pouca luz

A preferência do usuário é persistida no `localStorage` e aplicada automaticamente ao carregar a página.

### Variáveis CSS

As cores e estilos são definidos através de variáveis CSS em `src/assets/base.css`, permitindo fácil personalização:

```css
:root {
  --color-bg: #ffffff;
  --color-text: #1a1a1a;
  /* ... outras variáveis */
}

[page-theme="dark-default"] {
  --color-bg: #0a0a0a;
  --color-text: #e5e5e5;
  /* ... outras variáveis */
}
```

## 🌍 Internacionalização

O projeto suporta dois idiomas configurados via Vue I18n:

- **pt-BR**: Português Brasileiro (idioma padrão)
- **en-USA**: Inglês Americano

Os arquivos de tradução estão localizados em `src/locales/` e contêm todas as strings da interface. A seleção de idioma é persistida no `localStorage`.

### Adicionar Novo Idioma

1. Crie um novo arquivo em `src/locales/` (ex: `es-es.js`)
2. Adicione as traduções seguindo a estrutura dos arquivos existentes
3. Registre o novo idioma em `src/main.js`
4. Adicione a opção no seletor de idioma nos componentes `Header.vue` e `Resume.vue`

## 📄 Páginas

### Home (`/home`)
Página principal com:
- **Header**: Navegação fixa com links para seções e controles de tema/idioma
- **Me**: Apresentação pessoal com foto e descrição
- **AboutMe**: Seção detalhada sobre background e valores
- **Stacks**: Ecossistema de tecnologias utilizadas
- **Projects**: Projetos mais relevantes com links e descrições
- **Experiences**: Experiência profissional e acadêmica
- **Contact**: Informações de contato e redes sociais

### Resume (`/home/resume`)
Página de currículo otimizada para impressão com:
- Cabeçalho com navegação e controles
- Informações pessoais e de contato
- Resumo profissional
- Experiência profissional detalhada
- Formação acadêmica
- Idiomas
- Botão de download em PDF

## 🚀 Deploy Automático

O projeto utiliza GitHub Actions para deploy automático no GitHub Pages:

### Workflow de CI/CD

O arquivo `.github/workflows/deploy.yml` configura:
1. **Trigger**: Deploy automático em push para branch `main`
2. **Setup**: Configuração do Node.js versão 24
3. **Install**: Instalação de dependências via npm
4. **Build**: Criação do build de produção com Vite
5. **404 Fallback**: Cópria do `index.html` como `404.html` para SPA routing
6. **Deploy**: Publicação no GitHub Pages

### Configuração do Vite

O `vite.config.js` está configurado com:
- `base: '/portfolio/'` para compatibilidade com GitHub Pages
- Alias `@` para imports relativos a `src/`
- Plugins: TailwindCSS, SVG loader, Vue, Vue DevTools

## 🎯 Componentes Principais

### Header.vue
- Navegação responsiva com menu hamburger para mobile
- Controles de tema (dark/light toggle)
- Seletor de idioma (pt-BR/en-USA)
- Links de navegação com scroll suave para seções

### ThemeStore.js (Pinia)
Gerencia o estado do tema:
- `isDark`: Estado atual do tema
- `changeTheme()`: Alterna entre temas
- `initTheme()`: Inicializa tema do localStorage
- Persistência automática no localStorage

### LangStore.js (Pinia)
Gerencia o estado do idioma:
- `lang`: Idioma atual (pt-BR/en-USA)
- `setLang()`: Define novo idioma
- `initLang()`: Inicializa idioma do localStorage e sincroniza com Vue I18n
- Watch automático para atualizar locale do i18n

### MarkdownText.vue
Componente reutilizável para renderização de Markdown:
- Utiliza `markdown-it` para parsing
- Suporte a sintaxe Markdown padrão
- Sanitização básica de HTML

## 🔧 Scripts Disponíveis

```bash
npm run dev      # Inicia servidor de desenvolvimento
npm run build    # Cria build de produção
npm run preview  # Preview do build de produção
```

## 📱 Responsividade

O projeto é totalmente responsivo com breakpoints:
- **Mobile**: < 768px (menu hamburger, layout empilhado)
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px (navegação completa, layout expandido)

## 👨‍💻 Desenvolvedor

**Carlos Daniel Portela**
- Email: carlos.rocha@ufpi.edu.br
- LinkedIn: [carlos-daniel-portela](https://linkedin.com/in/carlos-daniel-portela)
- GitHub: [@carlos-dani-dev](https://github.com/carlos-dani-dev)

## 📄 Licença

Este projeto está sob licença MIT. Sinta-se livre para utilizar e modificar conforme necessário.

## 🚀 Roadmap / Próximos Passos

- [ ] Adicionar animações com Framer Motion ou GSAP
- [ ] Implementar blog pessoal com Markdown
- [ ] Adicionar testes unitários com Vitest
- [ ] Otimizar SEO com meta tags dinâmicas
- [ ] Adicionar PWA capabilities (service worker, manifest)
- [ ] Implementar analytics com Google Analytics ou Plausible
- [ ] Adicionar mais projetos ao portfólio
- [ ] Criar versão em outros idiomas (español, français)
- [ ] Implementar formulário de contato funcional
- [ ] Adicionar seção de publicações acadêmicas
- [ ] Otimizar performance e Lighthouse scores
- [ ] Adicionar modo de apresentação (slides)
