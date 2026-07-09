# Aura TV Site

Static GitHub Pages site for the public Aura TV app store URLs.

## Intended URLs

- Marketing: `https://auratv.mesikalabs.com/`
- Support: `https://auratv.mesikalabs.com/support/`
- Privacy: `https://auratv.mesikalabs.com/privacy/`
- Terms: `https://auratv.mesikalabs.com/terms/`
- Blog: `https://auratv.mesikalabs.com/blog/`
- Blog feed: `https://auratv.mesikalabs.com/blog/feed.json`
- Robots: `https://auratv.mesikalabs.com/robots.txt`
- Sitemap: `https://auratv.mesikalabs.com/sitemap.xml`
- LLM summary: `https://auratv.mesikalabs.com/llms.txt`

## Store Review Surfaces

- Apple ID: `6762010608`
- Publisher: `Eliran Mesika`
- Public support contact: `auratv@mesikalabs.com`
- Release model: player-only submission focused on user-provided sources
- The support, privacy, and terms pages should keep the same player-only language and public contact identity used in Apple App Store and Google Play review surfaces.

## Brand Assets

- `assets/app-icon.png` mirrors the approved iOS 1024 icon from the Aura TV app repo.
- Favicon, Apple touch icon, manifest icons, and Open Graph image assets are generated from the same approved icon source.
- `assets/og-image.png` is the 1200 x 630 social share export from the app repo's `scripts/generate_social_asset_pack.py`.
- Pages link `site.webmanifest`, favicon PNGs, Apple touch icon, and social preview metadata so public brand surfaces stay consistent.

## Social Identity

- Social profile copy and handle choices are drafted in the app repo under `/Users/eliranmesika/Repos/Iptv/Aura-TV-Smart-IPTV-Player/docs/marketing/`.
- Use `aura-tv-social-identity-guardrails.md` as the policy source, `aura-tv-social-identity-kit.md` for profile copy, and `aura-tv-handle-registry.md` for handle fallback order.
- Do not add social profile links to this site until the matching profiles are MesikaLabs-controlled, verified in the registry, and approved for public linking.

## Validation

```bash
shasum -a 256 assets/app-icon.png /Users/eliranmesika/Repos/Iptv/Aura-TV-Smart-IPTV-Player/IPTVPlayer/Resources/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png
sips -g pixelWidth -g pixelHeight assets/app-icon.png assets/apple-touch-icon.png assets/favicon-32.png assets/favicon-16.png assets/icon-192.png assets/icon-512.png assets/og-image.png
grep -RInE 'app-icon|apple-touch-icon|favicon|og:image|twitter:image|manifest' . --exclude-dir=.git
curl -I -L https://auratv.mesikalabs.com/ https://auratv.mesikalabs.com/support/ https://auratv.mesikalabs.com/privacy/ https://auratv.mesikalabs.com/terms/ https://auratv.mesikalabs.com/blog/ https://auratv.mesikalabs.com/blog/feed.json https://auratv.mesikalabs.com/robots.txt https://auratv.mesikalabs.com/sitemap.xml
```

## Publish

1. Create a public GitHub repository named `auratv-site`.
2. Push this folder to the repository root on the `main` branch.
3. Enable GitHub Pages from the branch root.
4. Wait for Pages to publish, then verify all four URLs return `200`.
