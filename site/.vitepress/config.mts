import { defineConfig } from 'vitepress'

const repo = 'https://github.com/gdex-waiken/kiro-workshop'

export default defineConfig({
  title: 'Kiro Developer Workshop',
  description: 'Build the same cart API twice with Kiro: spec-driven development, then AI-DLC. Chapter by chapter, with every prompt ready to copy.',
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
        text: 'Chapter 2 · The scenario',
        collapsed: false,
        items: [{ text: '2. The KedaiKu cart', link: '/chapters/02-the-scenario' }],
      },
      {
        text: 'Chapter 3 · Spec-driven development',
        collapsed: false,
        items: [
          { text: '3.0 What a spec is', link: '/chapters/03-spec/' },
          { text: '3.1 Create the spec', link: '/chapters/03-spec/1-create-the-spec' },
          { text: '3.2 Review the requirements', link: '/chapters/03-spec/2-requirements' },
          { text: '3.3 Design and tasks', link: '/chapters/03-spec/3-design-and-tasks' },
          { text: '3.4 Build and check', link: '/chapters/03-spec/4-build-and-check' },
          { text: '3.5 Fix errors', link: '/chapters/03-spec/5-fix-errors' },
        ],
      },
      {
        text: 'Chapter 4 · AI-DLC',
        collapsed: false,
        items: [
          { text: '4.0 The method', link: '/chapters/04-ai-dlc/' },
          { text: '4.1 Set up', link: '/chapters/04-ai-dlc/1-set-up' },
          { text: '4.2 Questions and conflicts', link: '/chapters/04-ai-dlc/2-inception' },
          { text: '4.3 Plan and design', link: '/chapters/04-ai-dlc/3-plan-and-design' },
          { text: '4.4 Construction', link: '/chapters/04-ai-dlc/4-construction' },
          { text: '4.5 Read the record', link: '/chapters/04-ai-dlc/5-the-record' },
        ],
      },
      {
        text: 'Chapter 5 · Compare',
        collapsed: false,
        items: [{ text: '5. Which way to build?', link: '/chapters/05-compare' }],
      },
      {
        text: 'Chapter 6 · Extend Kiro',
        collapsed: false,
        items: [{ text: '6. MCP, skills and powers', link: '/chapters/06-extend-kiro' }],
      },
      {
        text: 'Chapter 7 · Wrap-up',
        collapsed: false,
        items: [
          { text: '7. Roll it out to the team', link: '/chapters/07-wrap-up' },
          { text: 'Cheat sheet', link: '/chapters/cheat-sheet' },
          { text: 'Resources', link: '/chapters/resources' },
        ],
      },
    ],
    outline: [2, 3],
    socialLinks: [{ icon: 'github', link: repo }],
    docFooter: { prev: 'Previous', next: 'Next' },
    footer: {
      message: 'KedaiKu and everyone in the scenario are fictional. Kiro images from kiro.dev. AI-DLC figures from the AWS AI-DLC method definition.',
    },
  },
})
