import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    base: '/',
    alias: {
      '@': '/src' // Ensure '@' points to the 'src' folder
    }
  },
})
