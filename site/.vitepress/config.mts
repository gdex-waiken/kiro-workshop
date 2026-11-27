import { defineConfig } from 'vitepress'

const repo = 'https://github.com/gdex-waiken/kiro-workshop'

export default defineConfig({
  title: 'Kiro Developer Workshop',
  description: 'Build Lumen Ideas, a staff idea portal, with Kiro: spec-driven development, then AI-DLC, then a brownfield change. Chapter by chapter, with every prompt ready to copy.',
  lang: 'en',
  cleanUrls: true,
  lastUpdated: true,
  head: [['link', { rel: 'icon', href: '/favicon.svg' }]],
  themeConfig: {
    logo: '/images/kiro-ghost.png',
    nav: [
      { text: 'Setup', link: '/chapters/00-setup' },
      { text: 'Prompts', link: '/chapters/prompts' },
      { text: 'Cheat sheet', link: '/chapters/cheat-sheet' },
      { text: 'Debugging', link: '/chapters/troubleshooting' },
    ],
    sidebar: [
      {
        text: 'Session 0 · Mon 7 Dec',
        items: [{ text: 'Setup: get to green', link: '/chapters/00-setup' }],
      },
      {
        text: '9:30 · Open and meet Kiro',
        collapsed: false,
        items: [
          { text: '1. Meet Kiro', link: '/chapters/01-meet-kiro' },
          { text: '2. Extend Kiro', link: '/chapters/02-extend-kiro' },
        ],
      },
      {
        text: '10:00 · Hands-on 1 · Spec',
        collapsed: false,
        items: [
          { text: '3.0 What a spec is', link: '/chapters/03-spec/' },
          { text: '3.1 Create the spec', link: '/chapters/03-spec/1-create-the-spec' },
          { text: '3.2 Hunt for the gaps', link: '/chapters/03-spec/2-requirements' },
          { text: 'Take-home: design and tasks', link: '/chapters/03-spec/3-design-and-tasks' },
          { text: 'Take-home: build and check', link: '/chapters/03-spec/4-build-and-check' },
          { text: 'Take-home: fix errors', link: '/chapters/03-spec/5-fix-errors' },
        ],
      },
      {
        text: '10:30 · From spec to AI-DLC',
        collapsed: false,
        items: [
          { text: '4. Who asks the questions?', link: '/chapters/04-bridge' },
          { text: '5. The stakeholders', link: '/chapters/05-scenario' },
        ],
      },
      {
        text: '11:00 · Hands-on 2 · AI-DLC',
        collapsed: false,
        items: [
          { text: '6.0 How AI-DLC works', link: '/chapters/06-ai-dlc/' },
          { text: '6.1 Start the workflow', link: '/chapters/06-ai-dlc/1-set-up' },
          { text: '6.2 Questions and conflicts', link: '/chapters/06-ai-dlc/2-inception' },
          { text: '6.3 Plan and design', link: '/chapters/06-ai-dlc/3-plan-and-design' },
          { text: '6.4 Build and check', link: '/chapters/06-ai-dlc/4-construction' },
          { text: '6.5 Read the record', link: '/chapters/06-ai-dlc/5-the-record' },
        ],
      },
      {
        text: '12:10 · Hands-on 3 · Brownfield',
        collapsed: false,
        items: [{ text: '7. Add Feature 2 to existing code', link: '/chapters/07-brownfield' }],
      },
      {
        text: '12:50 · Show, trace, roll out',
        collapsed: false,
        items: [
          { text: '8. Show, trace and roll out', link: '/chapters/08-wrap-up' },
          { text: 'Every prompt, in order', link: '/chapters/prompts' },
          { text: 'Cheat sheet', link: '/chapters/cheat-sheet' },
          { text: 'Debugging', link: '/chapters/troubleshooting' },
          { text: 'Resources', link: '/chapters/resources' },
        ],
      },
    ],
    outline: [2, 3],
    socialLinks: [{ icon: 'github', link: repo }],
    docFooter: { prev: 'Previous', next: 'Next' },
    footer: {
      message: 'Velox Group and everyone in the scenario are fictional. Kiro images from kiro.dev. AI-DLC figures from the AWS AI-DLC method definition.',
    },
  },
})
