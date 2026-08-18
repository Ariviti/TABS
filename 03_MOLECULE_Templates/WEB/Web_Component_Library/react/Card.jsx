import React from "react";
import "../../tokens/components.css";

/**
 * Card — content container with optional eyebrow/title, or fully custom children.
 *
 * <Card eyebrow="Case Study" title="40% faster claims triage">
 *   Body copy goes here.
 * </Card>
 *
 * <Card interactive onClick={...}><CustomLayout /></Card>
 */
export default function Card({
  eyebrow,
  title,
  interactive = false,
  className = "",
  children,
  ...rest
}) {
  return (
    <div
      className={`ar-card${interactive ? " ar-card--interactive" : ""} ${className}`.trim()}
      role={interactive ? "button" : undefined}
      tabIndex={interactive ? 0 : undefined}
      {...rest}
    >
      {eyebrow && <p className="ar-card__eyebrow">{eyebrow}</p>}
      {title && <h3 className="ar-card__title">{title}</h3>}
      {typeof children === "string" ? <p className="ar-card__body">{children}</p> : children}
    </div>
  );
}
