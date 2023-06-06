import React from 'react';

export default function Register() {
  const handleRegistrationFormSubmit = async event => {
    event.preventDefault();
    const email = event.target.email.value;
    const password = event.target.password.value;
    // Add any additional form fields as needed

    try {
      const response = await fetch('http://127.0.0.1:5000/auth/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });
      if (response.ok) {
        // Handle successful registration, redirect, etc.
      } else {
        throw new Error('Registration failed.');
      }
    } catch (error) {
      console.error(error);
      // Handle registration error, display error message, etc.
    }
  };

  return (
    <div>
      <div className="page-header">
        <h1>Register</h1>
      </div>
      <div className="col-md-4">
        <form onSubmit={handleRegistrationFormSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input type="email" className="form-control" id="email" name="email" required />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input type="password" className="form-control" id="password" name="password" required />
          </div>
          {/* Add any additional form fields here */}
          <button type="submit" className="btn btn-primary">Register</button>
        </form>
      </div>
    </div>
  );
}
