// functions/api/files.js

export async function onRequest(context) {
    const { request, env } = context;
    const url = new URL(request.url);
    const prefix = url.searchParams.get("prefix") || "";

    // Verify R2 bucket binding exists
    if (!env.BUCKET) {
        return new Response(
            JSON.stringify({ error: "R2 bucket not bound to BUCKET environment variable." }),
            { status: 500, headers: { "Content-Type": "application/json" } }
        );
    }

    const CDN_DOMAIN = "https://cdn.ariviti.com";

    try {
        // Query R2 bucket for objects matching the prefix
        const listing = await env.BUCKET.list({ prefix });

        const files = listing.objects
            .filter((obj) => !obj.key.endsWith("/")) // Exclude folder placeholders
            .map((obj) => {
                // Calculate human-readable size
                const bytes = obj.size;
                let sizeHuman = bytes + " B";
                if (bytes >= 1024 * 1024) {
                    sizeHuman = (bytes / (1024 * 1024)).toFixed(1) + " MB";
                } else if (bytes >= 1024) {
                    sizeHuman = (bytes / 1024).toFixed(1) + " KB";
                }

                // Extract filename from object key path
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
            JSON.stringify({ grouped: { files } }),
            {
                headers: {
                    "Content-Type": "application/json",
                    "Cache-Control": "public, max-age=60" // Cache response for 1 minute
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