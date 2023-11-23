import { defineConfig } from "vite";
import path from "path";
import vue from "@vitejs/plugin-vue";
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import { ElementPlusResolver } from "unplugin-vue-components/resolvers";

export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
    AutoImport({
      imports: ["vue"],
    }),
  ],

  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        javascriptEnabled: true,
        additionalData: `@import "/src/assets/styles/global.scss";`,
      },
    },
  },
  server: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8765", //你的服务器地址
        changeOrigin: true, // 允许跨域
      },
    },
    resolve: {
      alias: [
        {
          find: "@",
          replacement: path.resolve("./src"),
        },
      ],
    },
  },
});
