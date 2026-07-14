from pathlib import Path
import re

files = [
    Path(r"c:\Users\Synz\Downloads\Personal website file\index.html"),
    Path(r"c:\Users\Synz\Downloads\Personal website file\dashboard.html"),
    Path(r"c:\Users\Synz\Downloads\Personal website file\receipt.html"),
]

css = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg-main: #fcfbf7;
      --bg-panel: #ffffff;
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --accent-blue: #1e3a8a;
      --accent-gold: #9a3412;
      --border-light: #e2e8f0;
      --border-focus: #1e3a8a;
    }

    body {
      font-family: 'Fredoka', 'Kantumruy Pro', sans-serif;
      background: var(--bg-main);
      color: var(--text-primary);
      line-height: 1.6;
      min-height: 100vh;
    }

    h1, h2, h3, h4 {
      font-family: 'Fredoka', 'Kantumruy Pro', sans-serif;
      font-weight: 700;
      letter-spacing: 0.02em;
      color: var(--accent-blue);
    }

    a { color: inherit; text-decoration: none; }

    .site-header, .site-footer, .hero, .form-section, .estimator-grid, .estimate-total-bar, .admin-panel, .repair-card, .empty-state, .all-repairs, .receipt, .receipt-header, .receipt-body, .payment-block, .toolbar, .no-data-msg, .lookup-bar, .progress-tracker, .repair-card-header, .repair-details, .detail-block, .repairs-table, .qr-panel, .merchant-qr-manager, .cash-panel, .payment-qr-panel, .chat-menu, .chat-toggle, .nav-links a, .btn-primary, .btn-secondary, .status-btn, .btn-print, .btn-back, .estimator-input, .estimator-remove, .estimator-add, .field input, .field select, .field textarea {
      border-radius: 16px;
    }

    .site-header, .site-footer, .hero, .form-section, .estimator-grid, .estimate-total-bar, .admin-panel, .repair-card, .empty-state, .all-repairs, .receipt, .receipt-header, .receipt-body, .payment-block, .toolbar, .no-data-msg, .lookup-bar, .progress-tracker, .repair-card-header, .repairs-table, .qr-panel, .merchant-qr-manager, .cash-panel, .payment-qr-panel, .chat-menu {
      background: var(--bg-panel);
      color: var(--text-primary);
      border: 1px solid var(--border-light);
      box-shadow: 0 16px 45px rgba(15, 23, 42, 0.06);
    }

    .site-header {
      background: var(--bg-panel);
      border-bottom: 1px solid var(--border-light);
      position: sticky;
      top: 0;
      z-index: 100;
      border-radius: 0px !important;
      margin: 0 0 2rem 0;
      width: 100%;
    }

    .header-inner, .container, .toolbar, .receipt-wrapper, .hero-inner {
      max-width: 1200px;
      margin: 0 auto;
      padding: 1.25rem 1.75rem;
    }

    .logo {
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
      color: var(--text-primary);
      text-decoration: none;
    }

    .logo-mark {
      font-family: 'Fredoka', 'Kantumruy Pro', sans-serif;
      font-weight: 700;
      font-size: 1.75rem;
      color: var(--accent-blue);
      border: 2px solid var(--accent-blue);
      padding: 0.1rem 0.45rem;
      line-height: 1;
      border-radius: 10px;
    }

    .logo-text {
      font-family: 'Fredoka', 'Kantumruy Pro', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-primary);
    }

    .nav-links {
      display: flex;
      gap: 0.5rem;
      list-style: none;
    }

    .nav-links a {
      font-family: 'Fredoka', 'Kantumruy Pro', sans-serif;
      font-weight: 600;
      font-size: 0.95rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-secondary);
      text-decoration: none;
      padding: 0.7rem 1rem;
      border: 1px solid var(--border-light);
      background: var(--bg-panel);
      transition: all 0.2s ease;
    }

    .nav-links a:hover, .nav-links a.active {
      background: var(--accent-blue);
      color: #ffffff;
      border-color: var(--accent-blue);
    }

    .hero {
      background: linear-gradient(135deg, #ffffff 0%, #fcfbf7 100%);
      border: 1px solid var(--border-light);
      margin: 0 auto 2rem auto;
      padding: 2rem;
    }

    .hero h1 {
      font-size: clamp(2.2rem, 4.4vw, 3.4rem);
      line-height: 1.02;
      color: var(--accent-blue);
      margin-bottom: 0.85rem;
    }

    .hero h1 span {
      color: var(--accent-gold);
    }

    .hero-meta {
      border-left: 4px solid var(--accent-gold);
      padding-left: 1.25rem;
      color: var(--text-secondary);
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1.75rem 2.5rem;
    }

    .section-title, .page-title {
      font-size: 1.35rem;
      margin-bottom: 0.35rem;
      color: var(--accent-blue);
      display: inline-block;
      padding-bottom: 0.25rem;
      border-bottom: 3px solid var(--accent-gold);
    }

    .section-desc, .page-desc, .admin-label, .detail-block .label, .repair-meta-item .label, .info-block .label, .payment-block .label, .totals-table td:first-child {
      color: var(--text-secondary);
      font-size: 0.95rem;
    }

    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }

    .form-section, .estimator-grid, .estimate-total-bar, .admin-panel, .repair-card, .empty-state, .all-repairs, .lookup-bar, .progress-tracker, .merchant-qr-manager, .qr-panel, .cash-panel, .payment-block {
      margin-bottom: 2rem !important;
      padding: 2rem !important;
    }

    .form-section h2 {
      font-size: 1.15rem;
      margin-bottom: 1rem;
      color: var(--accent-blue);
      padding-bottom: 0.45rem;
      border-bottom: 1px solid var(--border-light);
    }

    .field, .estimator-row, .payment-options, .info-grid, .repair-card-header, .repair-details, .progress-steps {
      margin-bottom: 1.5rem;
    }

    .field label {
      display: block;
      margin-bottom: 0.45rem;
      font-family: 'Fredoka', 'Kantumruy Pro', sans-serif;
      font-weight: 600;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-secondary);
    }

    .field input, .field select, .field textarea, .estimator-input, .estimator-remove, .estimator-add, .btn-primary, .btn-secondary, .btn-print, .btn-back, .status-btn, .lookup-bar input, .lookup-bar button {
      width: 100%;
      padding: 0.9rem 1rem;
      font-family: 'Fredoka', 'Kantumruy Pro', sans-serif;
      font-size: 1rem;
      line-height: 1.4;
      color: var(--text-primary);
      background: var(--bg-panel);
      border: 1px solid var(--border-light);
      outline: none;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
      border-radius: 10px;
    }

    .field input::placeholder, .field textarea::placeholder, .estimator-input::placeholder, .lookup-bar input::placeholder {
      color: var(--text-secondary);
      opacity: 1;
    }

    .field input:focus, .field select:focus, .field textarea:focus, .estimator-input:focus, .lookup-bar input:focus {
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px rgba(30, 58, 138, 0.12);
    }

    .field select {
      appearance: none;
      background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%231e3a8a' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
      background-position: calc(100% - 20px) center;
      background-size: 14px;
      background-repeat: no-repeat;
      padding-right: 2.5rem;
    }

    .field select option {
      color: var(--text-primary);
      background: var(--bg-panel);
    }

    .payment-options {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.75rem;
    }

    .payment-option label {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.35rem;
      padding: 0.95rem 0.85rem;
      border: 1px solid var(--border-light);
      background: var(--bg-panel);
      color: var(--text-secondary);
      cursor: pointer;
      text-align: center;
      border-radius: 10px;
    }

    .payment-option input:checked + label {
      background: var(--accent-blue);
      color: #ffffff;
      border-color: var(--accent-blue);
    }

    .estimator-row {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 140px auto;
      gap: 0.75rem;
      align-items: center;
    }

    .estimator-remove, .estimator-add, .btn-primary, .btn-secondary, .btn-print, .btn-back, .status-btn, .lookup-bar button {
      cursor: pointer;
      font-weight: 600;
      border: 1px solid var(--border-light);
      transition: all 0.2s ease;
    }

    .estimator-remove, .btn-secondary, .btn-back {
      background: var(--bg-panel);
      color: var(--text-secondary);
    }

    .estimator-add, .btn-primary, .btn-print, .lookup-bar button {
      background: var(--accent-blue);
      color: #ffffff;
      border-color: var(--accent-blue);
    }

    .estimator-add:hover, .btn-primary:hover, .btn-print:hover, .lookup-bar button:hover, .nav-links a:hover, .nav-links a.active, .status-btn.active, .status-btn:hover {
      transform: translateY(-1px);
      box-shadow: 0 10px 24px rgba(30, 58, 138, 0.16);
    }

    .estimate-total-bar {
      background: var(--bg-panel);
      border: 1px solid var(--border-light);
    }

    .estimate-total-bar .total-row {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      align-items: center;
      color: var(--text-secondary);
    }

    .estimate-total-bar .total-amount {
      font-size: 1.75rem;
      color: var(--accent-gold);
      font-weight: 700;
    }

    .form-msg {
      margin-top: 0.8rem;
      padding: 0.8rem 1rem;
      border-radius: 10px;
      border: 1px solid var(--border-light);
      color: var(--text-primary);
    }

    .form-msg.success {
      background: #ecfdf3;
      color: #166534;
      border-color: #86efac;
    }

    .form-msg.error {
      background: #fef2f2;
      color: #b91c1c;
      border-color: #fecaca;
    }

    .status-btn {
      background: var(--bg-panel);
      color: var(--text-secondary);
      border: 1px solid var(--border-light);
      font-weight: 600;
    }

    .status-btn.active {
      background: var(--accent-gold);
      color: #ffffff;
      border-color: var(--accent-gold);
    }

    .repair-card-header {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1rem;
    }

    .repair-meta-item .value, .detail-block .value, .info-block .value, .method, .invoice-id {
      font-family: 'Fredoka', 'Kantumruy Pro', sans-serif;
      font-weight: 600;
      color: var(--text-primary);
    }

    .repair-meta-item .value-sub, .info-block .value-sub {
      color: var(--accent-gold);
      font-weight: 600;
      margin-top: 0.2rem;
    }

    .progress-tracker {
      padding: 1.75rem 1.25rem 1rem;
    }

    .progress-steps {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      position: relative;
      align-items: center;
    }

    .progress-line {
      position: absolute;
      top: 18px;
      left: 16.66%;
      right: 16.66%;
      height: 2px;
      background: var(--border-light);
      z-index: 0;
    }

    .progress-line-fill {
      height: 100%;
      width: 0%;
      background: var(--accent-gold);
      transition: width 0.25s ease;
    }

    .progress-step {
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.45rem;
      text-align: center;
    }

    .step-node {
      width: 36px;
      height: 36px;
      border: 2px solid var(--border-light);
      background: var(--bg-panel);
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      border-radius: 10px;
    }

    .progress-step.active .step-node {
      background: var(--accent-gold);
      border-color: var(--accent-gold);
      color: #ffffff;
    }

    .progress-step.completed .step-node {
      background: var(--accent-blue);
      border-color: var(--accent-blue);
      color: #ffffff;
    }

    .step-label {
      font-size: 0.9rem;
      color: var(--text-secondary);
    }

    .detail-block {
      padding: 1rem;
      border-right: 1px solid var(--border-light);
      border-bottom: 1px solid var(--border-light);
    }

    .detail-block:nth-child(even) { border-right: none; }
    .detail-block:nth-last-child(-n+2) { border-bottom: none; }

    .repair-details { display: grid; grid-template-columns: 1fr 1fr; }

    .parts-list {
      list-style: none;
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
    }

    .parts-list li {
      background: var(--bg-main);
      color: var(--text-primary);
      padding: 0.35rem 0.65rem;
      border: 1px solid var(--border-light);
      border-radius: 8px;
    }

    .parts-list li.empty {
      color: var(--text-secondary);
      font-style: italic;
      background: transparent;
      border: none;
    }

    .repairs-table {
      width: 100%;
      border-collapse: collapse;
    }

    .repairs-table th, .repairs-table td {
      padding: 0.85rem 0.95rem;
      text-align: left;
      border-bottom: 1px solid var(--border-light);
      color: var(--text-primary);
    }

    .repairs-table th {
      background: var(--bg-main);
      color: var(--text-secondary);
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .status-badge {
      display: inline-block;
      padding: 0.35rem 0.6rem;
      border: 1px solid var(--border-light);
      color: var(--text-primary);
      background: var(--bg-main);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      font-size: 0.75rem;
      border-radius: 8px;
    }

    .status-badge.ready { color: #166534; border-color: #86efac; background: #ecfdf3; }
    .status-badge.fixing { color: var(--accent-gold); border-color: #fdba74; background: #fff7ed; }

    .receipt-wrapper {
      max-width: 960px;
      margin: 0 auto 2rem;
      padding: 0 1.75rem;
    }

    .receipt {
      background: var(--bg-panel);
      border: 1px solid var(--border-light);
      border-radius: 16px;
      overflow: hidden;
    }

    .receipt-header {
      background: linear-gradient(135deg, #ffffff 0%, #fcfbf7 100%);
      border-bottom: 1px solid var(--border-light);
      padding: 1.5rem 1.75rem;
    }

    .receipt-body {
      padding: 1.5rem 1.75rem 1.75rem;
      background: var(--bg-panel);
    }

    .info-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }

    .line-items {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1rem;
    }

    .line-items th, .line-items td {
      padding: 0.75rem 0.8rem;
      border-bottom: 1px solid var(--border-light);
      text-align: left;
      color: var(--text-primary);
    }

    .line-items th {
      background: var(--bg-main);
      color: var(--text-secondary);
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .totals-table {
      width: 280px;
      border-collapse: collapse;
      margin-left: auto;
    }

    .totals-table td {
      padding: 0.6rem 0.7rem;
      border-bottom: 1px solid var(--border-light);
      color: var(--text-primary);
    }

    .totals-table .grand-total td {
      background: var(--bg-main);
      color: var(--accent-blue);
      font-weight: 700;
    }

    .payment-block {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      margin-top: 1rem;
      padding: 1.25rem;
      border: 1px solid var(--border-light);
      border-radius: 12px;
      background: var(--bg-main);
    }

    .payment-qr-panel img {
      width: 120px;
      height: 120px;
      object-fit: contain;
      border: 1px solid var(--border-light);
      border-radius: 10px;
      background: var(--bg-panel);
      padding: 0.35rem;
    }

    .receipt-footer {
      padding: 1rem 1.75rem;
      background: var(--bg-main);
      color: var(--text-secondary);
      border-top: 1px solid var(--border-light);
      text-align: center;
      font-size: 0.85rem;
    }

    .chat-toggle {
      background: var(--accent-gold);
      color: #ffffff;
      border: 1px solid var(--accent-gold);
      padding: 0.8rem 1rem;
      font-family: 'Fredoka', 'Kantumruy Pro', sans-serif;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-radius: 10px;
    }

    .chat-menu {
      min-width: 220px;
      padding: 0.45rem;
      border-radius: 12px;
      background: var(--bg-panel);
    }

    .chat-menu a {
      display: block;
      padding: 0.7rem 0.8rem;
      color: var(--text-primary);
      text-decoration: none;
      border-radius: 8px;
      margin: 0.2rem 0;
    }

    .chat-menu a:hover {
      background: var(--bg-main);
      color: var(--accent-blue);
    }

    .no-data-msg {
      max-width: 900px;
      margin: 1.5rem auto 2rem;
      padding: 1.5rem 1.75rem;
      text-align: center;
      color: var(--text-secondary);
    }

    .no-data-msg a {
      color: var(--accent-blue);
      font-weight: 700;
    }

    .site-footer {
      max-width: 1200px;
      margin: 0 auto 1.5rem;
      padding: 1rem 1.75rem;
      text-align: center;
      color: var(--text-secondary);
      border-top: 1px solid var(--border-light);
      background: transparent;
      box-shadow: none;
    }

    .form-section.full-width { grid-column: 1 / -1; }

    @media (max-width: 900px) {
      .form-grid, .info-grid, .repair-card-header, .repair-details {
        grid-template-columns: 1fr;
      }

      .payment-options {
        grid-template-columns: 1fr;
      }

      .repair-card-header { display: grid; }
      .detail-block { border-right: none; border-bottom: 1px solid var(--border-light); }
      .detail-block:nth-last-child(-n+2) { border-bottom: 1px solid var(--border-light); }
    }

    @media (max-width: 768px) {
      .nav-links {
        display: none;
      }

      .estimator-row {
        grid-template-columns: 1fr;
      }

      .payment-block {
        flex-direction: column;
      }
    }
"""

pattern = re.compile(r"<style[^>]*>.*?</style>", re.I | re.S)

for path in files:
    text = path.read_text(encoding="utf-8")
    text, count = pattern.subn(f"<style>\n{css}\n  </style>", text, count=1)
    if count != 1:
        raise SystemExit(f"No style block replaced in {path}")
    path.write_text(text, encoding="utf-8")

print("Replaced style blocks in all three HTML files")
