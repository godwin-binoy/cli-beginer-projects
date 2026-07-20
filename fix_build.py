import os

astro_path = "website/src/pages/index.astro"
workflow_path = ".github/workflows/website.yml"

# 1. Patch arbitrary Tailwind shadows to compile-safe classes in index.astro
if os.path.exists(astro_path):
    with open(astro_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace arbitrary purple shadow with compile-safe Tailwind shadow
    old_shadow_1 = 'shadow-[0_0_15px_rgba(99,102,241,0.15)]'
    new_shadow_1 = 'shadow-indigo-500/15'
    
    # Replace arbitrary green shadow with compile-safe Tailwind shadow
    old_shadow_2 = 'shadow-[0_0_15px_rgba(16,185,129,0.15)]'
    new_shadow_2 = 'shadow-emerald-500/15'

    content = content.replace(old_shadow_1, new_shadow_1)
    content = content.replace(old_shadow_2, new_shadow_2)

    with open(astro_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced arbitrary Tailwind braces with compile-safe shadow utilities.")

# 2. Update Workflow to clear concurrent runs and prevent stale artifact build queues
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

if os.path.exists(workflow_path):
    with open(workflow_path, "w", encoding="utf-8") as f:
        f.write(workflow_content)
    print("Updated workflow concurrency defaults to clear stale deployment queues.")

