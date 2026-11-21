# Personal filter lists

- Maintain four source lists:
  - `domains/allowlist.txt` + `domains/blocklist.txt`: lowercase domains, one per line, for DNS providers/resolvers.
  - `domains/rewritelist.txt`: hosts-file entries (`IP domain`) for DNS rewrites.
  - `adblock.txt`: browser filters for uBlock Origin, AdGuard, Adblock Plus, and other content blockers. Check compatibility for advanced rules.
- Flag domains appearing in both allow and block lists for a decision rather than silently choosing precedence.
- Add rules only for requested behavior. Prefer narrow scope.
- Add full-line comments when useful: `#` for domain lists, `!` for AdBlock syntax. Avoid inline comments.
- Distinguish syntax checks from live testing. Report untested behavior as unverified.
