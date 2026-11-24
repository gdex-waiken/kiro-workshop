import { defineConfig } from 'vitepress'

const repo = 'https://github.com/gdex-waiken/kiro-workshop'

export default defineConfig({
  title: 'Kiro Developer Workshop',
  description: 'Build Pelita Ideas, a staff idea portal, with Kiro: spec-driven development, then AI-DLC, then a brownfield change. Chapter by chapter, with every prompt ready to copy.',
  lang: 'en',
  cleanUrls: true,
  lastUpdated: true,
  head: [['link', { rel: 'icon', href: '/favicon.svg' }]],
  themeConfig: {
    logo: '/images/kiro-ghost.png',
    nav: [
      { text: 'Start here', link: '/chapters/00-before-you-start' },
      { text: 'Cheat sheet', link: '/chapters/cheat-sheet' },
    ],
    sidebar: [
      {
        text: 'Before the workshop',
        items: [{ text: '0. Before you start', link: '/chapters/00-before-you-start' }],
      },
      {
        text: 'Chapter 1 · Meet Kiro',
        collapsed: false,
        items: [{ text: '1. Meet Kiro', link: '/chapters/01-meet-kiro' }],
      },
      {
        text: 'Chapter 2 · Extend Kiro',
        collapsed: false,
        items: [{ text: '2. MCP, skills and powers', link: '/chapters/02-extend-kiro' }],
      },
      {
        text: 'Chapter 3 · Compare',
        collapsed: false,
        items: [{ text: '3. Vibe, spec or AI-DLC?', link: '/chapters/03-compare' }],
      },
      {
        text: 'Chapter 4 · The scenario',
        collapsed: false,
        items: [{ text: '4. Pelita Ideas', link: '/chapters/04-the-scenario' }],
      },
      {
        text: 'Chapter 5 · Spec-driven development',
        collapsed: false,
        items: [
          { text: '5.0 What a spec is', link: '/chapters/05-spec/' },
          { text: '5.1 Create the spec', link: '/chapters/05-spec/1-create-the-spec' },
          { text: '5.2 Review the requirements', link: '/chapters/05-spec/2-requirements' },
          { text: '5.3 Design and tasks', link: '/chapters/05-spec/3-design-and-tasks' },
          { text: '5.4 Build and check', link: '/chapters/05-spec/4-build-and-check' },
          { text: '5.5 Fix errors', link: '/chapters/05-spec/5-fix-errors' },
        ],
      },
      {
        text: 'Chapter 6 · AI-DLC (greenfield)',
        collapsed: false,
        items: [
          { text: '6.0 The method', link: '/chapters/06-ai-dlc/' },
          { text: '6.1 Set up', link: '/chapters/06-ai-dlc/1-set-up' },
          { text: '6.2 Questions and conflicts', link: '/chapters/06-ai-dlc/2-inception' },
          { text: '6.3 Plan and design', link: '/chapters/06-ai-dlc/3-plan-and-design' },
          { text: '6.4 Construction', link: '/chapters/06-ai-dlc/4-construction' },
          { text: '6.5 Read the record', link: '/chapters/06-ai-dlc/5-the-record' },
        ],
      },
      {
        text: 'Chapter 7 · Brownfield',
        collapsed: false,
        items: [{ text: '7. Add Feature 2 to existing code', link: '/chapters/07-brownfield' }],
      },
      {
        text: 'Chapter 8 · Wrap-up',
        collapsed: false,
        items: [
          { text: '8. Wrap-up and roll-out', link: '/chapters/08-wrap-up' },
          { text: 'Cheat sheet', link: '/chapters/cheat-sheet' },
          { text: 'Resources', link: '/chapters/resources' },
        ],
      },
    ],
    outline: [2, 3],
    socialLinks: [{ icon: 'github', link: repo }],
    docFooter: { prev: 'Previous', next: 'Next' },
    footer: {
      message: 'Pelita Group and everyone in the scenario are fictional. Kiro images from kiro.dev. AI-DLC figures from the AWS AI-DLC method definition.',
    },
  },
})
