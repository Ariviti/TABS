import React from "react";
import "../../tokens/components.css";

/**
 * Button — primary / secondary / ghost variants, 3 sizes.
 *
 * <Button variant="primary" onClick={...}>Get started</Button>
 * <Button variant="ghost" size="sm" disabled>Not now</Button>
 */
export default function Button({
  variant = "primary",   // "primary" | "secondary" | "ghost"
  size = "md",            // "sm" | "md" | "lg"
  disabled = false,
  as: Component = "button",
  className = "",
  children,
  ...rest
}) {
  const sizeClass = size !== "md" ? ` ar-btn--${size}` : "";
  return (
    <Component
      className={`ar-btn ar-btn--${variant}${sizeClass} ${className}`.trim()}
      disabled={Component === "button" ? disabled : undefined}
      aria-disabled={Component !== "button" ? disabled : undefined}
      {...rest}
    >
      {children}
    </Component>
  );
}
