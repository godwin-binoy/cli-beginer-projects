import os, re
astro_path = None
config_path = None
workflow_path = None

for root, dirs, files in os.walk("."):
    if "index.astro" in files and "pages" in root:
        astro_path = os.path.join(root, "index.astro")
    if "astro.config.mjs" in files:
        config_path = os.path.join(root, "astro.config.mjs")
    if "website.yml" in files:
        workflow_path = os.path.join(root, "website.yml")

if astro_path:
    with open(astro_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace("shadow-[0_0_15px_rgba(99,102,241,0.15)]", "shadow-indigo-500/15")
    content = content.replace("shadow-[0_0_15px_rgba(16,185,129,0.15)]", "shadow-emerald-500/15")
    content = re.sub(r"shadow-\[[^\]]*rgba\([^)]+\)[^\]]*\]", "shadow-indigo-500/15", content)

    target = "isProgra"
    replacement = """isProgramRunning = false;
      activeVM = null;
      term.write("guest@cli-playground:~$ ");
    }

    // Stateful Project Switcher & Editor Updater
    function switchProject(id) {
      activeProjectId = id;
      const p = PROJECTS.find(proj => proj.id === id);
      if (!p) return;

      // Update active layout state in repository map
      renderExplorer(fileSearch.value);

      // Update top header labels
      const filenameEl = document.getElementById("editor-filename");
      const badgeEl = document.getElementById("editor-badge");
      if (filenameEl) filenameEl.textContent = p.filename;
      if (badgeEl) {
        badgeEl.textContent = p.badge;
        badgeEl.className = "text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded font-mono " + (
          p.lang === "python" ? "bg-sky-950 text-sky-400 border border-sky-800" :
          p.lang === "c" ? "bg-indigo-950 text-indigo-400 border border-indigo-800" :
          p.lang === "java" ? "bg-orange-950 text-orange-400 border border-orange-800" :
          "bg-slate-800 text-slate-400"
        );
      }

      // Load code buffer into editor session
      if (editorInstance) {
        editorInstance.setValue(modifiedCodes[id] || p.code);
        const model = editorInstance.getModel();
        if (model) {
          monaco.editor.setModelLanguage(model, p.lang);
        }
      }

      // Update preview if markdown page is currently open
      const readmeContainer = document.getElementById("readme-view-container");
      if (readmeContainer && !readmeContainer.classList.contains("hidden")) {
        document.getElementById("readme-content").innerHTML = parseMarkdown(p.readme);
      }
    }

    // Set up control click bindings
    document.getElementById("btn-run").addEventListener("click", () => {
      launchProgram(activeProjectId);
    });

    document.getElementById("btn-reset").addEventListener("click", () => {
      const p = PROJECTS.find(proj => proj.id === activeProjectId);
      if (p) {
        modifiedCodes[p.id] = p.code;
        if (editorInstance) {
          editorInstance.setValue(p.code);
        }
      }
    });

    document.getElementById("btn-clear").addEventListener("click", () => {
      if (term) term.write("\\x1b[2J\\x1b[H");
    });

    // Initialize application runtime
    initTerminal().then(() => {
      renderExplorer();
      
      loadMonaco(() => {
        const container = document.getElementById("editor-container");
        if (!container) return;

        const p = PROJECTS.find(proj => proj.id === activeProjectId);
        editorInstance = monaco.editor.create(container, {
          value: p ? p.code : "",
          language: p ? p.lang : "python",
          theme: "vs-dark",
          automaticLayout: true,
          fontSize: 13,
          minimap: { enabled: false },
          lineNumbers: "on",
          roundedSelection: true,
          scrollBeyondLastLine: false,
          readOnly: false,
          fontFamily: "\\"Fira Code\\", monospace"
        });

        // Track code changes
        editorInstance.onDidChangeModelContent(() => {
          if (activeProjectId) {
            modifiedCodes[activeProjectId] = editorInstance.getValue();
          }
        });

        // Set initial selected project state
        if (activeProjectId) {
          switchProject(activeProjectId);
        }
      });
    });
  </script>
</body>
</html>"""

    if target in content:
        content = content.replace(target, replacement)
        print("Patched index.astro script.")

    with open(astro_path, "w", encoding="utf-8") as f:
        f.write(content)

if config_path:
    config_content = """import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  base: "/cli-beginer-projects/",
  build: {
    assets: "assets",
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
"""
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(config_content)
    print("Patched config.")

if workflow_path:
    workflow_content = """name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Node.js Environment
        uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Install Dependencies
        run: |
          cd website
          npm install

      - name: Build Astro Website
        run: |
          cd website
          npm run build

      - name: Upload Pages Artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: website/dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""
    with open(workflow_path, "w", encoding="utf-8") as f:
        f.write(workflow_content)
    print("Patched workflow.")
