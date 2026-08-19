/* file-browser.js
   Loaded on every page (see mkdocs.yml → extra_javascript).
   Finds every element with a data-r2-prefix attribute and fills it
   with a live file listing + download links, pulled from R2 via
   functions/api/files.js. This is the whole reason a separate
   "Downloads" page isn't needed — any tier page can show its own
   relevant files inline, filtered to its own folder.

   Usage, inside any .md file (raw HTML passes through untouched):
     <div class="ariviti-file-list" data-r2-prefix="04_MOLECULES"></div>
*/

// Replace DOMContentLoaded listener with this:
if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    document.querySelectorAll("[data-r2-prefix]").forEach(renderFileList);
  });
} else {
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-r2-prefix]").forEach(renderFileList);
  });
}

async function renderFileList(container) {
  const prefix = container.getAttribute("data-r2-prefix");
  container.innerHTML = '<p class="ariviti-file-status">Loading files…</p>';

  try {
    const res = await fetch(`/files?prefix=${encodeURIComponent(prefix)}`);
    if (!res.ok) throw new Error(`API returned ${res.status}`);
    const data = await res.json();

    const files = Object.values(data.grouped || {}).flat();

    if (files.length === 0) {
      container.innerHTML = '<p class="ariviti-file-status">No files uploaded to this folder yet.</p>';
      return;
    }

    const rows = files
      .map(
        (f) => `
      <tr>
        <td>${escapeHtml(f.name)}</td>
        <td>${escapeHtml(f.sizeHuman)}</td>
        <td>${new Date(f.lastModified).toLocaleDateString()}</td>
        <td><a class="md-button md-button--primary" href="${f.downloadUrl}" download>Download</a></td>
      </tr>`
      )
      .join("");

    container.innerHTML = `
      <table class="ariviti-file-table">
        <thead><tr><th>File</th><th>Size</th><th>Updated</th><th></th></tr></thead>
        <tbody>${rows}</tbody>
      </table>`;
  } catch (err) {
    container.innerHTML =
      '<p class="ariviti-file-status">Couldn\u2019t reach storage right now. If this persists, check the R2 binding in the Cloudflare dashboard (Settings \u2192 Functions \u2192 R2 bucket bindings).</p>';
    console.error("Ariviti file browser error:", err);
  }
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}