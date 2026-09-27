# Resource catalog

The machine-readable catalog is in [`../catalog.json`](../catalog.json). It
contains 49 optional or recommended pointers grouped by role. The catalog tells
the Lead what a resource can provide; it does not install tools or transfer
credentials. Check the provider's current documentation, access model, pricing,
and platform policy before connecting it.

Use the helper to filter it:

```bash
python3 scripts/autospread.py catalog --role analytics
```
