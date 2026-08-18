import React from "react";
import "../../tokens/components.css";
import Button from "./Button.jsx";

/**
 * Nav — top navigation bar with brand mark, links, and an action slot.
 *
 * <Nav
 *   links={[{ label: "Product", href: "/product" }, { label: "Pricing", href: "/pricing", current: true }]}
 *   actions={<Button size="sm">Book a demo</Button>}
 * />
 */
export default function Nav({ links = [], actions, brandHref = "/", className = "" }) {
  return (
    <nav className={`ar-nav ${className}`.trim()} aria-label="Primary">
      <a className="ar-nav__brand" href={brandHref}>
        <span className="ar-nav__brand-accent">a</span>riviti
      </a>
      <ul className="ar-nav__links">
        {links.map((link) => (
          <li key={link.href}>
            <a
              className="ar-nav__link"
              href={link.href}
              aria-current={link.current ? "page" : undefined}
            >
              {link.label}
            </a>
          </li>
        ))}
      </ul>
      {actions && <div className="ar-nav__actions">{actions}</div>}
    </nav>
  );
}
