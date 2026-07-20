import os

# 1. Update Astro config to output assets to a clean directory bypassing Jekyll rules
config_path = "website/astro.config.mjs"
config_content = """import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  base: '/cli-beginer-projects/',
  build: {
    assets: 'assets',
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
"""

if os.path.exists(config_path):
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(config_content)
    print("Patched astro.config.mjs with custom assets folder mapping.")

# 2. Re-patch the index.astro frontend with the complete VM, Monaco and project switcher
astro_path = "website/src/pages/index.astro"
if os.path.exists(astro_path):
    with open(astro_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Locate where the prior truncation ended
    target = "isProgra"
    
    # Replace with fully-realized editor initialization and lifecycle hooks
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
        badgeEl.className = `text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded font-mono ${
          p.lang === 'python' ? 'bg-sky-950 text-sky-400 border border-sky-800' :
          p.lang === 'c' ? 'bg-indigo-950 text-indigo-400 border border-indigo-800' :
          p.lang === 'java' ? 'bg-orange-950 text-orange-400 border border-orange-800' :
          'bg-slate-800 text-slate-400'
        }`;
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
          fontFamily: "'Fira Code', monospace"
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
        with open(astro_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully resolved web page truncation, switchProject logic, and Monaco bindings.")
    else:
        # If the file has already been partially edited, overwrite the script segment completely
        print("Warning: Direct match for 'isProgra' not found. Checking if file was already modified.")
