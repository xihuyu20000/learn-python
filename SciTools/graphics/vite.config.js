import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import { resolve } from "path";
import AutoImport from "unplugin-auto-import/vite";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      imports: ["vue", "vue-router"],
    }),
  ],
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/assets/variables.scss";`,
      },
    },
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
      "*": resolve(""),
    },
  },
});
