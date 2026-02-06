import React from 'react';
import AuthForms from '../components/AuthForms';

const Login = () => {
  const handleAuthSuccess = (authData) => {
    // Redirect to dashboard on successful login
    window.location.href = '/dashboard';
  };

  return (
    <div className="login-page">
      <div className="auth-wrapper">
        <h1>Login to Todo App</h1>
        <AuthForms onAuthSuccess={handleAuthSuccess} />
      </div>
    </div>
  );
};

export default Login;