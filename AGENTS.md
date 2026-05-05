# Aura TV Site Agent Notes

## Product Focus

- This repo is the static public site for Aura TV App Store URLs.
- Keep the site aligned with the free, player-only Aura TV positioning.
- Aura TV does not provide channels, playlists, broadcaster accounts, catalogs, or content access.
- Do not add money-gated product copy unless the active App Store release plan explicitly reintroduces that positioning.

## Contact Points

- General support: `support@mesikalabs.com`
- Privacy: `privacy@mesikalabs.com`
- Legal: `legal@mesikalabs.com`
- App-specific support: `auratv@mesikalabs.com`

Use `auratv@mesikalabs.com` for Aura TV support surfaces and the policy-specific MesikaLabs addresses for privacy and legal pages.

## Brand Asset Contract

- `assets/app-icon.png` must mirror the approved iOS 1024 icon from `/Users/eliranmesika/Repos/Iptv/Aura-TV-Smart-IPTV-Player/IPTVPlayer/Resources/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png`.
- Favicon, Apple touch icon, manifest icons, and Open Graph image assets should be regenerated from that same approved icon source.
- Keep homepage, support, privacy, terms, metadata, and manifest copy consistent with the free player-only App Store packet.

## Validation

- Icon parity: `shasum -a 256 assets/app-icon.png /Users/eliranmesika/Repos/Iptv/Aura-TV-Smart-IPTV-Player/IPTVPlayer/Resources/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png`
- Asset dimensions: `sips -g pixelWidth -g pixelHeight assets/app-icon.png assets/apple-touch-icon.png assets/favicon-32.png assets/favicon-16.png assets/icon-192.png assets/icon-512.png assets/og-image.png`
- Brand metadata scan: `grep -RInE 'app-icon|apple-touch-icon|favicon|og:image|twitter:image|manifest' . --exclude-dir=.git`
- Local smoke test: `python3 -m http.server 8087 --bind 127.0.0.1`, then check `/`, `/support/`, `/privacy/`, `/terms/`, `/assets/app-icon.png`, and `/site.webmanifest`.
- Hosted URL checks: `curl -I -L https://auratv.mesikalabs.com/ https://auratv.mesikalabs.com/support/ https://auratv.mesikalabs.com/privacy/ https://auratv.mesikalabs.com/terms/`
