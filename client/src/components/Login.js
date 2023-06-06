import React from 'react';

export default function Login() {
  const handleLoginFormSubmit = async event => {
    event.preventDefault();
    const email = event.target.email.value;
    const password = event.target.password.value;
    const rememberMe = event.target.rememberMe.checked;

    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password, rememberMe }),
      });
      if (response.ok) {
        // Handle successful login, redirect, etc.
      } else {
        console.log(response)
        throw new Error('Login failed.');
      }
    } catch (error) {
      console.error(error);
      // Handle login error, display error message, etc.
    }
  };

  return (
    <div>
      <div className="page-header">
        <h1>Login</h1>
      </div>
      <div className="col-md-4">
        <form onSubmit={handleLoginFormSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input type="email" className="form-control" id="email" name="email" required />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input type="password" className="form-control" id="password" name="password" required />
          </div>
          <div className="form-group form-check">
            <input type="checkbox" className="form-check-input" id="rememberMe" name="rememberMe" />
            <label className="form-check-label" htmlFor="rememberMe">Remember me</label>
          </div>
          <button type="submit" className="btn btn-primary">Login</button>
        </form>
        <br />
        <p>
          Forgot your password? <a href="/auth/password_reset_request">Click here to reset it</a>.
        </p>
        <p>
          New user? <a href="/auth/register">Click here to register</a>.
        </p>
      </div>
    </div>
  );
}
