<p align="center">
  <a href="https://macro-deck.app/store/com.sertaycil.discord-soundboard">
    <img src="https://assets.macro-deck.app/branding/Open%20in%20the%20Macro%20Deck%20Store%20Badge%20Dark.png" alt="Open in the Macro Deck Store" height="150">
  </a>
</p>

---

## 🇬🇧 English: Release Notes (v1.0.1)

This update addresses Macro Deck Store review feedback with critical security hardening, architecture refactoring, and seamless native Macro Deck SDK integration.

### 🛡️ Security & Architecture Hardening
- 🔒 **Session Token Authentication:** Added cryptographically secure per-session token validation (`X-Session-Token`) on all local manager API requests.
- 🌐 **Strict CORS & Host Protection:** Removed wildcard CORS (`*`). Enforced strict `Host`, `Origin`, and `Referer` validation restricted strictly to `localhost` and `127.0.0.1`.
- 🛡️ **HTML Injection / XSS Prevention:** Completely rebuilt UI rendering using safe DOM APIs (`document.createElement`, `textContent`, `setAttribute`). All Discord sound, server, and emoji names are strictly escaped.
- ⚡ **Native SDK Compliance:** Removed direct profile file rewrites and force-killing processes. The plugin exclusively manages its data in its own directory (`favorites.json`) and provides audio triggers purely through the official Macro Deck SDK (`PlaySoundAction`).

---

## 🇹🇷 Türkçe: Sürüm Notları (v1.0.1)

Bu sürüm, Macro Deck Mağaza inceleme ekibinin geri bildirimleri doğrultusunda kapsamlı güvenlik sıkılaştırması, sıfır XSS koruması ve resmi Macro Deck SDK uyumluluğu ile güncellenmiştir.

### 🛡️ Güvenlik ve Mimari İyileştirmeleri
- 🔒 **Oturum Belirteci (Session Token) Koruması:** Web arayüzünün yerel API isteklerinde rastgele üretilen oturum belirteci (`X-Session-Token`) zorunlu kılındı.
- 🌐 **Sıkı CORS ve Host Doğrulaması:** Joker karakter CORS (`*`) kaldırıldı; sadece `localhost` ve `127.0.0.1` adreslerinden gelen isteklere izin verildi.
- 🛡️ **HTML Enjeksiyonu (XSS) Koruması:** Arayüzdeki tüm ses, sunucu ve emoji verileri güvenli DOM API'leri (`document.createElement`, `textContent`) ile render edilerek enjeksiyon açıkları kapatıldı.
- ⚡ **Resmi SDK Uyumluluğu:** Dahili profil dosyalarını değiştirme ve zorla yeniden başlatma işlemleri tamamen kaldırılarak Macro Deck SDK standartlarına tam uyum sağlandı.

---

### 📦 Kurulum / Installation:
- **Macro Deck Store:** Search `Discord Soundboard` in Extension Store → Click **Install**.
- **Manuel:** Download `com.sertaycil.discord-soundboard-1.0.0.macroDeckPlugin` below and double-click to install.
