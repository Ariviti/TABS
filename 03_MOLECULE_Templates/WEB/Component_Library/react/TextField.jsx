import React, { useId } from "react";
import "../../tokens/components.css";

/**
 * TextField — labeled input with helper text and error state.
 *
 * <TextField label="Work email" placeholder="you@company.com" required />
 * <TextField label="Company" error="This field is required" />
 */
export default function TextField({
  label,
  helperText,
  error,
  required = false,
  id,
  className = "",
  ...rest
}) {
  const autoId = useId();
  const fieldId = id || autoId;
  const helperId = `${fieldId}-helper`;
  const errorId = `${fieldId}-error`;

  return (
    <div className={`ar-field ${className}`.trim()}>
      {label && (
        <label className="ar-field__label" htmlFor={fieldId}>
          {label}
          {required && <span className="ar-field__required" aria-hidden="true">*</span>}
        </label>
      )}
      <input
        id={fieldId}
        className="ar-input"
        aria-invalid={Boolean(error)}
        aria-describedby={error ? errorId : helperText ? helperId : undefined}
        aria-required={required}
        {...rest}
      />
      {error ? (
        <span id={errorId} className="ar-field__error" role="alert">{error}</span>
      ) : helperText ? (
        <span id={helperId} className="ar-field__helper">{helperText}</span>
      ) : null}
    </div>
  );
}
