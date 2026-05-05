# Aura TV Site

Static GitHub Pages site for the public Aura TV App Store URLs.

## Intended URLs

- Marketing: `https://auratv.mesikalabs.com/`
- Support: `https://auratv.mesikalabs.com/support/`
- Privacy: `https://auratv.mesikalabs.com/privacy/`
- Terms: `https://auratv.mesikalabs.com/terms/`

## App Store Connect

- Apple ID: `6762010608`
- Publisher: `Eliran Mesika`
- Public support contact: `auratv@mesikalabs.com`
- First-release model: free-first player submission with no gated App Store product unlocks exposed
- The support, privacy, and terms pages should keep the same player-only language and public contact identity used in App Store Connect.

## Brand Assets

- `assets/app-icon.png` mirrors the approved iOS 1024 icon from the Aura TV app repo.
- Favicon, Apple touch icon, manifest icons, and Open Graph image assets are generated from the same approved icon source.
- Pages link `site.webmanifest`, favicon PNGs, Apple touch icon, and social preview metadata so public brand surfaces stay consistent.

## Validation

```bash
shasum -a 256 assets/app-icon.png /Users/eliranmesika/Repos/Iptv/Aura-TV-Smart-IPTV-Player/IPTVPlayer/Resources/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png
sips -g pixelWidth -g pixelHeight assets/app-icon.png assets/apple-touch-icon.png assets/favicon-32.png assets/favicon-16.png assets/icon-192.png assets/icon-512.png assets/og-image.png
grep -RInE 'app-icon|apple-touch-icon|favicon|og:image|twitter:image|manifest' . --exclude-dir=.git
curl -I -L https://auratv.mesikalabs.com/ https://auratv.mesikalabs.com/support/ https://auratv.mesikalabs.com/privacy/ https://auratv.mesikalabs.com/terms/
```

## Publish

1. Create a public GitHub repository named `auratv-site`.
2. Push this folder to the repository root on the `main` branch.
3. Enable GitHub Pages from the branch root.
4. Wait for Pages to publish, then verify all four URLs return `200`.
