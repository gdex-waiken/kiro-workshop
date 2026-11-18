import { defineConfig } from 'vitepress'

const repo = 'https://github.com/gdex-waiken/kiro-workshop'

export default defineConfig({
  title: 'Kiro AI-DLC Workshop',
  description: 'Build software with AI-DLC in Kiro: chapter by chapter, from why to a tested cart API.',
  lang: 'en',
  cleanUrls: true,
  lastUpdated: true,
  head: [['link', { rel: 'icon', href: '/favicon.svg' }]],
  themeConfig: {
    nav: [
      { text: 'Start here', link: '/chapters/00-before-you-start' },
      { text: 'Cheat sheet', link: '/chapters/cheat-sheet' },
      { text: 'Repo', link: repo },
    ],
    sidebar: [
      {
        text: 'Before the workshop',
        items: [{ text: '0. Before you start', link: '/chapters/00-before-you-start' }],
      },
      {
        text: 'Concepts',
        items: [
          { text: '1. Why AI-DLC', link: '/chapters/01-why-ai-dlc' },
          { text: '2. Kiro spec mode and steering', link: '/chapters/02-spec-mode-and-steering' },
          { text: '3. What agents really cost', link: '/chapters/03-what-agents-cost' },
          { text: '4. The AI-DLC method', link: '/chapters/04-the-ai-dlc-method' },
        ],
      },
      {
        text: 'Hands-on',
        items: [
          { text: '5. Set up', link: '/chapters/05-set-up' },
          { text: '6. Build the KedaiKu cart', link: '/chapters/06-build-the-cart' },
          { text: '7. Done, demo and traceability', link: '/chapters/07-done-and-demo' },
        ],
      },
      {
        text: 'Wrap-up',
        items: [
          { text: '8. Retro and next steps', link: '/chapters/08-retro-and-next-steps' },
          { text: 'Cheat sheet', link: '/chapters/cheat-sheet' },
          { text: 'Resources', link: '/chapters/resources' },
        ],
      },
    ],
    outline: [2, 3],
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: repo }],
    docFooter: { prev: 'Previous chapter', next: 'Next chapter' },
    footer: {
      message: 'KedaiKu and everyone in the scenario are fictional.',
    },
  },
})
