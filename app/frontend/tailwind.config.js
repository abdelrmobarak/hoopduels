/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    fontFamily: {
      karantina: ['Karantina', 'sans-serif']
    },
    colors: {
      'orange': '#E78C18',
      'grape': '#EFF0FF',
      'deepblue': '#0070FF',
      'limegreen': '#29FF00',
      'stone': '#7E7E7E',
    },
    extend: {},
  },
  plugins: [],
}

