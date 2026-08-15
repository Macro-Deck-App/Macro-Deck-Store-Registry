# Registry signing

The Macro Deck root public key embedded in the application is the trust anchor. The corresponding
offline root key signs certificates; it does not sign every registry update.

Package artifacts are signed with a Creator or Organization certificate that permits `package`
signing. The signature is stored inside the package format and covers its format-specific canonical
digest.

The registry is signed with a dedicated service certificate that permits `registry` signing. Every
publication generates `registry-manifest.json`, containing a complete, sorted list of the SHA-256
digest and byte size of all public registry data. `registry-signature.json` signs the exact UTF-8
bytes of that manifest.

The package upload, registry changes, generated manifest, and detached registry signature are
prepared in this order:

1. Verify and sign the approved package.
2. Upload the signed package and versioned assets to object storage.
3. Prepare all registry file changes and regenerate the index.
4. Generate the complete registry manifest with a strictly increasing sequence.
5. Sign its exact bytes with the registry service key.
6. Commit and push all registry changes, the manifest, and its signature atomically.

Clients verify the certificate against the pinned root key, require the `registry` key usage, check
the registry signature, reject a lower sequence than previously trusted, and verify every fetched
registry file against the signed manifest. Missing, unknown, duplicated, or unlisted registry data
must fail closed for the official registry.

The public certificate and its detached root signature are published under `certificates/`. Package
release manifests explicitly reference detached package signatures where the package format cannot
carry an embedded signature.
