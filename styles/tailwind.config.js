module.exports = {
    content: ['_site/**/*.html'],
    safelist: [],
    theme: {
      extend: {
      },
    },
    plugins: [
      require('@tailwindcss/typography')
    ],
  }