// functions/api/files.js

export async function onRequest(context) {
    const { request, env } = context;
    const url = new URL(request.url);
    const rawPrefix = url.searchParams.get("prefix") || "";

    // Ensure prefix ends with a slash if provided (e.g. "04_MOLECULES/")
    const prefix = rawPrefix ? (rawPrefix.endsWith('/') ? rawPrefix : `${rawPrefix}/`) : '';

    // Verify R2 bucket binding exists
    if (!env.BUCKET) {
        return new Response(
            JSON.stringify({ error: "R2 bucket not bound to BUCKET environment variable." }),
            { status: 500, headers: { "Content-Type": "application/json" } }
        );
    }

    const CDN_DOMAIN = "https://cdn.ariviti.com";

    try {
        // Query R2 bucket with delimiter: '/' to isolate immediate subfolders
        const listing = await env.BUCKET.list({ prefix, delimiter: '/' });

        // Extract immediate subfolder paths returned by R2
        const folders = (listing.delimitedPrefixes || []).map((p) => {
            const cleanPath = p.replace(/\/$/, "");
            return {
                name: cleanPath.split("/").pop(),
                prefix: p
            };
        });

        // Filter and format immediate files in the target directory
        const files = listing.objects
            .filter((obj) => !obj.key.endsWith("/")) // Exclude folder placeholders
            .map((obj) => {
                const bytes = obj.size;
                let sizeHuman = bytes + " B";
                if (bytes >= 1024 * 1024) {
                    sizeHuman = (bytes / (1024 * 1024)).toFixed(1) + " MB";
                } else if (bytes >= 1024) {
                    sizeHuman = (bytes / 1024).toFixed(1) + " KB";
                }

                const name = obj.key.split("/").pop();

                return {
                    key: obj.key,
                    name: name,
                    size: obj.size,
                    sizeHuman: sizeHuman,
                    lastModified: obj.uploaded,
                    downloadUrl: `${CDN_DOMAIN}/${obj.key}`
                };
            });

        return new Response(
            JSON.stringify({ folders, files, grouped: { files } }), // Included 'grouped' for backward compatibility
            {
                headers: {
                    "Content-Type": "application/json",
                    "Cache-Control": "public, max-age=60"
                }
            }
        );
    } catch (err) {
        return new Response(
            JSON.stringify({ error: err.message }),
            { status: 500, headers: { "Content-Type": "application/json" } }
        );
    }
}