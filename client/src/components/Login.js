import React, { useState } from "react";
import "./Login.css";

function Login({ onLogin, user }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("")

  function handleSubmit(e) {
    
    e.preventDefault();
    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    })
      .then((r) => {
        if (r.ok) {
          r.json().then((user) => onLogin(user));
        } else {
          r.json().then((err) => setError("Password is incorrect"));
        }
      })
      // r.json())
      // .then((user) => onLogin(user));

      // console.log(user)
  }

  return (
    <div className='login-form'>
    {user ? (<p>{user.email} is currently logged in</p>) : (
      <form onSubmit={handleSubmit}>
        <div className='basic-form-content'>
          <label>Email:</label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <label>Password:</label>
          <input
            type="password"
            id="password"
            autoComplete="current-password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <div className='other-form-content'>
          <button type="submit">Login</button>
          <p color="red">{error}</p>
        </div>
        </form>
      )}
    </div>
  );
}

export default Login;
