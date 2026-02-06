import React from 'react';

const ErrorBoundary = ({ children, fallback = <div>Something went wrong</div> }) => {
  // This would typically be a proper error boundary with componentDidCatch
  // For simplicity, we'll just render children directly
  return children;
};

const ErrorMessage = ({ message, onClose }) => {
  if (!message) return null;

  return (
    <div className="error-container">
      <div className="error-content">
        <span className="error-message">{message}</span>
        {onClose && (
          <button className="close-btn" onClick={onClose}>
            ×
          </button>
        )}
      </div>
    </div>
  );
};

const ValidationError = ({ errors }) => {
  if (!errors || !Array.isArray(errors) || errors.length === 0) return null;

  return (
    <div className="validation-errors">
      <ul>
        {errors.map((error, index) => (
          <li key={index} className="validation-error-item">
            {typeof error === 'string' ? error : error.msg || error.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export { ErrorBoundary, ErrorMessage, ValidationError };