import React from "react";
import "../../tokens/components.css";

/**
 * Badge — small status/category label.
 * <Badge tone="success">Live</Badge>
 */
export default function Badge({ tone = "neutral", className = "", children, ...rest }) {
  return (
    <span className={`ar-badge ar-badge--${tone} ${className}`.trim()} {...rest}>
      {children}
    </span>
  );
}
