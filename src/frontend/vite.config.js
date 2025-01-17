import { defineConfig } from "vite";

export default defineConfig({
  server: {
    headers: {
      "Cross-Origin-Embedder-Policy": "require-corp",
      "Cross-Origin-Opener-Policy": "same-origin",
      "GameServer": "http://localhost:8000",
      // todo: prod - only add for static/map/*
      "Cache-Control": "max-age=3600",
    },
  },
});
