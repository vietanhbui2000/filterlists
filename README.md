# Personal filter lists

Personal DNS domain lists, DNS rewrites, and browser content-blocking rules.

| File | Purpose | Format |
| --- | --- | --- |
| `adblock.txt` | Block browser requests and unwanted page content | Adblock-style filters |
| `domains2allow.txt` | Allow domains | Lowercase domains, one per line |
| `domains2block.txt` | Block domains | Lowercase domains, one per line |
| `domains2rewrite.txt` | Rewrite domains | IP address + lowercase domains, one per line |

## Adblocker list

For browser extensions such as uBlock Origin, AdGuard, Adblock Plus... and other content blockers. Add the raw URL of `adblock.txt` as a custom filter subscription where supported.

## DNS lists

For [cloudflare-gateway-pihole-scripts](https://github.com/vietanhbui2000/cloudflare-gateway-pihole-scripts), Pi-hole, and other private DNS servers.

Allow and block files contain domains only (`example.com`). The rewrite file uses hosts-file entries (`1.2.3.4 example.com`), one per IP when a domain has several.

Subscribe using raw file URLs where supported; otherwise import the entries. Pi-hole supports subscribed allowlists from v6. Other providers may require format conversion. Allow/block precedence and subdomain matching vary by consumer.

For CGPS, set each raw file URL as a repository variable:

- `ALLOWLIST_URL`: becomes the `Allowlist (manual)` policy. It sits above CGPS's block policies, so it also unblocks domains on the filter lists, including a subdomain of a blocked parent.
- `BLOCKLIST_URL`: becomes the `Blocklist (manual)` policy.
- `REWRITE_URL`: each domain becomes a `Rewrite: <domain>` policy that answers with the listed IPs.

Allow and block entries also match subdomains; rewrites match the exact hostname only. These variables add policies alongside CGPS's filter lists; they don't replace its default sources (`ALLOWLIST_URLS` and `BLOCKLIST_URLS`).

## License

GPL-3.0 license. See [`LICENSE`](./LICENSE) for more information.
