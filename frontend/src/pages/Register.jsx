import React from 'react';
import AuthForms from '../components/AuthForms';

const Register = () => {
  const handleAuthSuccess = (authData) => {
    // Redirect to dashboard on successful registration
    window.location.href = '/dashboard';
  };

  return (
    <div className="register-page">
      <div className="auth-wrapper">
        <h1>Register for Todo App</h1>
        <AuthForms onAuthSuccess={handleAuthSuccess} />
      </div>
    </div>
  );
};

export default Register;