/* file-browser.js
   Loaded on every page (see mkdocs.yml → extra_javascript).
   Finds every element with a data-r2-prefix attribute and fills it
   with a live, navigable folder and file tree pulled from R2 via
   functions/api/files.js.

   Usage inside any .md file:
     <div class="ariviti-file-list" data-r2-prefix="04_MOLECULES"></div>
*/

if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    document.querySelectorAll("[data-r2-prefix]").forEach((c) => renderFileList(c));
  });
} else {
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-r2-prefix]").forEach((c) => renderFileList(c));
  });
}

async function renderFileList(container, currentPrefix = null) {
  const basePrefix = container.getAttribute("data-r2-prefix");
  const prefix = currentPrefix !== null ? currentPrefix : basePrefix;

  // Track the root prefix for boundary navigation
  if (!container.dataset.basePrefix) {
    container.dataset.basePrefix = basePrefix;
  }

  container.innerHTML = '<p class="ariviti-file-status">Loading directory…</p>';

  try {
    const res = await fetch(`/files?prefix=${encodeURIComponent(prefix)}`);
    if (!res.ok) throw new Error(`API returned ${res.status}`);
    const data = await res.json();

    let folders = data.folders || [];
    let files = data.files || [];

    // Client-side fallback if the API returns a flat list of nested files
    if (!data.folders && data.grouped) {
      const allFiles = Object.values(data.grouped || {}).flat();
      const folderSet = new Set();
      const directFiles = [];

      const cleanPrefix = prefix ? (prefix.endsWith('/') ? prefix : prefix + '/') : '';

      allFiles.forEach((f) => {
        if (!f.key.startsWith(cleanPrefix)) return;
        const relativeKey = f.key.slice(cleanPrefix.length);
        const parts = relativeKey.split('/');

        if (parts.length > 1) {
          folderSet.add(parts[0]);
        } else if (parts[0]) {
          directFiles.push(f);
        }
      });

      folders = Array.from(folderSet).map((name) => ({
        name: name,
        prefix: `${cleanPrefix}${name}/`
      }));
      files = directFiles;
    }

    if (folders.length === 0 && files.length === 0) {
      container.innerHTML = '<p class="ariviti-file-status">No files or subfolders found in this directory.</p>';
      return;
    }

    // Build "Up one level" navigation row if inside a subfolder
    let navHeader = '';
    if (prefix !== container.dataset.basePrefix) {
      const parentPrefix = getParentPrefix(prefix, container.dataset.basePrefix);
      navHeader = `
        <tr class="ariviti-folder-row">
          <td colspan="4">
            <a href="#" class="ariviti-nav-back" data-prefix="${escapeHtml(parentPrefix)}">📁 .. (Up one level)</a>
          </td>
        </tr>`;
    }

    const folderRows = folders
      .map(
        (f) => `
      <tr class="ariviti-folder-row">
        <td colspan="3">
          📁 <a href="#" class="ariviti-folder-link" data-prefix="${escapeHtml(f.prefix)}"><strong>${escapeHtml(f.name)}/</strong></a>
        </td>
        <td><em>Directory</em></td>
      </tr>`
      )
      .join("");

    const fileRows = files
      .map(
        (f) => `
      <tr>
        <td>📄 ${escapeHtml(f.name)}</td>
        <td>${escapeHtml(f.sizeHuman)}</td>
        <td>${new Date(f.lastModified).toLocaleDateString()}</td>
        <td><a class="md-button md-button--primary" href="${f.downloadUrl}" download>Download</a></td>
      </tr>`
      )
      .join("");

    container.innerHTML = `
      <table class="ariviti-file-table">
        <thead><tr><th>Name</th><th>Size</th><th>Updated</th><th>Action</th></tr></thead>
        <tbody>${navHeader}${folderRows}${fileRows}</tbody>
      </table>`;

    // Attach click listeners for seamless directory drilling without page reload
    container.querySelectorAll(".ariviti-folder-link, .ariviti-nav-back").forEach((el) => {
      el.addEventListener("click", (e) => {
        e.preventDefault();
        const nextPrefix = el.getAttribute("data-prefix");
        renderFileList(container, nextPrefix);
      });
    });

  } catch (err) {
    container.innerHTML =
      '<p class="ariviti-file-status">Couldn\u2019t reach storage right now. Check R2 bucket bindings.</p>';
    console.error("Ariviti file browser error:", err);
  }
}

function getParentPrefix(currentPrefix, basePrefix) {
  const clean = currentPrefix.replace(/\/$/, "");
  const parts = clean.split("/");
  parts.pop();
  const parent = parts.join("/");
  return parent.length < basePrefix.length ? basePrefix : parent;
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}