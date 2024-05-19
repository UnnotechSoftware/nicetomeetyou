import {defineConfig, loadEnv} from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import {ElementPlusResolver} from 'unplugin-vue-components/resolvers'



export default defineConfig({
  base: '/admin_news/',
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
  server: {
    cors: true,
    port: 5174,
    proxy: {
      // "/api": "https://thenewstep-system.herokuapp.com",
      "/auth": "http://127.0.0.1:5987",
      "/bonds": "http://127.0.0.1:5987",
      "/orders": "http://127.0.0.1:5987",
      "/dealers": "http://127.0.0.1:5987",
      "/customers": "http://127.0.0.1:5987",
      "/positions": "http://127.0.0.1:5987",
      "/vendors": "http://127.0.0.1:5987",
      "/vendor_quotations": "http://127.0.0.1:5987",
      "/quotations": "http://127.0.0.1:5987",
      "/stat": "http://127.0.0.1:5987",
      "/vendor_tradings": "http://127.0.0.1:5987",
      "/customer_tradings": "http://127.0.0.1:5987",
      "/audits": "http://127.0.0.1:5987",
      "/quotation_audits": "http://127.0.0.1:5987"
    }
  }
})
