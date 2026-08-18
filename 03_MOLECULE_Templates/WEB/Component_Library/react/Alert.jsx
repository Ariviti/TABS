import React from "react";
import "../../tokens/components.css";

const ICONS = { info: "i", success: "\u2713", warning: "!", danger: "\u2715" };

/**
 * Alert — inline status callout.
 * <Alert tone="warning" title="Review required">
 *   This change affects production data.
 * </Alert>
 */
export default function Alert({ tone = "info", title, className = "", children, ...rest }) {
  return (
    <div className={`ar-alert ar-alert--${tone} ${className}`.trim()} role="status" {...rest}>
      <span className="ar-alert__icon" aria-hidden="true">{ICONS[tone]}</span>
      <div>
        {title && <p className="ar-alert__title">{title}</p>}
        <p className="ar-alert__body">{children}</p>
      </div>
    </div>
  );
}
