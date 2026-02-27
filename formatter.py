from datetime import datetime



today = datetime.now().strftime("%B %d, %Y")

    if not deals:
        plain = "No PlayStation Store deals found today."
        html  = f"<html><body><p>No deals found on {today}.</p></body></html>"
        return plain, html

    # ── Plain Text ─────────────────────────────────────────
    plain_lines = [f"PlayStation Store Deals — {today}", "=" * 50]

    for d in deals:
        title      = d.get("name", "Unknown Title")
        platform   = ", ".join(d.get("platforms", [])) or "PS"
        original   = d.get("regular_price", "N/A")
        sale_price = d.get("sale_price", "N/A")
        discount   = d.get("discount", "?")
        end_date   = d.get("sale_end_date", "")[:10] if d.get("sale_end_date") else "N/A"
        url        = d.get("url", "")

        plain_lines.append(
            f"\n🎮 {title} [{platform}]\n"
            f"   {original} → {sale_price}  ({discount}% OFF)\n"
            f"   Sale ends: {end_date}\n"
            f"   {url}"
        )

    plain_text = "\n".join(plain_lines)

    # ── HTML ───────────────────────────────────────────────
    rows = []
    for d in deals:
        title      = d.get("name", "Unknown Title")
        platform   = ", ".join(d.get("platforms", [])) or "PS"
        original   = d.get("regular_price", "N/A")
        sale_price = d.get("sale_price", "N/A")
        discount   = d.get("discount", "?")
        end_date   = d.get("sale_end_date", "")[:10] if d.get("sale_end_date") else "N/A"
        url        = d.get("url", "")

        rows.append(f"""
        <tr>
          <td style="padding:8px; border-bottom:1px solid #333;">
            <a href="{url}" style="color:#0070cc; text-decoration:none; font-weight:bold;">{title}</a>
            <br><small style="color:#aaa;">{platform}</small>
          </td>
          <td style="padding:8px; border-bottom:1px solid #333; text-align:center;">
            <span style="text-decoration:line-through; color:#888;">{original}</span>
          </td>
          <td style="padding:8px; border-bottom:1px solid #333; text-align:center; color:#00c853; font-weight:bold;">
            {sale_price}
          </td>
          <td style="padding:8px; border-bottom:1px solid #333; text-align:center; color:#ff6b6b; font-weight:bold;">
            {discount}% OFF
          </td>
          <td style="padding:8px; border-bottom:1px solid #333; text-align:center; color:#aaa;">
            {end_date}
          </td>
        </tr>""")

    html = f"""
    <html><body style="background:#1a1a2e; color:#eee; font-family:Arial,sans-serif; padding:20px;">
      <div style="max-width:800px; margin:auto;">
        <h1 style="color:#0070cc;">🎮 PlayStation Store Deals</h1>
        <p style="color:#aaa;">{today} &nbsp;|&nbsp; {len(deals)} deals found</p>
        <table width="100%" cellspacing="0" style="border-collapse:collapse; background:#16213e; border-radius:8px; overflow:hidden;">
          <thead>
            <tr style="background:#0070cc; color:#fff;">
              <th style="padding:10px; text-align:left;">Game</th>
              <th style="padding:10px;">Original</th>
              <th style="padding:10px;">Sale Price</th>
              <th style="padding:10px;">Discount</th>
              <th style="padding:10px;">Ends</th>
            </tr>
          </thead>
          <tbody>
            {''.join(rows)}
          </tbody>
        </table>
        <p style="color:#555; font-size:12px; margin-top:20px;">
          Powered by PSDeals.net · Disable your cron job to stop receiving these.
        </p>
      </div>
    </html></body>
    """
    return plain_text, html